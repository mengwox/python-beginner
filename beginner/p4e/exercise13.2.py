import ssl
from urllib.request import urlopen

from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html_url = input('Enter - ')
html_content = urlopen(html_url, context=ctx)
soup = BeautifulSoup(html_content, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
total = 0
count = 0
for tag in tags:
	total += int(tag.contents[0])
	count += 1
print('Count ', count)
print('Sum ', total)
