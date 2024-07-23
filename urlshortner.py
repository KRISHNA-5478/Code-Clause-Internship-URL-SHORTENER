import string
import random

class URLShortener:
    def __init__(self):
        self.url_map = {}  # To store long URL to short URL mappings
        self.short_map = {}  # To store short URL to long URL mappings
        self.base_url = "https://www.pcmag.com/encyclopedia/term/long-url"
        self.chars = string.ascii_letters + string.digits
        self.short_url_length = 6

    def _generate_short_url(self):
        return ''.join(random.choice(self.chars) for _ in range(self.short_url_length))

    def shorten(self, long_url):
        if long_url in self.url_map:
            return self.base_url + self.url_map[long_url]
        
        short_url = self._generate_short_url()
        while short_url in self.short_map:
            short_url = self._generate_short_url()
        
        self.url_map[long_url] = short_url
        self.short_map[short_url] = long_url
        
        return self.base_url + short_url

    def expand(self, short_url):
        short_key = short_url.replace(self.base_url, "")
        return self.short_map.get(short_key, None)

# Example Usage
url_shortener = URLShortener()
long_url = "https://www.pcmag.com/encyclopedia/term/long-url"
short_url = url_shortener.shorten(long_url)
print(f"Short URL: {short_url}")

expanded_url = url_shortener.expand(short_url)
print(f"Expanded URL: {expanded_url}")
