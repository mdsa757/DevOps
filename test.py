from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# change the key values based on your registeration form input selectors
test_cases = [
    {
        "full": "User MissingPhone",
        "userName": "usernopho",
        "email": "nopho@example.com",
        "phn": "",
        "psw": "password123",
        "cpsw": "password123",
        "gender": "dt1"
    },
    {
        "full": "User ShortPass",
        "userName": "shortpassuser",
        "email": "shortpass@example.com",
        "phn": "9999999992",
        "psw": "123",
        "cpsw": "123",
        "gender": "dt2"
    },
    {
        "full": "Mismatch User",
        "userName": "mismatchuser",
        "email": "mismatch@example.com",
        "phn": "9999999993",
        "psw": "password123",
        "cpsw": "different123",
        "gender": "dt3"
    },
    {
        "full": "Success User",
        "userName": "successuser",
        "email": "success@example.com",
        "phn": "9999999994",
        "psw": "validpass123",
        "cpsw": "validpass123",
        "gender": "dt1"
    }
]

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5000/") # change it based on the URL you are getting

for test in test_cases:

    driver.refresh()
    time.sleep(1) #wait for 1 sec

    driver.find_element(By.ID, "full").send_keys(test["full"])
    driver.find_element(By.ID, "userName").send_keys(test["userName"])
    driver.find_element(By.ID, "email").send_keys(test["email"])
    driver.find_element(By.ID, "phn").send_keys(test["phn"])
    driver.find_element(By.ID, "psw").send_keys(test["psw"])
    driver.find_element(By.ID, "cpsw").send_keys(test["cpsw"])
    driver.find_element(By.CSS_SELECTOR, f"label[for='{test['gender']}']").click()


    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # **Wait for the alert and accept it**
    time.sleep(1)  # Give time for alert to appear (Better: Use explicit waits)
    try:
        WebDriverWait(driver, 1).until(EC.alert_is_present())
        alert = Alert(driver)
        print("Alert Text:", alert.text)  # Prints alert message
        alert.accept()  # Click OK on the alert
    except:
        print("No alert appeared.")

    # **Now check for the message**
    msg = driver.find_element(By.ID, "msg").text
    print("Message:", msg)

driver.quit()