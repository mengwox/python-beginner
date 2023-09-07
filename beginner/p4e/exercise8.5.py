# Minimalist Email Client
def print_email_sender(fileName: str):
    try:
        content = open(fileName)
        for curLine in content:
            if not curLine.startswith('From'):
                continue
            words = curLine.rstrip().split()
            if len(words) < 2:
                print("words is empty or only contains one word")
            print(words[1])
    except FileNotFoundError:
        print("can not found the file named:", fileName)


print_email_sender('mbox-short.txt')
