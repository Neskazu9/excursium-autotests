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
