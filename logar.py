from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time
import getpass

username = input("Enter UserName:")
password = getpass.getpass("Enter password:")


wd  = webdriver.Chrome()
wd.get('https://www.instagram.com')
time.sleep(1)

#Conecte-se
def login():
    global username, password

    wd.find_element(By.NAME, 'username').send_keys(username)
    time.sleep(1)
    wd.find_element(By.NAME, 'password').send_keys(password)
    time.sleep(1)
    wd.find_element(By.CLASS_NAME, 'L3NKy   ').click()
    time.sleep(random.randint(3, 4))
    try:
        error_msg = wd.find_element(By.XPATH, '//*[@id="slfErrorAlert"]').text
        print(error_msg)
        time.sleep(15)
        quit()
    except:
        return

        