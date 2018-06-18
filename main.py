import download

BASE_URL = 'https://static.fossee.in/python/Basic-Programming-using-Python/'

next_links = [BASE_URL]

if __name__ == '__main__':
    while next_links != []:
        try:
            new_links = download.process_html(next_links.pop())
            next_links.extend(new_links)
        except Exception as e:
            print(e)

