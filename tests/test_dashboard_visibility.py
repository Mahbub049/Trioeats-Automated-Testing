import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_dashboard_visibility_after_login():
    driver_path = os.path.abspath("drivers/chromedriver.exe")
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)

    driver.get("https://trioeats-8ebfe.web.app/login")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "email"))
    )

    driver.find_element(By.NAME, "email").send_keys("mahbubsarwar32@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("123456M@hbub")
    driver.find_element(By.TAG_NAME, "form").submit()

    # ✅ Wait for SweetAlert2 popup and click OK
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "swal2-popup"))
    )
    driver.find_element(By.CLASS_NAME, "swal2-confirm").click()

    # ✅ Wait for "Log Out" button to become visible
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Log Out')]"))
    )

    # ✅ Confirm dashboard UI elements
    assert "Log Out" in driver.page_source
    assert "Explore All Foods" in driver.page_source

    driver.quit()
