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


def test_show_more_filter_values(driver):
    page = ExcursionsPage(driver)
    page.open()

    more_link = driver.find_element(
        "xpath",
        "//*[contains(normalize-space(.), 'ещё')]"
    )

    assert more_link.is_displayed()

def test_cost_filter_options_are_displayed(driver):
    page = ExcursionsPage(driver)
    page.open()

    assert driver.find_element(
        "xpath",
        "//*[contains(normalize-space(.), '1000₽ - 1500₽')]"
    ).is_displayed()

    assert driver.find_element(
        "xpath",
        "//*[contains(normalize-space(.), '1500₽ - 2500₽')]"
    ).is_displayed()

def test_telegram_contact_is_displayed(driver):
    page = ExcursionsPage(driver)
    page.open()

    assert driver.find_element(
        "xpath",
        "//*[contains(normalize-space(.), 'Написать в Telegram')]"
    ).is_displayed()
