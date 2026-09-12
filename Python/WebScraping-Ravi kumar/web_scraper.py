import os
import re
import sys
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
PRODUCT_URLS = [
    "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html",
    "https://books.toscrape.com/catalogue/soumission_998/index.html",
    "https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html",
]
TARGET_PRICE = 30.00
IMAGE_DIR = "downloaded_images"
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    )
}
def fetch_webpage(url: str) -> BeautifulSoup:
    response = requests.get(url, headers=HEADERS, timeout=15)
    response.raise_for_status()  # raises an error for bad status codes
    return BeautifulSoup(response.text, "html.parser")

def extract_product_details(soup: BeautifulSoup, page_url: str) -> dict:
    title_tag = soup.find("h1")
    title = title_tag.get_text(strip=True) if title_tag else "Title not found"

    #Price
    price_tag = soup.find("p", class_="price_color")
    price_text = price_tag.get_text(strip=True) if price_tag else ""
    # Strip currency symbols / stray characters, keep digits and dot
    price_match = re.search(r"[\d,]+\.\d+", price_text)
    price = float(price_match.group().replace(",", "")) if price_match else None

    #Image URL
    image_tag = soup.find("div", id="product_gallery")
    image_url = None
    if image_tag:
        img = image_tag.find("img")
        if img and img.get("src"):
            image_url = urljoin(page_url, img["src"])

    return {
        "title": title,
        "price": price,
        "price_text": price_text,
        "image_url": image_url,
        "page_url": page_url,
    }
def download_image(image_url: str, title: str, save_dir: str) -> str:
    if not image_url:
        return "No image URL available, skipped download."
    os.makedirs(save_dir, exist_ok=True)
    safe_name = re.sub(r"[^A-Za-z0-9_-]+", "_", title.strip())[:50] or "product"
    extension = os.path.splitext(image_url)[1] or ".jpg"
    file_path = os.path.join(save_dir, f"{safe_name}{extension}")

    try:
        response = requests.get(image_url, headers=HEADERS, timeout=15)
        response.raise_for_status()
        with open(file_path, "wb") as f:
            f.write(response.content)
        return file_path
    except requests.RequestException as exc:
        return f"Failed to download image: {exc}"


def compare_price(price: float, target_price: float) -> str:
    if price is None:
        return "Price unavailable, cannot compare."
    if price < target_price:
        return f"Price (${price:.2f}) is BELOW target (${target_price:.2f}) -> Good deal!"
    elif price > target_price:
        return f"Price (${price:.2f}) is ABOVE target (${target_price:.2f}) -> Too expensive."
    else:
        return f"Price (${price:.2f}) EQUALS target (${target_price:.2f})."


def process_product_url(url: str, target_price: float) -> None:
    print("=" * 70)
    print(f"Processing: {url}")
    try:
        soup = fetch_webpage(url)
    except requests.RequestException as exc:
        print(f"  [ERROR] Could not fetch page: {exc}")
        return

    details = extract_product_details(soup, url)

    print(f"  Title      : {details['title']}")
    print(f"  Price      : {details['price_text']}")
    print(f"  Image URL  : {details['image_url']}")

    saved_path = download_image(details["image_url"], details["title"], IMAGE_DIR)
    print(f"  Image saved: {saved_path}")

    comparison = compare_price(details["price"], target_price)
    print(f"  Comparison : {comparison}")

def main():
    print("Starting Web Scraping Assignment")
    print(f"Target price for comparison: ${TARGET_PRICE:.2f}")

    for url in PRODUCT_URLS:
        process_product_url(url, TARGET_PRICE)

    print("=" * 70)
    print("Scraping complete for all product URLs.")


if __name__ == "__main__":
    main()
