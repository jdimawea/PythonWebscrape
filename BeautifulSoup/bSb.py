from bs4 import BeautifulSoup
import requests

# assigning a variable to the url
website = 'https://subslikescript.com/movie/Titanic-120338'
# Fetching the page
result = requests.get(website)
# This is the page content
content = result.text
# creating the soup
soup = BeautifulSoup(content, 'lxml')
# Displays a nice version of the html of the page
print(soup.prettify())

soup.find('article', class_="main-article")