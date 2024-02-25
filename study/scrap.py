import requests
from bs4 import BeautifulSoup

def scrape_site(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    for heading in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"]):
        print(heading.name + ' ' + heading.text.strip())

# Используйте функцию на любом сайте, который вы хотите проанализировать
print(scrape_site('https://www.autodominicana.rent'))