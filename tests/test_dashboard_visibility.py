import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_dashboard_visibility_after_login():
    driver_path = os.path.abspath("drivers/chromedriver.exe")
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)

    # ✅ Step 1: Open login page
    driver.get("https://trioeats-8ebfe.web.app/login")

    # ✅ Step 2: Wait for login form to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "email"))
    )

    # ✅ Step 3: Fill valid login details
    driver.find_element(By.NAME, "email").send_keys("mahbubsarwar32@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("123456M@hbub")
    driver.find_element(By.TAG_NAME, "form").submit()

    # ✅ Step 4: Wait for dashboard/homepage to load after login
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    # ✅ Step 5: Assert dashboard indicators
    assert (
        "Logout" in driver.page_source or 
        "Welcome" in driver.page_source or 
        "Profile" in driver.page_source
    )

    driver.quit()
