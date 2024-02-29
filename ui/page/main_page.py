from page.base_page import BasePage
from selenium.webdriver.common.by import By


class RBC_Page(BasePage):
    path = '/'

    def __init__(self, driver):
        super().__init__(driver)

    def go_main_page(self):
        self.driver.get(self.base_url)

    def open_menu(self):
        self._click(By.CSS_SELECTOR, '.topline__auth__link.js-topline-profile-link')

    def check_register_button_exists(self):
        return self._find_element(By.XPATH, '//li[contains(@class, "topline__auth__profile__menu__item")]//b[text()="Регистрация"]')

    def check_login_button_exists(self):
        return self._find_element(By.XPATH, '//li[contains(@class, "topline__auth__profile__menu__item")]//b[text()="Вход"]')
