def most_mail_sender(fileName: str):
    sender_dict = dict()
    try:
        content = open(fileName)
        for cur_line in content:
            if not cur_line.startswith('From '):
                continue
            words = cur_line.split()
            if len(words) < 2:
                continue
            sender = words[1]
            if sender not in sender_dict:
                sender_dict[sender] = 1
            else:
                sender_dict[sender] += 1
    except FileNotFoundError:
        print('can not find the file named:', fileName)
    maxCount = max(list(sender_dict.values()))
    for key, value in sender_dict.items():
        if value == maxCount:
            print(key, value)
            return


most_mail_sender('files/mbox-short.txt')
