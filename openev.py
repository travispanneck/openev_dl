import requests
import re
from bs4 import BeautifulSoup
import os

url = 'https://openev.debatecoaches.org/'

r = requests.get(url, verify=False)

soup = BeautifulSoup(r.text, 'html.parser')



a = soup.find_all('a', href=True)
for link in a:
    if '.docx' in link['href']:
        folder = link.next_element.next_element.next_sibling.get_text()
        local_filename = folder + '/' + link.next_element + '.docx'
        os.makedirs(os.path.dirname(local_filename), exist_ok=True)


        q = requests.get(link['href'], verify=False)

        with open(local_filename, 'wb') as f:
            f.write(q.content)
