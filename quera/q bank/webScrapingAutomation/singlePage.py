import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome()
chrome_options.add_experimental_option("detach", True)
driver.get('https://www.digikala.com/search/category-notebook-netbook-ultrabook/lenovo/?has_selling_stock=1')
time.sleep(10)
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f'')))
print(element.text)

time.sleep(10)
# sign_in_button = driver.find_element(by=By.LINK_TEXT, value=f"{element.text}")
# print(sign_in_button)

df = pd.DataFrame({'Link':[''], 'Name':[''], 'Subtitle':[''],'Color':[''],'Price':[''],'Sale Price':['']})

try:
    name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="__next"]/div[1]/div[2]/div[4]/div[2]/div[2]/div[2]/div[2]/div[1]/div/h1')))
    print(element.text)
    name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f'')))
    print(element.text)
    subtitle = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f'')))
    print(element.text)
    color = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f'')))
    print(element.text)
    full_price = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f'')))
    print(element.text)
    sale_price = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f'')))
    print(element.text)
    df = df.append({'Link':link, 'Name':name, 'Subtitle':subtitle,'Color':color,'Price':full_price,'Sale Price':sale_price}, ignore_index= True)
except:
    pass

df.to_csv('1_scraped_data.csv')
driver.close()
