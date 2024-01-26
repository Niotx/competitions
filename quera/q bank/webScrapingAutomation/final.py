import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome()
chrome_options.add_experimental_option("detach", True)
driver.get('https://www.digikala.com/search/category-notebook-netbook-ultrabook/lenovo/?has_selling_stock=1')

i = 1
pattern = r'(\d+)'

while True:
    
    num = str(i)
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="ProductListPagesWrapper"]/section/div[2]/div[{num}]/a/div/article/div[2]/div[2]/div[2]/h3')))
    print(element.text)
    href = driver.find_element(By.XPATH, f'//*[@id="ProductListPagesWrapper"]/section/div[2]/div[{num}]/a').get_attribute('href')
    print(href)
    match = re.search(pattern, href)
    matchf = match.group(1)
    print(matchf)
    # time.sleep(50)
    # sign_in_button = driver.find_element(by=By.LINK_TEXT, value=f"{element.text}")
    # print(sign_in_button)
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')

    time.sleep(2)
    # new_hight = driver.execute_script('return document.body.scrollHeight')
    # print(new_hight)
    # if(new_hight == last_height):
    #     break
    # last_height = new_hight
    print(num)
    i += 1

driver.close()

# <h3 class="ellipsis-2 text-body2-strong text-neutral-700 styles_HorizontalProductCard__productTitle__hzx5X">لپ تاپ 15.6 اینچی لنوو مدل IdeaPad 3 15ITL6-i3 12GB 1HDD 256SSD - کاستوم شده</h3>
# //*[@id="ProductListPagesWrapper"]/section/div[2]/div[2]/a
# //*[@id="ProductListPagesWrapper"]/section/div[2]/div[1]/a
# //*[@id="ProductListPagesWrapper"]/section/div[2]/div[1]/a/div/article/div[2]/div[2]/div[2]/h3
# //*[@id="ProductListPagesWrapper"]/section/div[2]/div[2]/a/div/article/div[2]/div[2]/div[2]/h3
# last_height = 6634 #driver.execute_script('return document.body.scrollHeight')
# print(last_height)
# price = driver.find_element(By.CLASS_NAME, value='ellipsis-2 text-body2-strong text-neutral-700 styles_HorizontalProductCard__productTitle__hzx5X')
# element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="modal-root"]/div[8]/div/div/div/div/div[2]/div/div/div/div[17]/p')))
# print(element.text)

# time.sleep(10)
# sign_in_button = driver.find_element(by=By.LINK_TEXT, value=f"{element.text}"
# )
# sign_in_button.click()
# time.sleep(10)
# link_t = []
