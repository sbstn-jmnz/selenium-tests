from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By

def test_page_title():
    # Configure Firefox to run in headless mode
    firefox_options = FirefoxOptions()
    firefox_options.add_argument("--headless") # This is the crucial line
    firefox_options.add_argument("--no-sandbox")
    firefox_options.add_argument("--disable-dev-shm-usage")

    # Initialize Firefox with the configured options
    browser = webdriver.Firefox(options=firefox_options)

    browser.get("https://github.com")

    titleElement = browser.find_element(By.ID, "hero-section-brand-heading")

    assert titleElement.text == "Build and ship software on a single, collaborative platform"

    browser.quit()