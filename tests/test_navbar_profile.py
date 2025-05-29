import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_navbar_profile_after_login():
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

    # ✅ Wait for profile image to load
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//img[contains(@src, 'https://')]"))
    )

    # ✅ Assert the username exists somewhere (use span/div/p)
    username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Mahbub')]"))
    )
    assert "Mahbub" in username.text  # ✅ Correct indentation

    driver.quit()
