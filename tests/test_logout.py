import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_logout_functionality():
    # Setup Chrome WebDriver
    driver_path = os.path.abspath("drivers/chromedriver.exe")
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)

    # Step 1: Open login page
    driver.get("https://trioeats-8ebfe.web.app/login")

    # Step 2: Login with valid credentials
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email")))
    driver.find_element(By.NAME, "email").send_keys("mahbubsarwar32@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("123456M@hbub")
    driver.find_element(By.TAG_NAME, "form").submit()

    # Step 3: Wait until the "Log Out" button is clickable
    logout_button_locator = (By.XPATH, "//button[contains(text(), 'Log Out')]")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(logout_button_locator))
    logout_button = driver.find_element(*logout_button_locator)
    logout_button.click()

    # Step 4: Verify successful logout
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Register')]"))
    )
    assert "Register" in driver.page_source
    assert "Log Out" not in driver.page_source

    driver.quit()
