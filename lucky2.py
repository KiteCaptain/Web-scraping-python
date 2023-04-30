import requests
from bs4 import BeautifulSoup

query = 'python programming'
url = f'https://www.google.com/search?q={query}'

# Send HTTP request to the Google search results page
response = requests.get(url)
print(response.content)
# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the links of the first five search results
links = []
for result in soup.find_all('div', class_='yuRUbf'):
    link = result.find('a')['href']
    links.append(link)
    if len(links) == 5:
        break

# Print the links
for link in links:
    print(link)
