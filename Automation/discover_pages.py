import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def get_internal_links(base_url):
    try:
        response = requests.get(base_url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        internal_links = set()
        base_netloc = urlparse(base_url).netloc

        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            full_url = urljoin(base_url, href)
            parsed_url = urlparse(full_url)

            if parsed_url.netloc == base_netloc:
                # Remove fragment identifiers and query parameters for cleaner unique page list
                clean_url = full_url.split('#')[0].split('?')[0]
                if clean_url.rstrip('/') != base_url.rstrip('/'): # Exclude self-link
                    internal_links.add(clean_url)
        
        return internal_links
    except Exception as e:
        print(f"Error fetching {base_url}: {e}")
        return set()

def check_sitemap(base_url):
    sitemap_url = urljoin(base_url, '/sitemap.xml')
    try:
        response = requests.get(sitemap_url, timeout=5)
        if response.status_code == 200:
            print(f"Sitemap found at: {sitemap_url}")
            # Simple line count or regex could extract locs if needed
            print(f"Sitemap content preview: {response.text[:200]}")
        else:
            print(f"No sitemap found at {sitemap_url} (Status: {response.status_code})")
    except Exception as e:
        print(f"Error checking sitemap: {e}")

if __name__ == "__main__":
    target_url = "https://karsaazagent.com"
    print(f"Scanning {target_url} for pages...")
    
    links = get_internal_links(target_url)
    
    print("\n--- Discovered Internal Pages ---")
    for link in sorted(links):
        print(link)
    
    print(f"\nTotal unique internal pages linked from homepage: {len(links)}")
    
    print("\n--- Checking for Sitemap ---")
    check_sitemap(target_url)
