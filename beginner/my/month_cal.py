def calculate(father_money: float, my_reverse: float, rate: float):
    """
    计算需要多少月,多少年,才能还清父亲的钱
    :param father_money: 欠父亲的金额
    :param my_reverse: 每月能存下的金额
    :param rate: 年利率
    :return: 所需月数,所需年数
    """
    month = 0
    total_father = father_money
    month_rate = rate / 100 / 12
    while True:
        if (month * my_reverse) >= total_father:
            break
        month = month + 1
        total_father = total_father * (1 + month_rate)
    return [month, month / 12]


father_total = 1300000.0
rates = 4.0
# 15000 [137, 11.416666666666666]
# 25000 [65, 5.416666666666667]
while True:
    try:
        my_save = input("请输入每月可存款金额:")
        if my_save == 'done':
            break
        my_save = float(my_save.rstrip())
        res = calculate(father_total, my_save, rates)
        print("每月可存款金额%d, 预计月数:%.2f, 预计年数:%.2f" % (my_save, res[0], res[1]))
        print("那你的工资得要有", (my_save + 7000))
    except ValueError:
        print("输入不正确!")
    except KeyboardInterrupt:
        print("\n程序已关闭")
        break
