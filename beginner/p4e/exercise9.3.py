def mail_sender_count(fileName: str):
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
    return sender_dict


print(mail_sender_count('files/mbox-short.txt'))
