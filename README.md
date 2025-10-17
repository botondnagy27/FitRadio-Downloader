# FitRadio Terminal Downloader

A Python-based command-line tool for downloading music tracks from FitRadio's streaming service.

## Features

- 🎵 Download FitRadio tracks with persistent authentication
- 📁 Automatic configuration management
- 📊 Real-time download progress tracking
- 🛠️ Interactive terminal interface
- 🔒 Secure credential storage
- 🚀 Easy to use and configure

## Installation

### Prerequisites
- Python 3.x
- `requests` library

1. Install required dependencies:
```bash
pip install requests
```

2. Run the script for initial setup:
```bash
python fitradio.py
```

## Quick Start

### First-Time Setup
When you run the script for the first time, you'll be prompted to enter your FitRadio credentials:

```
=== FitRadio Downloader Setup ===
Enter your Bearer Token: [your_bearer_token_here]
Enter your User ID: [your_user_id_here]
```

The configuration will be automatically saved to `fitradio_config.json`.

### How to Obtain Credentials
1. Log into [FitRadio web player](https://player.fitradio.hu/)
2. Open browser Developer Tools (F12)
3. Go to Network tab
4. Look for API requests and find the Authorization header
5. Extract the Bearer token and User ID from the requests

### Using the Downloader
Run the script and follow the interactive prompts:

```bash
python fitradio.py
```

```
==================================================
FitRadio Terminal Downloader
==================================================
Commands:
  [URL] - Download track
  config - Reconfigure settings
  quit   - Exit program
==================================================

🎵 Enter media URL: [paste_media_url_here]
Downloading: 100.0%
✓ SUCCESS: track_name.mp3
```

## Usage

### Interactive Mode Commands
- **URL**: Paste any FitRadio media URL to download the track
- **config**: Update your Bearer Token and User ID
- **quit** or **exit**: Close the application


## File Structure

```.
├── fitradio.py                 # Main downloader script
├── fitradio_config.json        # Auto-generated config file
└── downloads/                  # Default download directory
    └── track1.mp3
    └── track2.mp3
```

## Configuration

The downloader automatically creates a configuration file (`fitradio_config.json`) with your credentials:

```json
{
  "bearer_token": "example",
  "user_id": "00000"
}
```

To update your credentials, use the `config` command in interactive mode or manually edit the JSON file.

## Troubleshooting

### Common Issues

**❌ Access forbidden (HTTP 403)**
- Your Bearer Token may have expired
- Run `config` command to update credentials
- Ensure your FitRadio subscription is active

**❌ No bearer token found**
- Run the setup process again
- Check if `fitradio_config.json` exists and is valid JSON

**❌ Download fails**
- Check your internet connection
- Verify the media URL is correct and accessible
- Ensure sufficient disk space is available

### Error Messages
- `❌ FAILED: HTTP [code]` - Server returned an error
- `❌ No URL provided` - Empty input when expecting media URL
- `❌ Unexpected error` - Check Python error details for more information

## Legal Notice

⚠️ **Important**: 
- Only download content you have legal rights to access
- Respect FitRadio's terms of service
- This tool is intended for personal use with your own account
- Keep your authentication credentials secure and do not share them

## Support

For issues and questions:
1. Check that you're using Python 3.x
2. Verify your FitRadio account is active
3. Ensure your credentials are up to date
4. Check file permissions in the download directory

## License

This project is for educational and personal use. Please ensure you comply with FitRadio's terms of service and applicable copyright laws.
