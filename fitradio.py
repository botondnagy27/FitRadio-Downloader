import requests
import os
import json

class FitRadioTerminalDownloader:
    def __init__(self, config_file="fitradio_config.json"):
        self.config_file = config_file
        self.session = requests.Session()
        self.load_config()
        
    def load_config(self):
        """Load or create configuration with bearer token"""
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                config = json.load(f)
                self.bearer_token = config.get('bearer_token')
                self.user_id = config.get('user_id')  # No default value
                if self.bearer_token:
                    print("✓ Loaded configuration")
                else:
                    print("❌ No bearer token found in config")
                    self.setup_config()
        else:
            self.setup_config()
    
    def setup_config(self):
        """First-time setup for bearer token and user ID"""
        print("\n=== FitRadio Downloader Setup ===")
        self.bearer_token = input("Enter your Bearer Token: ").strip()
        self.user_id = input("Enter your User ID: ").strip()
        
        if not self.bearer_token or not self.user_id:
            print("❌ Both Bearer Token and User ID are required!")
            return self.setup_config()
        
        config = {
            'bearer_token': self.bearer_token,
            'user_id': self.user_id
        }
        
        with open(self.config_file, 'w') as f:
            json.dump(config, f)
        print("✓ Configuration saved to fitradio_config.json")
    
    def download_track(self, media_url, output_dir="downloads"):
        """Download track with persistent authentication"""
        if not media_url:
            print("❌ No URL provided")
            return False
            
        if not hasattr(self, 'bearer_token') or not self.bearer_token:
            print("❌ No bearer token configured. Run setup first.")
            return False
            
        headers = {
            'Authorization': f'Bearer {self.bearer_token}',
            'Referer': 'https://player.fitradio.hu/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Origin': 'https://player.fitradio.hu',
            'Range': 'bytes=0-'
        }
        
        try:
            response = self.session.get(media_url, headers=headers, stream=True)
            
            if response.status_code in [200, 206]:
                os.makedirs(output_dir, exist_ok=True)
                filename = media_url.split('/')[-1].split('?')[0]
                filename = requests.utils.unquote(filename)
                filepath = os.path.join(output_dir, filename)
                
                total_size = int(response.headers.get('content-length', 0))
                downloaded_size = 0
                
                with open(filepath, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                            downloaded_size += len(chunk)
                            if total_size > 0:
                                percent = (downloaded_size / total_size) * 100
                                print(f"\rDownloading: {percent:.1f}%", end='', flush=True)
                
                print(f"\n✓ SUCCESS: {filename}")
                return True
            else:
                print(f"❌ FAILED: HTTP {response.status_code}")
                if response.status_code == 403:
                    print("   Access forbidden - check your Bearer Token and User ID")
                return False
                
        except Exception as e:
            print(f"❌ ERROR: {str(e)}")
            return False
    
    def interactive_mode(self):
        """Start interactive terminal session"""
        print("\n" + "="*50)
        print("FitRadio Terminal Downloader")
        print("="*50)
        print("Commands:")
        print("  [URL] - Download track")
        print("  config - Reconfigure settings")
        print("  quit   - Exit program")
        print("="*50)
        
        while True:
            try:
                user_input = input("\n🎵 Enter media URL: ").strip()
                
                if user_input.lower() in ['quit', 'exit', 'q']:
                    print("Goodbye!")
                    break
                elif user_input.lower() == 'config':
                    self.setup_config()
                    continue
                elif user_input.startswith('http'):
                    self.download_track(user_input)
                elif user_input:
                    print("❌ Invalid input. Enter a URL or 'quit' to exit.")
                    
            except KeyboardInterrupt:
                print("\n\nInterrupted. Goodbye!")
                break
            except Exception as e:
                print(f"❌ Unexpected error: {str(e)}")

# USAGE
if __name__ == "__main__":
    downloader = FitRadioTerminalDownloader()
    downloader.interactive_mode()