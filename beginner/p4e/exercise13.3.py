import ssl
import urllib.request

from bs4 import BeautifulSoup


def find_name(url: str, position: int):
	print('Retrieving: ', url)
	html = urllib.request.urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')
	name = ''
	pos = 1

	# Retrieve all of the anchor tags
	tags = soup('a')
	for tag in tags:
		if pos == position:
			url = tag.get('href')
			name = tag.contents[0]
			break
		pos += 1
	return url, name


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL:')
count = int(input('Enter count:'))
position = int(input('Enter position:'))
while count >= 0:
	url, name = find_name(url, position)
	count -= 1
