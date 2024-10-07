import json
import os
import random
import requests
from bs4 import BeautifulSoup
from colorama import init, Fore

# Initialize Colorama
init(autoreset=True)

# Function to fetch and crawl URLs
def crawl_urls(urls):
    collected_urls = set()
    
    for url in urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                # Parse the page content
                soup = BeautifulSoup(response.content, 'html.parser')
                # Find all anchor tags and extract their href attributes
                for link in soup.find_all('a', href=True):
                    full_url = link['href']
                    # Make sure the URL is absolute
                    if full_url.startswith('http'):
                        collected_urls.add(full_url)
                        # Print the mapping with colored output
                        print(f"{Fore.GREEN}{url} --> {Fore.YELLOW}{full_url}")
            else:
                print(f"{Fore.RED}Failed to retrieve {url}: Status Code {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"{Fore.RED}Error fetching {url}: {e}")
    
    return list(collected_urls)

# Function to read JSON file and return list of URLs
def read_urls_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data['urls']

# Function to write collected URLs to a new JSON file
def write_urls_to_json(urls):
    random_number = random.randint(1000, 9999)
    output_file = f"../data/{random_number}.json"
    
    with open(output_file, 'w') as file:
        json.dump({"urls": urls}, file, indent=4)
    
    print(f"{Fore.CYAN}Collected URLs saved to {output_file}")

# Main function
def main():
    input_file = '../data/pathss.json'
    
    # Read URLs from JSON file
    urls = read_urls_from_json(input_file)
    
    # Crawl URLs to collect more URLs
    collected_urls = crawl_urls(urls)
    
    # Write collected URLs to a new JSON file
    write_urls_to_json(collected_urls)

if __name__ == "__main__":
    # Ensure the data directory exists
    if not os.path.exists('data'):
        os.makedirs('data')
    
    main()
