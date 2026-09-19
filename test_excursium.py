from excursions_page import ExcursionsPage


def test_excursium_excursions_page(driver):
    page = ExcursionsPage(driver)
    page.open()

    assert "/ekskursii-dlya-shkolnikov/list" in driver.current_url


def test_empty_search_page(driver):
    page = ExcursionsPage(driver)
    page.open()

    search_input = driver.find_element(
        "xpath",
        "//input[contains(@placeholder, 'Поиск')]"
    )
    search_input.clear()

    driver.find_element(
        "xpath",
        "//*[self::button or self::a][contains(normalize-space(.), 'Найти')]"
    ).click()

    assert "/ekskursii-dlya-shkolnikov/list" in driver.current_url


def test_filters_are_displayed(driver):
    page = ExcursionsPage(driver)
    page.open()

    assert driver.find_element(
        "xpath",
        "//*[contains(normalize-space(.), 'Фильтр')]"
    ).is_displayed()


def test_cost_filter_is_displayed(driver):
    page = ExcursionsPage(driver)
    page.open()

    assert driver.find_element(
        "xpath",
        "//*[contains(normalize-space(.), 'Стоимость')]"
    ).is_displayed()


def test_login_link_is_available(driver):
    driver.get("https://excursium.com/")

    assert "Вход" in driver.page_source


def test_location_filter_is_displayed(driver):
    page = ExcursionsPage(driver)
    page.open()

    assert driver.find_element(
        "xpath",
        "//*[contains(normalize-space(.), 'Место проведения')]"
    ).is_displayed()


def test_duration_filter_is_displayed(driver):
    page = ExcursionsPage(driver)
    page.open()

    assert driver.find_element(
        "xpath",
        "//*[contains(normalize-space(.), 'Продолжительность')]"
    ).is_displayed()


def test_activity_filter_is_displayed(driver):
    page = ExcursionsPage(driver)
    page.open()

    assert driver.find_element(
        "xpath",
        "//*[contains(normalize-space(.), 'Уровень активности')]"
    ).is_displayed()


def test_class_filter_is_displayed(driver):
    page = ExcursionsPage(driver)
    page.open()

    assert driver.find_element(
        "xpath",
        "//*[contains(normalize-space(.), 'Класс')]"
    ).is_displayed()


def test_popular_requests_are_displayed(driver):
    page = ExcursionsPage(driver)
    page.open()

    assert driver.find_element(
        "xpath",
        "//*[contains(normalize-space(.), 'Популярные запросы')]"
    ).is_displayed()


def test_duration_options_are_displayed(driver):
    page = ExcursionsPage(driver)
    page.open()

    assert "Полдня" in driver.page_source
    assert "Целый день" in driver.page_source


def test_location_options_are_displayed(driver):
    page = ExcursionsPage(driver)
    page.open()

    assert "Москва" in driver.page_source


def test_login_form_is_displayed(driver):
    driver.get("https://excursium.com/Client/Login")

    assert "Ваша электронная почта" in driver.page_source
    assert "Ваш пароль" in driver.page_source


def test_password_field_is_masked(driver):
    driver.get("https://excursium.com/Client/Login")

    password_field = driver.find_element(
        "xpath",
        "//input[@type='password']"
    )

    assert password_field.is_displayed()


def test_login_button_is_displayed(driver):
    driver.get("https://excursium.com/Client/Login")

    assert "Войти" in driver.page_source


def test_contacts_are_displayed(driver):
    driver.get("https://excursium.com/")

    assert "Написать в Telegram" in driver.page_source
    assert "Написать в WhatsApp" in driver.page_source


def test_search_field_is_displayed(driver):
    driver.get("https://excursium.com/")

    assert "Поиск экскурсий" in driver.page_source


def test_excursions_counter_is_displayed(driver):
    driver.get("https://excursium.com/")

    assert "Экскурсий" in driver.page_source


def test_phone_is_displayed(driver):
    driver.get("https://excursium.com/")

    assert "+7" in driver.page_source
