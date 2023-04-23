#import libraries
import requests
from bs4 import BeautifulSoup
import googletrans

#get the webpage
url = 'https://en.wikipedia.org/wiki/Main_Page'
page = requests.get(url)

#parse the html
soup = BeautifulSoup(page.content, 'lxml')

#extract all html headers
headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

#create an empty list to store the translated headers
translated_headers = []

#translate the headers to chinese
translator = googletrans.Translator()
for header in headers:
    trans_dict = {
        "name": header.name,
        "text": translator.translate(header.text, dest='zh-cn').text,
    }
    translated_headers.append(trans_dict)

#create an html file to store the translated headers
with open('translated_headers.html', 'w') as f:
    # write the translated headers to the html file
    f.write('<html><head><title>Translated Headers</title></head><body>')
    for header in translated_headers:
        f.write(f'<{header["name"]}>' + header["text"] + f'</{header["name"]}>')
    f.write('</body></html>')
