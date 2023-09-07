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
