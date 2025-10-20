#!/usr/bin/env python3
"""
Gmail MCP Server with Official MCP Python SDK
Based on Appendix E from the book

This implementation uses the official MCP Python SDK to create
a Model Context Protocol server for Gmail operations.
"""

import os
import csv
import asyncio
from datetime import datetime
from typing import Optional

# MCP SDK imports
from mcp.server import Server
from mcp.types import Tool, TextContent

# Google API imports
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


# Initialize MCP Server
app = Server("gmail-extractor")

# Gmail API setup
def get_gmail_service():
    """Initialize Gmail API service with credentials"""
    try:
        creds = Credentials.from_authorized_user_file(
            'private/token.json',
            scopes=['https://www.googleapis.com/auth/gmail.readonly']
        )
        return build('gmail', 'v1', credentials=creds)
    except FileNotFoundError:
        raise Exception("Token file not found. Please run OAuth setup first.")
    except Exception as e:
        raise Exception(f"Failed to initialize Gmail service: {e}")


# Initialize service globally
gmail_service = None


@app.list_tools()
async def list_tools() -> list[Tool]:
    """List available tools"""
    return [
        Tool(
            name="search_and_export_emails",
            description="Search Gmail by label and date range, export results to CSV file with UTF-8 encoding",
            inputSchema={
                "type": "object",
                "properties": {
                    "label": {
                        "type": "string",
                        "description": "Gmail label to filter by (e.g., 'INBOX', 'Research_Data'). Optional."
                    },
                    "start_date": {
                        "type": "string",
                        "description": "Start date in YYYY-MM-DD format. Optional."
                    },
                    "end_date": {
                        "type": "string",
                        "description": "End date in YYYY-MM-DD format. Optional."
                    },
                    "max_results": {
                        "type": "integer",
                        "description": "Maximum number of results to return. Default: 100",
                        "default": 100
                    }
                }
            }
        )
    ]


@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """Handle tool calls"""
    global gmail_service

    if gmail_service is None:
        gmail_service = get_gmail_service()

    if name == "search_and_export_emails":
        return await search_and_export_emails(
            label=arguments.get("label"),
            start_date=arguments.get("start_date"),
            end_date=arguments.get("end_date"),
            max_results=arguments.get("max_results", 100)
        )
    else:
        raise ValueError(f"Unknown tool: {name}")


async def search_and_export_emails(
    label: Optional[str] = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    max_results: int = 100
) -> list[TextContent]:
    """
    Search emails and export to CSV file.

    Args:
        label: Gmail label to filter by (optional)
        start_date: Start date in YYYY-MM-DD format (optional)
        end_date: End date in YYYY-MM-DD format (optional)
        max_results: Maximum number of results (default: 100)

    Returns:
        TextContent with JSON response containing success status and file path
    """
    try:
        # Build search query
        query = ""
        if label:
            query += f"label:{label} "
        if start_date:
            query += f"after:{start_date} "
        if end_date:
            query += f"before:{end_date} "

        # Execute search
        results = gmail_service.users().messages().list(
            userId='me',
            q=query.strip(),
            maxResults=max_results
        ).execute()

        messages = results.get('messages', [])

        if not messages:
            return [TextContent(
                type="text",
                text='{"success": true, "count": 0, "message": "No emails found matching criteria"}'
            )]

        # Generate output filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        label_name = label.replace('/', '_') if label else 'emails'
        output_file = f"csv/{label_name}_{timestamp}.csv"

        # Ensure csv directory exists
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

        # Export to CSV with UTF-8-sig encoding (Excel compatible)
        with open(output_file, 'w', newline='', encoding='utf-8-sig') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Date", "From", "Subject"])

            for msg in messages:
                try:
                    msg_data = gmail_service.users().messages().get(
                        userId='me',
                        id=msg['id'],
                        format='metadata',
                        metadataHeaders=['Date', 'From', 'Subject']
                    ).execute()

                    headers = {h['name']: h['value']
                              for h in msg_data.get('payload', {}).get('headers', [])}

                    writer.writerow([
                        headers.get('Date', ''),
                        headers.get('From', ''),
                        headers.get('Subject', '')
                    ])
                except Exception as e:
                    print(f"Error processing message {msg['id']}: {e}")
                    continue

        # Return success response
        response = {
            "success": True,
            "count": len(messages),
            "message": f"Successfully exported {len(messages)} emails",
            "output_file": output_file,
            "query": query.strip() if query else "all emails"
        }

        return [TextContent(
            type="text",
            text=str(response)
        )]

    except HttpError as e:
        error_response = {
            "success": False,
            "error": f"Gmail API error: {e}",
            "message": "Failed to fetch emails"
        }
        return [TextContent(
            type="text",
            text=str(error_response)
        )]

    except Exception as e:
        error_response = {
            "success": False,
            "error": str(e),
            "message": "An error occurred"
        }
        return [TextContent(
            type="text",
            text=str(error_response)
        )]


async def main():
    """Run the MCP server"""
    from mcp.server.stdio import stdio_server

    async with stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options()
        )


if __name__ == "__main__":
    asyncio.run(main())
