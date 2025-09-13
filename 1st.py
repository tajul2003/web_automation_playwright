from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    # Browser launch
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Open Playwright Python page
    page.goto("https://playwright.dev/python/", wait_until="networkidle", timeout=60000)
    print("Webpage opened successfully")

    # Click on "Docs" link
    button = page.get_by_role('link', name="GET STARTED")
    button.click()
    print("Button clicked")
    
    #get url
    print("link :", page.url)

    # Wait 10 seconds before closing
    page.wait_for_timeout(10000) 
    print("Closing browser...")
    
    
    
    browser.close()
