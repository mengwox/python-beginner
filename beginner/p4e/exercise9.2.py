# categorizes each mail message by which day of the week the commit was done.
# To do this look for lines that start with “From”,
# then look for the third word and keep a running count of
# each of the days of the week.
# At the end of the program print out the contents of your dictionary
# (order does not matter)
def counting_day(fileName: str):
    dict_day_counts = dict()
    try:
        content = open(fileName)
        for cur_line in content:
            if not cur_line.startswith('From'):
                continue
            words = cur_line.split()
            if len(words) < 3:
                continue
            day = words[2]
            if day not in dict_day_counts:
                dict_day_counts[day] = 1
            else:
                dict_day_counts[day] += 1
    except FileNotFoundError:
        print('can not find the file named:', fileName)
    return dict_day_counts


print(counting_day('files/mbox-short.txt'))
