from playwright.sync_api import sync_playwright

def test_googlescreenshot():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        page=browser.new_page()


        page.goto("https://www.google.com")
        assert page.url=="https://www.google.com/"

        page.screenshot(path="google_homepage.png",full_page=True)

        print("Screenshot saved successfully!")

        browser.close()

