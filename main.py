from bs4 import BeautifulSoup 
import requests 
import fpdf
import re

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
#print()