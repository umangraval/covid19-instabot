import requests 
from bs4 import BeautifulSoup 
  
URL = "http://best-hashtags.com/hashtag/indian/"
r = requests.get(URL) 
soup = BeautifulSoup(r.content, 'html5lib') 
hashtgs = soup.find('p1').getText()
print(hashtgs)