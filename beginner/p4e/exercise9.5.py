def mail_domain_count(fileName: str):
    domain_dict = dict()
    try:
        content = open(fileName)
        for cur_line in content:
            if not cur_line.startswith('From '):
                continue
            words = cur_line.split()
            if len(words) < 2:
                continue
            address = words[1].split('@')
            if len(address) < 2:
                continue
            domain = address[1]
            if domain not in domain_dict:
                domain_dict[domain] = 1
            else:
                domain_dict[domain] += 1
    except FileNotFoundError:
        print('can not find the file named:', fileName)
    return domain_dict


print(mail_domain_count('files/mbox-short.txt'))
