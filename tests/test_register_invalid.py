import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_register_with_invalid_data():
    driver_path = os.path.abspath("drivers/chromedriver.exe")
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)

    # 🟢 Go directly to register page
    driver.get("https://trioeats-8ebfe.web.app/register")

    # Wait for form to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "name"))
    )

    # Fill invalid data
    driver.find_element(By.NAME, "name").send_keys("")  # Empty
    driver.find_element(By.NAME, "photoURL").send_keys("not-a-url")
    driver.find_element(By.NAME, "email").send_keys("invalid-email")
    driver.find_element(By.NAME, "password").send_keys("123")

    driver.find_element(By.TAG_NAME, "form").submit()

    # Wait and assert error appears
    alert = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "swal2-popup"))
    )
    assert "error" in alert.text.lower()

    driver.quit()
