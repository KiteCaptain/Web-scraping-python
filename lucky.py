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
linkElems = soup.select('.yuRUbf a') 
print("Link Elems selected")
# numOpen = min(len(linkElems), 5)
print(len(linkElems))
# x = 15
numOpen = min(5, len(linkElems))
for i in range(len(linkElems)):
    print(linkElems[i])
    # if x > len(linkElems) - 9:
    #     break
    # # x = x + 1
# n = 15
# for i in range(5):
#     webbrowser.open('https://google.com/' +linkElems[n].get('href'))
#     print(str(i) +" ==> " 'https://google.com/' +linkElems[n].get('href'))
#     print(linkElems[])
#     n = n + 1