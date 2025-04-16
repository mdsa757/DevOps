from selenium import webdriver
from selenium.webdriver.common.by import By
import time
test_cases = [
    {
        "num1": "12",
        "num2": "44"
    },
    {
        "num1": "1.5",
        "num2": "9.9"
    },
    {
        "num1": "11",
        "num2": "80"
    }
]
driver = webdriver.Chrome()
driver.get("S:\\LABS\\DevOps\\DevOps\\JS_Testing\\add.html")

for test in test_cases:
    driver.refresh()

    driver.find_element(By.ID,"num1").send_keys(test["num1"])
    driver.find_element(By.ID,"num2").send_keys(test["num2"])

    driver.find_element(By.CSS_SELECTOR, "button[type='button']").click()
    time.sleep(3)
    res = driver.find_element(By.ID,"res").text
    print(res)
driver.quit()
