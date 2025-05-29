from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
import time

def test_login():
    driver_path = os.path.abspath("drivers/chromedriver.exe")
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)

    driver.maximize_window()
    driver.get("https://trioeats-8ebfe.web.app/")

    driver.find_element(By.XPATH, "//a[@href='/login']").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "email"))
    )

    driver.find_element(By.NAME, "email").send_keys("mahbubsarwar32@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("123456M@hbub")
    driver.find_element(By.TAG_NAME, "form").submit()

    # ✅ Wait for SweetAlert2 popup
    success_popup = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "swal2-popup"))
    )
    assert "successfully" in success_popup.text.lower()

    driver.quit()
