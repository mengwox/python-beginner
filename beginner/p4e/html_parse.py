import re

href = '(http[s]?://.+?)"'
content = open('files/html.txt')
for cur_line in content:
	words = re.findall(href, cur_line)
	if len(words) < 1:
		continue
	for word in words:
		print(word)
