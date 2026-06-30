# from playwright.sync_api import Page

# def test_signup_and_signin(page: Page):

#     # Open site
#     page.goto(
#         "https://yugapriya1012-hub.github.io/Fullstack_Frontend/index.html"
#     )

#     # Go to signup page
#     page.click("#signupBtn")
#     page.wait_for_url("**/page/signup.html")

#     # Fill signup form
#     page.fill("#fullName", "Desh")

#     # Use a new email every time
#     page.fill("#email", "d12345@gmail.com")

#     page.fill("#phoneNumber", "6380495230")
#     page.fill("#password", "D@123")
#     page.fill("#confirmPassword", "D@123")

#     # Capture signup alert
#     def signup_dialog(dialog):
#         print("Signup Alert:", dialog.message)
#         dialog.accept()

#     page.once("dialog", signup_dialog)

#     page.click("#submitBtn")

#     # Wait a few seconds
#     page.wait_for_timeout(5000)

#     print("After Signup URL:", page.url)

#     # Continue only if redirected
#     if "signin.html" not in page.url:
#         raise AssertionError(
#             f"Signup redirect failed. Current URL: {page.url}"
#         )

#     # Signin
#     page.fill("#email", "d12345@gmail.com")
#     page.fill("#password", "D@123")

#     page.click("#submitBtn")

#     # signin.js uses setTimeout(1500)
#     page.wait_for_timeout(4000)

#     print("Final URL:", page.url)

#     assert "home.html" in page.url
