# import requests
# from bs4 import BeautifulSoup
#
# URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
#
# # Write your code below this line 👇
#
# response = requests.get(URL)
# website_html = response.text
#
# soup = BeautifulSoup(website_html, "html.parser")
#
# all_movies = soup.find_all(name="h3", class_="title")
#
# movie_titles = [movie.getText() for movie in all_movies]
# movies = movie_titles[::-1]
#
# with open("movies.txt", mode="w") as file:
#     for movie in movies:
#         file.write(f"{movie}\n")
#
#
# '''
# FAQ: Empire's website has changed!
#
# When this lesson was created, I used this URL for the project:
# URL = "https://www.empireonline.com/movies/features/best-movies-2/"
#
# However, Empire has since changed their website. You can see this when you inspect the movie title elements.
# You'll see that the h3 with the class "title" is no longer there.
# To use exactly the same code as per the solution, we can use a cached version of the website from the Internet Archive's Wayback Machine.
#
# '''
#
#
#
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from bs4 import BeautifulSoup
# import pandas as pd
# import time
#
# driver = webdriver.Firefox()
# driver.get('https://www.indeed.com/')
#
# input_job_name = driver.find_element_by_xpath('//*[@id="text-input-what"]')
# input_job_name.send_keys('data analyst')
#
# input_location = driver.find_element_by_xpath('//*[@id="text-input-where"]')
# input_location.send_keys('New York, NY')
# time.sleep(5)
# find_job = driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div[1]/div/div/div/form/div[3]').click()
#
# # Creates a dataframe
# df = pd.DataFrame({'Link': [''], 'Job Title': [''], 'Company': [''], 'Location': [''], 'Salary': [''], 'Date': ['']})
#
# # This loop goes through every page and grabs all the details of each posting
# # Loop will only end when there are no more pages to go through
# while True:
#     # Imports the HTML of the current page into python
#     soup = BeautifulSoup(driver.page_source, 'lxml')
#
#     # Grabs the HTML of each posting
#     postings = soup.find_all('div', class_='jobsearch-SerpJobCard unifiedRow row result clickcard')
#
#     # grabs all the details for each posting and adds it as a row to the dataframe
#     for post in postings:
#         link = post.find('a', class_='jobtitle turnstileLink').get('href')
#         link_full = 'https://www.indeed.com/' + link
#         name = post.find('h2', class_='title').text.strip()
#         company = post.find('span', class_='company').text.strip()
#         try:
#             location = post.find('div', class_='location accessible-contrast-color-location').text.strip()
#         except:
#             location = 'N/A'
#         date = post.find('span', class_='date').text.strip()
#         try:
#             salary = post.find('span', class_='salaryText').text.strip()
#         except:
#             salary = 'N/A'
#         df = df.append(
#             {'Link': link_full, 'Job Title': name, 'Company': company, 'Location': location, 'Salary': salary,
#              'Date': date},
#             ignore_index=True)
#
#     # checks if there is a button to go to the next page, and if not will stop the loop
#     try:
#         button = soup.find('a', attrs={'aria-label': 'Next'}).get('href')
#         driver.get('https://www.indeed.com/' + button)
#     except:
#         break
#
# df['Date_num'] = df['Date'].apply(lambda x: x[:2].strip())
#
# def integer(x):
#     try:
#         return int(x)
#     except:
#         return x
#
# df['Date_new'] = df['Date_num'].apply(integer)
# df.sort_values(by= ['Date_new', 'Salary'], inplace= True)
#
# df = df[['Link', 'Job Title', 'Company', 'Location', 'Salary', 'Date']]
# df.to_csv('~/Scraped-Data/indeed_scraped_data.csv')
#
#
# #####################################################################################
#
# #Code below sends an email to whomever through python
# import smtplib, ssl
# from email.mime.text import MIMEText
# from email.mime.base import MIMEBase
# from email.mime.multipart import MIMEMultipart
# from email import encoders
#
# #Input the email account that will send the email and who will receiving it
# sender = 'account@gmail.com'
# receiver = 'account@gmail.com'
#
# #Creates the Message, Subject line, From and To
# msg = MIMEMultipart()
# msg['Subject'] = 'New Jobs on Indeed'
# msg['From'] = sender
# msg['To'] = ','.join(receiver)
#
# #Adds a csv file as an attachment to the email (indeed_jobs.csv is our attahced csv in this case)
# part = MIMEBase('application', 'octet-stream')
# part.set_payload(open('A/File/Path/indeed_jobs.csv', 'rb').read())
# encoders.encode_base64(part)
# part.add_header('Content-Disposition', 'attachment; filename ="indeed_jobs.csv"')
# msg.attach(part)
#
# #Will login to your email and actually send the message above to the receiver
# s = smtplib.SMTP_SSL(host = 'smtp.gmail.com', port = 465)
# s.login(user = 'account@gmail.com', password = 'input your password')
# s.sendmail(sender, receiver, msg.as_string())
# s.quit()
#
#
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(
    "https://www.zillow.com/homes/San-Francisco,-CA_rb/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.55177535009766%2C%22east%22%3A-122.31488264990234%2C%22south%22%3A37.69926912019228%2C%22north%22%3A37.851235694487485%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D",
    headers=header)

data = response.text
soup = BeautifulSoup(data, "html.parser")

all_link_elements = soup.select(".list-card-top a")

all_links = []
for link in all_link_elements:
    href = link["href"]
    print(href)
    if "http" not in href:
        all_links.append(f"https://www.zillow.com{href}")
    else:
        all_links.append(href)

all_address_elements = soup.select(".list-card-info address")
all_addresses = [address.get_text().split(" | ")[-1] for address in all_address_elements]

all_price_elements = soup.select(".list-card-heading")
all_prices = []
for element in all_price_elements:
    # Get the prices. Single and multiple listings have different tag & class structures
    try:
        # Price with only one listing
        price = element.select(".list-card-price")[0].contents[0]
    except IndexError:
        print('Multiple listings for the card')
        # Price with multiple listings
        price = element.select(".list-card-details li")[0].contents[0]
    finally:
        all_prices.append(price)

# driver = webdriver.Chrome()
# driver.get ("https://www.amazon.com")
# Create Spreadsheet using Google Form
# Substitute your own path here 👇
# chrome_driver_path = '/Applications/Google Chrome.app'
# driver = webdriver.Chrome(executable_path=chrome_driver_path)

# for n in range(len(all_links)):
#     # Substitute your own Google Form URL here 👇
#     driver.get(URL_TO_YOUR_GOOGLE_FORM)
#
#     time.sleep(2)
#     address = driver.find_element_by_xpath(
#         '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
#     price = driver.find_element_by_xpath(
#         '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
#     link = driver.find_element_by_xpath(
#         '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
#     submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')
#
#     address.send_keys(all_addresses[n])
#     price.send_keys(all_prices[n])
#     link.send_keys(all_links[n])
#     submit_button.click()

