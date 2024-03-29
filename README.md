# Проект

## Описание

Этот проект содержит две версии: UI версию и API версию.

### UI версия

В UI версии используются следующие инструменты и библиотеки:

- **Пайтест**: для написания и запуска тестов.
- **Селениум**: для автоматизации браузерных тестов.
- **Аллюр**: для создания отчетов о результатах тестов.

Версии библиотек:

- **pytest**: 8.0.1
- **selenium**: 4.17.2
- **allure-pytest**: 2.13.2

Тесты в UI версии можно запускать по меткам, что позволяет запускать определенные наборы тестов. Аллюр используется для создания отчетов о результатах тестов.

### API версия

В API версии используются следующие инструменты и библиотеки:

- **Пайтест**: для написания и запуска тестов.
- **Аллюр**: для создания отчетов о результатах тестов.

Версии библиотек:

- **pytest**: 8.0.1
- **allure-pytest**: 2.13.2

Тесты в API версии можно запускать по меткам, что позволяет запускать определенные наборы тестов. Аллюр используется для создания отчетов о результатах тестов.

## Запуск тестов

Для запуска тестов используйте следующие команды:

UI версия:
```bash
pytest --alluredir=allure-results
```

API версия:
```bash
pytest --alluredir=allure-results
```

Для запуска тестов по меткам, добавьте параметр `-m` и название метки:
```bash
pytest -m <метка> --alluredir=allure-results
```

Для генерации отчета по результатам тестов используйте следующую команду:
```bash
allure serve allure-results
```

## Отчеты

Отчеты о результатах тестов создаются с помощью Аллюр и доступны по ссылке, которая открывается после выполнения команды `allure serve allure-results`.
