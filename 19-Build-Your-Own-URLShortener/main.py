import hashlib
import json
import os

# File to store URL mappings
DATA_FILE = "url_mappings.json"

class URLShortener:
    def __init__(self):
        self.url_mapping = {}
        self.load_data()
    
    def load_data(self):
        """Load existing URL mappings from file"""
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, 'r') as f:
                    self.url_mapping = json.load(f)
                print(f"Loaded {len(self.url_mapping)} existing URL mappings.")
            except (json.JSONDecodeError, IOError):
                print("Starting with empty URL database.")
    
    def save_data(self):
        """Save URL mappings to file"""
        with open(DATA_FILE, 'w') as f:
            json.dump(self.url_mapping, f, indent=2)
    
    def generate_short_code(self, url):
        """Generate a short code for the URL using hashing
        
        Note: MD5 is used here for generating short codes in this educational project.
        MD5 should NOT be used for security purposes in production applications.
        """
        # Create a hash of the URL
        hash_object = hashlib.md5(url.encode())
        hash_hex = hash_object.hexdigest()
        # Take first 6 characters as short code
        return hash_hex[:6]
    
    def shorten_url(self, long_url):
        """Shorten a long URL"""
        # Check if URL already exists
        for short_code, stored_url in self.url_mapping.items():
            if stored_url == long_url:
                return short_code
        
        # Generate new short code
        short_code = self.generate_short_code(long_url)
        
        # Handle collisions by adding a counter
        counter = 0
        original_short_code = short_code
        while short_code in self.url_mapping:
            counter += 1
            short_code = original_short_code + str(counter)
        
        # Store the mapping
        self.url_mapping[short_code] = long_url
        self.save_data()
        return short_code
    
    def get_long_url(self, short_code):
        """Retrieve the original URL from short code"""
        return self.url_mapping.get(short_code, None)
    
    def list_all_urls(self):
        """List all shortened URLs"""
        if not self.url_mapping:
            print("No URLs stored yet.")
            return
        
        print("\n=== All Shortened URLs ===")
        for short_code, long_url in self.url_mapping.items():
            print(f"Short: {short_code} -> {long_url}")
        print()

def main():
    print("=" * 50)
    print("Welcome to Build Your Own URL Shortener!")
    print("=" * 50)
    
    shortener = URLShortener()
    
    while True:
        print("\nChoose an option:")
        print("1. Shorten a URL")
        print("2. Expand a short code")
        print("3. List all URLs")
        print("4. Exit")
        
        choice = input("\nYour choice: ").strip()
        
        if choice == "1":
            long_url = input("Enter the URL to shorten: ").strip()
            if long_url:
                short_code = shortener.shorten_url(long_url)
                print(f"\n✓ Short code created: {short_code}")
                print(f"  Original URL: {long_url}")
            else:
                print("Please enter a valid URL.")
        
        elif choice == "2":
            short_code = input("Enter the short code: ").strip()
            long_url = shortener.get_long_url(short_code)
            if long_url:
                print(f"\n✓ Original URL: {long_url}")
            else:
                print(f"\n✗ Short code '{short_code}' not found.")
        
        elif choice == "3":
            shortener.list_all_urls()
        
        elif choice == "4":
            print("\nThank you for using the URL Shortener!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
