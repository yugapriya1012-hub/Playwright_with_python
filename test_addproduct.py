from playwright.sync_api import sync_playwright, expect

def test_add_product():
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://yugapriya1012-hub.github.io/Fullstack_Frontend/page/seller/add_product.html")

        # Fill form
        page.locator("input[placeholder='Your brand name']").fill("Priya")

        page.locator("input[placeholder='e.g. Chocolate Cake']").fill("Cookies")

        page.locator("textarea").fill("Fresh homemade cookies baked to perfection.")

        page.locator("input[type='number']").nth(0).fill("450")
        page.locator("input[type='number']").nth(1).fill("0")

        page.locator("input[placeholder='e.g. Chennai, Madurai']").fill("Taramani")

        # Upload image
        page.locator("input[type='file']").set_input_files(r"C:\Users\YugapriyaVijayakumar\Downloads\cookies.jpg")

        # Submit
        page.locator(".submit-btn").click()

        page.wait_for_timeout(3000)

        print("Current URL:", page.url)

        # Wait for success page
        expect(page).to_have_url("https://yugapriya1012-hub.github.io/Fullstack_Frontend/page/seller/productsucc.html")

        expect(page.get_by_text("Product Added Successfully!")).to_be_visible()

        expect(page.get_by_text("Your product is now listed in My Products.")).to_be_visible()

        back_btn = page.get_by_role("link", name="Back to Products")

        expect(back_btn).to_be_visible()

        back_btn.click()

        expect(page).to_have_url("https://yugapriya1012-hub.github.io/Fullstack_Frontend/page/seller/add_product.html")