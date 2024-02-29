import allure
from selenium.webdriver.common.by import By

from page.base_page import BasePage


class RBC_Page(BasePage):
    path = '/'

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Переход на главную страницу')
    def go_main_page(self):
        self.driver.get(self.base_url)

    @allure.step('Открытие меню')
    def open_menu(self):
        self._click(By.CSS_SELECTOR, '.topline__auth__link.js-topline-profile-link')

    @allure.step('Проверка наличия кнопки "Регистрация"')
    def check_register_button_exists(self):
        return self._find_element(By.XPATH, '//li[contains(@class, "topline__auth__profile__menu__item")]//b[text()="Регистрация"]')

    @allure.step('Проверка наличия кнопки "Вход"')
    def check_login_button_exists(self):
        return self._find_element(By.XPATH, '//li[contains(@class, "topline__auth__profile__menu__item")]//b[text()="Вход"]')
