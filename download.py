import requests
from bs4 import BeautifulSoup


def download(url, name):
    r = requests.get(url, allow_redirects=True)
    open(name, 'wb').write(r.content)

def process_html(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    hrefs = soup.find("a")
    next_links = []
    for a in hrefs:
        try:
            href = a.attrs['href']
            file_or_folder = href.split("/")
            if file_or_folder[-1] == '/':
                next_links.append(url + href)
            else:
                download(url+href, a.get_text())
        except Exception as e:
            print(e)
    return next_links


