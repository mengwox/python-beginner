# reads the words in words.txt and stores them as keys in a dictionary.
# It does not matter what the values are. Then you can use the in operator
# as a fast way to check whether a string is in the dictionary.
import string

content = open('files/words.txt')
word_dict = dict()

for line in content:
    line = line.rstrip().lower()
    line = line.translate(line.maketrans('', '', string.punctuation))
    words = line.split()
    for word in words:
        word_dict[word] = 'Have'

while True:
    try:
        word = input('Enter a word to check if exist in words.txt:\n').lower()
        if word == 'done':
            print('check done')
            exit()
        if word in word_dict:
            print('%s exist in file' % word)
        else:
            print('%s not exist in file' % word)
    except KeyboardInterrupt:
        print('keyboard interrupt')
        break
