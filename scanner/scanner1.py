import requests
from bs4 import BeautifulSoup

# Base URL to scan
base_url = "https://93.127.173.199"
# List of common paths to check
common_paths = [
    "/",
    "/about",
    "/contact",
    "/services",
    "/login",
    "/register",
    "/api",
    "/blog",
    "/404",
    "/sitemap.xml",
    "/robots.txt",
]

def scan_paths(base_url, paths):
    valid_paths = []
    for path in paths:
        url = f"{base_url}{path}"
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(f"[+] Valid Path Found: {url} (Status Code: {response.status_code})")
                valid_paths.append(url)
            else:
                print(f"[-] Invalid Path: {url} (Status Code: {response.status_code})")
        except requests.exceptions.RequestException as e:
            print(f"[!] Error accessing {url}: {e}")
    
    return valid_paths

if __name__ == "__main__":
    valid_paths = scan_paths(base_url, common_paths)
    print("\nSummary of Valid Paths:")
    for path in valid_paths:
        print(path)
