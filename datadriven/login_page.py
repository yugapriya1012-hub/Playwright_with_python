from playwright.sync_api import Page

class LoginPage:
    def __init__(self,page:Page):
        self.page=page
        self.username=page.locator('input[name="username"]')
        self.password=page.locator('input[name="password"]')
        self.login_btn=page.locator('button[type="submit"]')

    def open(self):
        self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def login(self,username,password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_btn.click()