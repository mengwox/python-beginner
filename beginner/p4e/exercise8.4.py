# Find all unique words in a file
# Shakespeare used over 20,000 words in his works.
# But how would you determine that?
# How would you produce the list of all the words that Shakespeare used?
# Would you download all his work, read it and track all unique words by hand?
# Let’s use Python to achieve that instead.
# List all unique words, sorted in alphabetical order,
# that are stored in a file romeo.txt containing a subset of Shakespeare’s work.
# To get started, download a copy of the file www.py4e.com/code3/romeo.txt.
# Create a list of unique words, which will contain the final result.
# Write a program to open the file romeo.txt and read it line by line.
# For each line, split the line into a list of words using the split function.
# For each word, check to see if the word is already in the list of unique words.
# If the word is not in the list of unique words, add it to the list.
# When the program completes, sort and print the list of unique words in alphabetical order.
def find_unique_words(fileName: str):
    unique_words = []
    try:
        content = open(fileName)
        for curLine in content:
            words = curLine.split()
            if len(words) == 0:
                continue
            for word in words:
                if word not in unique_words:
                    unique_words.append(word)
        unique_words.sort()
        print(unique_words)
    except FileNotFoundError:
        print("can't found the file named:", fileName)


find_unique_words("romeo123.txt")
