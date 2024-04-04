import time

from bs4 import BeautifulSoup
import requests

# original homepage, can reuse variable
root = 'https://subslikescript.com'
# assigning a variable to the url
website = f'{root}/movies'
# Fetching the page
result = requests.get(website)
# This is the page content
content = result.text
# creating the soup
soup = BeautifulSoup(content, 'lxml')
# Displays a nice version of the html of the page
# print(soup.prettify())

# .find gets an element
box = soup.find('article', class_="main-article")

links =[]
# .find_all find all returns a list
for link in box.find_all('a', href=True):
    links.append(link['href'])

print(links)


for link in links:
    time.sleep(1)
    website = f'{root}/{link}'
    result = requests.get(website)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')

    box = soup.find('article', class_='main-article')

    title = box.find('h1').get_text()
    transcript = box.find('div', class_="full-script").get_text(strip=True, separator=' ')

    with open(f'{title}.txt', 'w', encoding='utf-8') as file:
        file.write(transcript)