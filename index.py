from ast import Bytes
import time
import random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from faker import Faker


url = "https://develop.hqzen.com/signup/hqzen"
# Create an instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the sign up page
driver.get(url)

# Create an instance of Faker
fake = Faker()

# Generate a first name, last name and email combination
# Generate a random name
first_name = fake.first_name()
last_name = fake.last_name()
password = "123456"
email = first_name + "@example.com"


# Wait for page to load
time.sleep(10)

# Fill out the sign up form

driver.find_element(By.ID, "form-field-0").send_keys(first_name)
driver.find_element(By.ID, "form-field-1").send_keys(last_name)
driver.find_element(By.ID, "form-field-2").send_keys(email)
driver.find_element(By.ID, "form-field-3").send_keys(password)
driver.find_element(
    By.XPATH, "/html/body/div/div/div[1]/div/div[1]/form/div[4]/button").click()

# Wait for the verification code prompt
time.sleep(5)

# Bypass the verification code
driver.find_element(By.XPATH, '//*[@id="form-field-4"]').send_keys('123456')
driver.find_element(
    By.XPATH, '/html/body/div/div/div[1]/div/div[1]/form/button').click()


time.sleep(5)
# Skip upload Resume
driver.find_element(
    By.XPATH, '/html/body/div/div/div[1]/div/div[1]/div[2]/form/button[2]').click()

# Wait for page to load
time.sleep(5)
driver.find_element(
    By.XPATH, '/html/body/div/div/div[1]/div/div[1]/div[2]/button').click()

time.sleep(5)
# Print successful user was redirected to the Job Portal page
print("Successfully signed up and redirected to the Job Portal page!")
# Close the browser
driver.close()
