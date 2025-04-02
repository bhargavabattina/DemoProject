import time
import pytest
import allure
from pageObjects.loginpage import LoginPage
from utilites.readProperties import ReadConfig
from config import LOGIN_DATA


@allure.epic("Orange HRM")
@allure.feature("Authentication")
class TestLoginValidation:
    """Test class for Client Validation scenarios."""

    username = LOGIN_DATA["username"]
    password = LOGIN_DATA["password"]

    @allure.story("Login Function Validations")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Correct Login Credentials Validation")
    @pytest.mark.ui
    @pytest.mark.critical
    def test_correct_login(self, page_with_screenshot):
        """Test Payer Name Field Validation"""
        login_page = LoginPage(page_with_screenshot)
        try:
            with allure.step("Filling Username"):
                login_page.fill_username(self.username)

            with allure.step("Filling Password"):
                login_page.fill_password(self.password)

            with allure.step("Clicking Login Button"):
                login_page.click_login()

            with allure.step("Verifying Dashboard "):
                expected_message = "Dashboard"
                actual_message = login_page.get_valid_message_text()

                if expected_message in actual_message:
                    print("Login successful")
                    assert True
                else:
                    pytest.fail("Login failed")  # Fails test if element is missing or text is incorrect

        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.story("Login Function Validations")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Wrong Login Credentials Validation")
    @pytest.mark.ui
    @pytest.mark.critical
    def test_wrong_login(self, page_with_screenshot):
        """Test Payer Name Field Validation"""
        login_page = LoginPage(page_with_screenshot)
        try:
            with allure.step("Filling Username"):
                login_page.fill_username(self.username)

            with allure.step("Filling Password"):
                login_page.fill_password(self.password + "wjk")

            with allure.step("Clicking Login Button"):
                login_page.click_login()

            with allure.step("Verifying error message "):
                expected_text = "Invalid credentials"

                try:
                    actual_text = login_page.get_error_message_text()
                    assert expected_text == actual_text, f"Expected '{expected_text}', but got '{actual_text}'"
                except AssertionError as e:
                    pytest.fail(f"Test failed: {str(e)}")  # Fails test if element is missing or text is incorrect

        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            raise

