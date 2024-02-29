import allure

def check_condition(condition, message):
    with allure.step(message):
        assert condition, message
