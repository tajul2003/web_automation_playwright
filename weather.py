import sys
sys.stdout.reconfigure(encoding='utf-8')

from playwright.sync_api import sync_playwright

def get_weather(city="bangladesh/dhaka"):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=100)
        page = browser.new_page()

        # Open weather page (use load instead of networkidle)
        url = f"https://www.timeanddate.com/weather/{city}"
        page.goto(url, wait_until="domcontentloaded", timeout=60000)

        # Wait for temperature element
        page.wait_for_selector("div.h2", timeout=60000)

        # Get temperature text
        temperature = page.inner_text("div.h2")
        print(f"Current temperature in {city}: {temperature}")

        browser.close()

# Example usage
get_weather("bangladesh/dhaka")
