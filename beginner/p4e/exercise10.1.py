content = open('files/mbox-short.txt')
addr_dict = dict()
for curLine in content:
    if not curLine.startswith("From"):
        continue
    words = curLine.rstrip().split()
    if len(words) < 2:
        continue
    address = words[1]
    addr_dict[address] = addr_dict.get(address, 0) + 1
list_tuple = list()
for k, v in addr_dict.items():
    list_tuple.append((v, k))
list_tuple.sort(reverse=True)
print(list_tuple[0])
