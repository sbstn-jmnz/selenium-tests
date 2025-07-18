from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

def test_page_title():
  options = Options()
  options.headless = True

  browser = webdriver.Chrome(options=options)
  
  browser.get('https://github.com')

  titleElement = browser.find_element(By.ID,'hero-section-brand-heading')

  assert titleElement.text == 'Build and ship software on a single, collaborative platform'

  browser.quit()