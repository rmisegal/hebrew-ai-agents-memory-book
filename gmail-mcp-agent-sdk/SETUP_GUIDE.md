# Gmail MCP Server SDK - Complete Setup Guide

## Current Status

❌ **Python Version Issue**: Your system has Python 3.9.0, but the MCP SDK requires Python 3.10+

## What You Need

### 1. Python 3.10 or Higher

The official `mcp` package requires Python >=3.10.

**Download Python 3.11+:**
- Windows: https://www.python.org/downloads/windows/
- Direct link: https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe

**Installation Steps:**
1. Download Python 3.11.9 (or later)
2. Run installer
3. ✅ **CHECK** "Add Python to PATH"
4. Choose "Install Now"
5. Verify: Open new CMD and run `python --version`

### 2. Google Cloud OAuth Credentials

You'll need a Google Cloud project with Gmail API enabled.

## Step-by-Step Setup

### Step 1: Install Python 3.10+

After installing Python 3.11:

```bash
# Verify version
python --version
# Should show: Python 3.11.x or higher
```

### Step 2: Recreate Virtual Environment

```bash
cd "C:\25D\GeneralLearning\gmail_ai_agent_book_and_example\gmail-mcp-agent-sdk"

# Remove old venv
rmdir /s /q venv

# Create new venv with Python 3.11+
python -m venv venv

# Activate
venv\Scripts\activate

# Install requirements
pip install -r requirements.txt
```

### Step 3: Set Up Google OAuth

#### 3.1 Create Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Click "Select a project" → "NEW PROJECT"
3. Name it (e.g., "Gmail MCP Agent")
4. Click "CREATE"

#### 3.2 Enable Gmail API

1. In your project, go to "APIs & Services" → "Library"
2. Search for "Gmail API"
3. Click "ENABLE"

#### 3.3 Create OAuth Credentials

1. Go to "APIs & Services" → "Credentials"
2. Click "CREATE CREDENTIALS" → "OAuth client ID"
3. If prompted, configure consent screen:
   - User Type: **External**
   - App name: "Gmail MCP Agent"
   - User support email: your email
   - Developer contact: your email
   - Scopes: Add `https://www.googleapis.com/auth/gmail.readonly`
   - Test users: Add your Gmail address
   - Click "SAVE AND CONTINUE"
4. Back to credentials:
   - Application type: **Desktop app**
   - Name: "Gmail MCP Desktop"
   - Click "CREATE"
5. Download JSON file
6. Save it as: `C:\25D\GeneralLearning\gmail_ai_agent_book_and_example\gmail-mcp-agent-sdk\private\credentials.json`

#### 3.4 Run OAuth Setup

```bash
cd "C:\25D\GeneralLearning\gmail_ai_agent_book_and_example\gmail-mcp-agent-sdk"
venv\Scripts\activate
python setup_oauth.py
```

This will:
- Open browser for Google authentication
- Ask you to select your Google account
- Request permission to read Gmail
- Save `private/token.json`

### Step 4: Test the Server

```bash
# Test server runs
python gmail_mcp_server_sdk.py
```

The server should start and wait for MCP protocol messages (STDIO mode).
Press `Ctrl+C` to stop.

### Step 5: Configure Claude CLI

Find your Claude config file:
- Windows: `%USERPROFILE%\.claude\config.json`
- Linux/Mac: `~/.claude/config.json`

If it doesn't exist, create it:

```json
{
  "mcpServers": {
    "gmail-extractor": {
      "command": "C:/25D/GeneralLearning/gmail_ai_agent_book_and_example/gmail-mcp-agent-sdk/venv/Scripts/python.exe",
      "args": [
        "C:/25D/GeneralLearning/gmail_ai_agent_book_and_example/gmail-mcp-agent-sdk/gmail_mcp_server_sdk.py"
      ]
    }
  }
}
```

**Note:** Use **forward slashes** `/` even on Windows in the config file.

### Step 6: Test with Claude

Start Claude CLI:

```bash
claude
```

Try these commands:

```
# List available tools
/tools

# Use the Gmail tool
Search my Gmail for emails with label "INBOX" from the last 7 days and export to CSV
```

Or more specifically:

```
Use the gmail-extractor tool with these parameters:
- label: INBOX
- start_date: 2025-10-13
- end_date: 2025-10-20
- max_results: 10
```

### Step 7: Verify CSV Creation

Check the `csv/` directory:

```bash
dir csv
```

You should see a file like: `INBOX_20251020_153045.csv`

Open it in Excel or any text editor to verify the emails were exported correctly.

## Troubleshooting

### "ModuleNotFoundError: No module named 'mcp'"

Your Python is < 3.10. Install Python 3.11+ and recreate venv.

### "Token file not found"

Run `python setup_oauth.py` first.

### "Gmail API not enabled"

Enable Gmail API in Google Cloud Console.

### CSV file has garbled Hebrew text

The file uses UTF-8 with BOM. Open in:
- Excel: Should work automatically
- Notepad++: Set encoding to "UTF-8-BOM"
- VSCode: Should detect automatically

### Claude doesn't see the tool

1. Check `config.json` syntax is valid JSON
2. Use absolute paths in config
3. Restart Claude CLI completely
4. Check Claude output for MCP server errors

## Directory Structure After Setup

```
gmail-mcp-agent-sdk/
├── gmail_mcp_server_sdk.py  # Main server
├── setup_oauth.py            # OAuth helper
├── requirements.txt          # Dependencies
├── README.md
├── SETUP_GUIDE.md           # This file
├── .gitignore
├── venv/                     # Virtual env (Python 3.10+)
├── private/                  # OAuth files (DON'T COMMIT!)
│   ├── credentials.json      # From Google Cloud
│   └── token.json            # Generated by setup_oauth.py
└── csv/                      # Output directory
    └── *.csv                 # Exported emails
```

## Next Steps

1. ✅ Install Python 3.11+
2. ✅ Recreate virtual environment
3. ✅ Install dependencies
4. ✅ Set up Google OAuth credentials
5. ✅ Run setup_oauth.py
6. ✅ Configure Claude CLI
7. ✅ Test with Claude
8. ✅ Verify CSV creation

## Support

If you encounter issues, check:
1. Python version: `python --version` (must be >=3.10)
2. MCP package installed: `pip show mcp`
3. Google credentials exist: `dir private\credentials.json`
4. Token generated: `dir private\token.json`
5. Claude config valid: Check JSON syntax in config.json

## Comparison with Manual Implementation

The SDK version (this directory) vs Manual version (`gmail-mcp-agent/`):

| Feature | Manual | SDK |
|---------|--------|-----|
| Setup complexity | High | Medium |
| Code length | ~150 lines | ~230 lines |
| Python requirement | 3.7+ | 3.10+ |
| Protocol handling | Manual | Automatic |
| Maintenance | Complex | Simple |
| Production ready | Yes | Yes |

Both work, but SDK is recommended for new projects.
