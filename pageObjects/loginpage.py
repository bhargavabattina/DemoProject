from playwright.sync_api import Page


class LoginPage:

    #CSS Selectors
    username_css_selector = "input[placeholder='username']"
    password_css_selector = "input[placeholder='password']"
    login_button_css_selector = "button[type='submit']"

    #XPATH Selectors
    # username_xpath_selector = "//input[@placeholder='Username']"
    # password_xpath_selector = "//input[@placeholder='Password']"
    # login_button_xpath_selector = "//button[@type='submit']"
    dashboard_text_Xpath_selector = "//h6[normalize-space()='Dashboard']"
    error_message_Xpath_selector = "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']"



    def __init__(self, page: Page):
        self.page = page

    @property
    def username_input(self):
        return self.page.locator(self.username_css_selector)

    def fill_username(self, username: str):
        self.username_input.fill(username)

    @property
    def password_input(self):
        return self.page.locator(self.password_css_selector)

    def fill_password(self, password: str):
        self.password_input.fill(password)

    @property
    def login_button(self):
        return self.page.locator(self.login_button_css_selector)

    def click_login(self):
        self.login_button.click()


    @property
    def valid_message(self):
        return self.page.locator(self.dashboard_text_Xpath_selector)

    def get_valid_message_text(self):
        return self.valid_message.text_content()


    @property
    def error_message(self):
        return self.page.locator(self.error_message_Xpath_selector)

    def get_error_message_text(self):
        return self.error_message.text_content()



