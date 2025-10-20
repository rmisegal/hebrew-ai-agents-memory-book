#!/usr/bin/env python3
"""
OAuth 2.0 Setup for Gmail API

This script helps you authenticate with Gmail API and generate token.json
Run this once before using the MCP server.

Setup Instructions:
1. Go to https://console.cloud.google.com/
2. Create a new project or select existing
3. Enable Gmail API
4. Create OAuth 2.0 credentials (Desktop app)
5. Download credentials JSON and save as 'private/credentials.json'
6. Run this script: python setup_oauth.py
"""

import os
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# Scopes required for Gmail readonly access
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def setup_oauth():
    """Run OAuth flow and save token"""
    creds = None
    token_path = 'private/token.json'
    credentials_path = 'private/credentials.json'

    # Check if credentials.json exists
    if not os.path.exists(credentials_path):
        print("ERROR: credentials.json not found!")
        print("\nPlease follow these steps:")
        print("1. Go to https://console.cloud.google.com/")
        print("2. Create/select a project")
        print("3. Enable Gmail API")
        print("4. Create OAuth 2.0 credentials (Desktop app)")
        print("5. Download JSON and save as 'private/credentials.json'")
        return False

    # Check if token already exists
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)

    # If no valid credentials, run OAuth flow
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            print("Refreshing expired token...")
            creds.refresh(Request())
        else:
            print("Starting OAuth flow...")
            print("A browser window will open for authentication.")
            flow = InstalledAppFlow.from_client_secrets_file(
                credentials_path, SCOPES)
            creds = flow.run_local_server(port=0)

        # Save token
        os.makedirs('private', exist_ok=True)
        with open(token_path, 'w') as token:
            token.write(creds.to_json())
        print(f"✓ Token saved to {token_path}")

    print("\n✓ OAuth setup complete!")
    print("You can now use the Gmail MCP server.")
    return True


if __name__ == '__main__':
    setup_oauth()
