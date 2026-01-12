from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

try:
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))


    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    a=driver.find_element(By.ID, "user-name")
    a.send_keys("standard_user")
    b=driver.find_element(By.ID, "password")
    b.send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    sleep(3)
    driver.find_element(By.CLASS_NAME, "inventory_item_name").click()
    sleep(3)
    driver.find_element(By.ID, "add-to-cart").click()
    sleep(3)
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    sleep(3)
    driver.find_element(By.ID, "checkout").click()
    d=driver.find_element(By.NAME, "firstName")
    d.send_keys("Muhammad")
    e=driver.find_element(By.NAME, "lastName")
    e.send_keys("Mustafa")
    f=driver.find_element(By.NAME, "postalCode")
    f.send_keys("AZ1025")
    driver.find_element(By.ID, "continue").click()
    sleep(3)
    driver.find_element(By.ID, "finish").click()
    sleep(3)
    driver.save_screenshot("screenshot_saucedemo.com.png")
    driver.find_element(By.ID, "back-to-products").click()
    sleep(15)


except Exception as e:
    print("Xəta baş verdi:", e)

finally:
    print("All the things are good")