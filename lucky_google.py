#! python
# lucky.py - Opens several Google search results
import requests, sys, webbrowser, bs4
print('Googling...') # Display text while downloading the Google page
res = requests.get('https://google.com/search?q=' + ''.join(sys.argv[1:]))
print("Res downloaded")
try:
    res.raise_for_status()
except Exception as e:
    print('Problem %s' %e)

# Retrieve top search results
soup = bs4.BeautifulSoup(res.text, features="html.parser")
print("Soup created")
# Open a browser tab for each result
linkElems = soup.select('a') 
print("Link Elems selected")
numOpen = min(5, len(linkElems))
print(len(linkElems))
for i in range(numOpen):
    print(linkElems[i])
    
# for i in range(numOpen):
#     webbrowser.open('https://google.com/' +linkElems[i].get('href'))
#     print(str(i) +" ==> " 'https://google.com/' +linkElems[i].get('href'))