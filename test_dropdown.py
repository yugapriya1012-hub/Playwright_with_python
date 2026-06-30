# from playwright.sync_api import sync_playwright

# def test_dropdown():
#     with sync_playwright() as p:
#         browser=p.chromium.launch(headless=False)
#         page=browser.new_page()

#         page.goto("https://the-internet.herokuapp.com/dropdown")
 
#         # select option 1
#         page.select_option("#dropdown",label="Option 2")

#         # wait for 3 seconds to see the selection

#         page.wait_for_timeout(3000)

#         browser.close()
