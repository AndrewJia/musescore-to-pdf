from bs4 import BeautifulSoup 
import requests 
import fpdf
import re

from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
from webdriver_manager.core.os_manager import OperationSystemManager

options = webdriver.ChromeOptions() 
options.headless = True 

driver = webdriver.Chrome(service=ChromeService( 
	ChromeDriverManager(os_system_manager=OperationSystemManager(os_type="win64")).install()), options=options) 
url = 'https://lolesports.com/schedule?leagues=lcs'
driver.get(url) 

# select Dates and Matches after Future Divider
datesAndMatches = driver.find_elements(By.CSS_SELECTOR, '.future.divider ~ .EventMatch, .future.divider ~ .EventDate') 
print('number of future things is ' + str(len(datesAndMatches)))

nextDate = 'xdd'
for match in datesAndMatches[:20]: 
	# Date
	if match.get_attribute('class') == 'EventDate':
		nextDate = match.find_element(By.CLASS_NAME, 'monthday').text

	# Match
	else:
		names = match.find_elements(By.CLASS_NAME, 'tricode')
		names = [n.text for n in names]
		hour = match.find_element(By.CLASS_NAME, 'hour').text
		ampm = match.find_element(By.CLASS_NAME, 'ampm').text
		print(f'{nextDate} {hour}{ampm} {names[0]} VS {names[1]}')


	

driver.close()
driver.quit()

'''
# function to extract html document from given url 
def urlToSoup(url): 
      
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
      
    # response will be provided in JSON format 
    return BeautifulSoup(response.text, 'html.parser')

#print("Enter url:")
url = 'https://musescore.com/user/17800356/scores/8803419'#input()
soup = urlToSoup(url)

# find all the anchor tags with "href"  
# attribute starting with "https://" 
imgs = soup.find_all('img')

print(soup)
'''