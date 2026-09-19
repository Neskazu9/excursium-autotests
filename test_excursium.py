from excursions_page import ExcursionsPage


def test_excursium_excursions_page(driver):
    page = ExcursionsPage(driver)
    page.open()

    assert "/ekskursii-dlya-shkolnikov/list" in driver.current_url
