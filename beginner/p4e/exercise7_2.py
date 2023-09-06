# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
total = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    start = line.find('0')
    if start != -1:
        total = total + float(line[start:])
        count = count + 1
print("Average spam confidence:", total / count)
