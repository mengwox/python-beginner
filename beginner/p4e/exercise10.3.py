import string

# fileName = input("Enter a file name:")
content = open('files/mbox-short.txt')
char_count = {}
for curLine in content:
    curLine = curLine.rstrip().lower() \
        .translate(str.maketrans('', '', string.punctuation + string.digits + string.whitespace))
    if len(curLine) <= 0:
        continue
    for char in curLine:
        char_count[char] = char_count.get(char, 0) + 1

list_count = []
for key, count in char_count.items():
    list_count.append((key, count))
list_count.sort()
for item in list_count:
    print(item[0], item[1])
