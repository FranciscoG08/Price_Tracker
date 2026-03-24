from playwright.sync_api import sync_playwright
from scraper import *

# Headers realistas para evitar bloqueios iniciais
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"
}

def cleaned_link(url):
    return url.split("/")[2].split(".")[1]

def get_product_data(url, clean_link):
    try:
        with sync_playwright() as pw:

            browser = pw.chromium.launch(
                headless=True,
                channel="chrome", #importante para site Adidas
                args=["--disable-blink-features=AutomationControlled"]
            )

            context = browser.new_context(
                viewport={'width': 1280, 'height': 800},
                    user_agent=HEADERS["User-Agent"]
                )
            
            page = context.new_page()

            page.goto(url, wait_until="domcontentloaded", timeout=60000)

            if clean_link == 'worten':
                return worten(page)
            elif clean_link == 'adidas':
                return adidas(page)
            elif clean_link == 'puma':
                return puma(page)
            elif clean_link == 'ikea':
                return ikea(page)
            elif clean_link == 'nike':
                return nike(page)
            elif clean_link == 'pcdiga':
                return pcdiga(page)
            elif clean_link == 'amazon':
                return amazon(page)
            elif clean_link == 'samsung':
                return samsung(page)
            elif clean_link == 'sprintersports':
                return sportZone(page)
            elif clean_link == 'radiopopular':
                return radioPopular(page)
            else:
                print("E")
            
    except Exception as e:
        print(f"Falha total no Playwright para {url}: {e}")
        return None
