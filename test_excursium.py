def test_login_link_is_displayed(driver):
    page = ExcursionsPage(driver)
    page.driver.get("https://excursium.com/")

    assert driver.find_element(
        "xpath",
        "//*[contains(normalize-space(.), 'Войти')]"
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
