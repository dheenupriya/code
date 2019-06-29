import urllib
from bs4 import BeautifulSoup
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter URL:')
count = int(input('Enter count:'))
position = int(input('Enter position:'))-1
html = urllib.urlopen(url,context=ctx).read()

soup = BeautifulSoup(html,"lxml")
href = soup('a')
#print href

for i in range(count):
    link = href[position].get('href', None)
    print (href[position].contents[0])
    html = urllib.urlopen(link).read()
    soup = BeautifulSoup(html,"lxml")
    href = soup('a')