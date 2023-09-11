name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
dict_hour = dict()
for curLine in handle:
    if not curLine.startswith("From"):
        continue
    words = curLine.rstrip().split()
    if len(words) < 6:
        continue
    times = words[5].split(':')
    if len(times) < 1:
        continue
    hour = times[0]
    dict_hour[hour] = dict_hour.get(hour, 0) + 1

list_tuple = list()
for k, v in dict_hour.items():
    list_tuple.append((k, v))
list_tuple.sort()
for item in list_tuple:
    print(item[0], item[1])
