from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")  # بدون UI
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_login(driver):
    driver.get("https://example.com/login")
    driver.find_element(By.NAME, "username").send_keys("narges")
    driver.find_element(By.NAME, "password").send_keys("mypassword")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    assert "خوش آمدی نرگس" in driver.page_source
