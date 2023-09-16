# Search for link values within URL input
import re
import ssl
import urllib.request

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx)
while True:
	content = html.read(1024 * 10)
	if len(content) < 1:
		break
	links = re.findall(b'href="(http[s]?://.*?)"', html.read(1024 * 10))
	for link in links:
		print(link.decode())
html.close()

# Code: http://www.py4e.com/code3/urlregex.py
