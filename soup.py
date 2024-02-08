# Install the required libraries
# pip install requests
# pip install beautifulsoup4

import site_status
from bs4 import BeautifulSoup

# URL of the webpage you want to scrape
url = 'https://google.com'

# Send a GET request to the URL
response = site_status.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract information from the webpage
    # For example, let's say you want to get all the links on the page
    links = soup.find_all('a')

    # Print the links
    for link in links:
        print(link.get('href'))
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
