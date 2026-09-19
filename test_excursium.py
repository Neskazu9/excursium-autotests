from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_excursium_excursions_page():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://excursium.com/")
        driver.find_element(
            "xpath",
            "//a[contains(., 'Посмотреть экскурсии')]"
        ).click()

        assert "экскурс" in driver.current_url.lower()
    finally:
        driver.quit()
