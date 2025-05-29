import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_with_invalid_credentials():
    driver_path = os.path.abspath("drivers/chromedriver.exe")
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)

    driver.get("https://trioeats-8ebfe.web.app/")
    driver.find_element(By.XPATH, "//a[@href='/login']").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "email"))
    )

    # Invalid email and password
    driver.find_element(By.NAME, "email").send_keys("wronguser@example.com")
    driver.find_element(By.NAME, "password").send_keys("WrongPass123")
    driver.find_element(By.TAG_NAME, "form").submit()

    # Wait for alert (error)
    alert = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "swal2-popup"))
    )
    assert "wrong" in alert.text.lower() or "error" in alert.text.lower()

    driver.quit()
