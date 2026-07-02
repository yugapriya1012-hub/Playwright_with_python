# from playwright.sync_api import expect
# class TestLogin:

#     def test_valid_login(self,login_page):
#         login_page.fill('input[name="username"]',"Admin")
#         login_page.fill('input[name="password"]',"admin123")
#         login_page.click('button[type="submit"]')

#         assert login_page.url=="https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

#     def test_invalid_login(self,login_page):
#         login_page.fill('input[name="username"]',"Admin")
#         login_page.fill('input[name="password"]',"wrong123")
#         login_page.click('button[type="submit"]')

#         expect(login_page.locator("//p[text()='Invalid credentials']")).to_be_visible()

#     def test_empty_login(self,login_page):
#         login_page.click('button[type="Submit"]')

#         expect(login_page.locator("//span[text()='Required']").first).to_be_visible()