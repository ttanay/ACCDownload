import requests
from bs4 import BeautifulSoup


def download(url, name):
    print('Downloading: {}'.format(url))
    r = requests.get(url, allow_redirects=True)
    open(name, 'wb').write(r.content)
    print('Downloaded {}'.format(name))

def process_html(url):
    print('Processing: {}'.format(url))
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    hrefs = soup.find_all("a")
    next_links = []
    for a in hrefs:
        try:
            href = a.attrs['href']
            if '.' in href:
                download_url = url + href
                download(download_url, href)
            else:
                next_links.append(url + href)
        except Exception as e:
            print(e)
    return next_links


