# from playwright.sync_api import sync_playwright

# def test_browser_context():
#     with sync_playwright() as p:
#         browser=p.chromium.launch(headless=False)
#         #Opens the browser
#         context=browser.new_context()
#         #creates a new broswer session(like a new incognito window)
#         page=context.new_page()
#         #opens a new tab inside that session
#         page.goto("https://www.google.com")
#         browser.close()


# To use multiple contexts

# from playwright.sync_api import sync_playwright

# def test_multiple_context():
#     with sync_playwright() as p:
#         browser=p.chromium.launch(headless=False)

#         #user 1
#         context1=browser.new_context()
#         page1=context1.new_page()
#         page1.goto("https://www.google.com")

#         #user2
#         context2=browser.new_context()
#         page2=context2.new_page()
#         page2.goto("https://www.google.com")

#         page1.wait_for_timeout(5000)

#         browser.close()


# To create  2 different session

# from playwright.sync_api import sync_playwright

# def test_signin_signup():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)

#         context = browser.new_context()c

#         # Page 1 - Signup
#         signup_page = context.new_page()
#         signup_page.goto("https://example.com/signup")

#         # Page 2 - Signin
#         signin_page = context.new_page()
#         signin_page.goto("https://example.com/signin")