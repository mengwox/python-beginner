import json
import ssl
from urllib import parse, request

service_url = 'http://py4e-data.dr-chuck.net/json?'
api_key = 42

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

input_location = input('Enter location:')
params = dict()
params['address'] = input_location
params['key'] = api_key

url = service_url + parse.urlencode(params)
print('Retrieving', url)
geo_json = request.urlopen(url, context=ctx).read().decode()
print('Retrieved', len(geo_json), 'characters')
count = 0
count_sum = 0
try:
	js = json.loads(geo_json)
except:
	js = None

if not js or 'status' not in js or js['status'] != 'OK':
	print('==== Failure To Retrieve ====')
	print(js)
else:
	print('Place id', js['results'][0]['place_id'])