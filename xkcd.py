#! python3
# xkcd.py - Downloads every single xkcd comic
import requests, os, bs4

url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
    # Download the page
    print(f'Downloading the page {url}')
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text)
    # Find the url of thr comic image
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = comicElem[0].get('src')
        if comicUrl.startswith('//'):
            comicUrl = 'https:' + comicUrl        
        # Download the image
        print(f'Downloading image {comicUrl}')
        res = requests.get(comicUrl)
        res.raise_for_status()
        # Save the image
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    # Get the previous button url
    prevLink = soup.select('a[rel="prev"]')
    url =  f'http://xkcd.com{prevLink[0].get("href")}'
print('Done!')