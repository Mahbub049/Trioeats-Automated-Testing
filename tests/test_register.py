import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

def test_register():
    # Setup driver
    driver_path = os.path.abspath("drivers/chromedriver.exe")
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)

    driver.maximize_window()
    driver.get("https://trioeats-8ebfe.web.app/")

    # Click 'Register' button
    driver.find_element(By.XPATH, "//a[@href='/register']").click()

    # Wait for the name input field
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "name"))
    )

    # Generate unique email using timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    test_email = f"testuser{timestamp}@example.com"

    # Fill the form fields
    driver.find_element(By.NAME, "name").send_keys("QA Test User")
    driver.find_element(By.NAME, "photoURL").send_keys("https://i.ibb.co/YyRZpVG/user.png")
    driver.find_element(By.NAME, "email").send_keys(test_email)
    driver.find_element(By.NAME, "password").send_keys("Test@12345")

    # Submit the form
    driver.find_element(By.TAG_NAME, "form").submit()

    # Wait for SweetAlert2 popup
    success_popup = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "swal2-popup"))
    )
    assert "success" in success_popup.text.lower()

    driver.quit()
