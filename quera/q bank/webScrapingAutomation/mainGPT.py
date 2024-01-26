import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome()
chrome_options.add_experimental_option("detach", True)
driver.get('https://www.digikala.com/search/category-notebook-netbook-ultrabook/lenovo/')
# price = driver.find_element(By.CLASS_NAME, value='ellipsis-2 text-body2-strong text-neutral-700 styles_HorizontalProductCard__productTitle__hzx5X')
time.sleep(10)
# element = driver.find_element(By.XPATH, f'//*[@id="base_layout_desktop_fixed_header"]/header/nav/div[1]/div[1]/div[2]/div[1]/a')
# print(element.text)
# element.click
sign_in_button = driver.find_element(by=By.LINK_TEXT, value="شگفت‌انگیزها"
)
sign_in_button.click()
time.sleep(10)
#driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
driver.close()
# //*[@id="ProductListPagesWrapper"]/section/div[2]/div[1]/a
# //*[@id="ProductListPagesWrapper"]/section/div[2]/div[2]/a
