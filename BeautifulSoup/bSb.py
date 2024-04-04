import time
from bs4 import BeautifulSoup
import requests

root = 'https://subslikescript.com' # original homepage, can reuse variable
website = f'{root}/movies_letter-A' # assigning a variable to the url
result = requests.get(website) # Fetching the page
content = result.text # This is the page content
soup = BeautifulSoup(content, 'lxml') # creating the soup
# print(soup.prettify()) # Displays a nice version of the html of the page

# pagination
pagination = soup.find('ul', class_="pagination")
pages = pagination.find_all('li', class_='page-item')
last_page = pages[-2].text

links = [] # outside so it doesnt creat an empty list

for page in range(1, int(last_page)+1)[:2]: # range(1, 92+1)
    # https: // subslikescript.com/movies_letter-A?page=1
    result = requests.get(f'{website}?page={page}') # Fetching the page. # is going to change the numer because of loop
    content = result.text  # This is the page content
    soup = BeautifulSoup(content, 'lxml')  # creating the soup

    box = soup.find('article', class_="main-article") # .find gets an element


    # .finds_all find all returns a list
    for link in box.find_all('a', href=True):
        links.append(link['href'])

    # print(links)

    for link in links:
        try:
            print(link)
            time.sleep(1)
            result = requests.get(f'{root}/{link}')
            content = result.text
            soup = BeautifulSoup(content, 'lxml')

            box = soup.find('article', class_='main-article')

            title = box.find('h1').get_text()
            transcript = box.find('div', class_="full-script").get_text(strip=True, separator=' ')

            with open(f'{title}.txt', 'w', encoding='utf-8') as file:
                file.write(transcript)

        except: # if it doesn't work, it will go to the next one
            print('----Link not working----')
            print(link)

