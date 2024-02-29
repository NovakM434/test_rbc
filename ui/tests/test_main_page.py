import pytest
import allure

from page.main_page import RBC_Page



class TestMainRBCPage:
    @allure.title("Проверка наличия кнопок в меню")
    @allure.description("Тест проверяет наличие кнопок 'Вход' и 'Регистрация' в меню")
    @pytest.mark.web
    def test_menu_buttons(self, browser):
        rbc_page = RBC_Page(browser)
        rbc_page.go_main_page()
        rbc_page.open_menu()
        assert rbc_page.check_login_button_exists()
        assert rbc_page.check_register_button_exists()
