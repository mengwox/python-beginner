import ssl
import urllib.request

import xml.etree.ElementTree as ET

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location:')
print('Retrieving', url)
xml_content = urllib.request.urlopen(url, context=ctx).read()
print('Retrieved %d characters' % len(xml_content))
tree = ET.fromstring(xml_content)
count_soups = tree.findall('.//count')
count = 0
count_sum = 0
for soup in count_soups:
	count_sum += int(soup.text)
	count += 1
print('Count:', count)
print('Sum:', count_sum)
