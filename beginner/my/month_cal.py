rest_life = 10


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
		if month > rest_life * 12:
			break
		month = month + 1
		total_father = total_father * (1 + month_rate)
	total_rate = (total_father - father_money) / father_money * 100
	return [month, month / 12, total_father, total_rate]


father_total = 1200000.0  # 欠款总金额
bank_rest = 225700  # 银行欠款额
father_total += bank_rest
rates = 2.0  # 年化利率
while True:
	try:
		my_save = input("请输入每月可存款金额:")
		if my_save == 'done':
			break
		my_save = float(my_save.rstrip())
		res = calculate(father_total, my_save, rates)
		if res[1] > rest_life:
			print("你这辈子都还不完")
			continue
		print("每月可存款金额%d, 预计月数:%.2f, 预计年数:%.2f, 预计需还总金额:%.2f, 总利率:%.2f%%"
		      % (my_save, res[0], res[1], res[2], res[3]))
		print("那你的工资得要有", (my_save + 7000))
	except ValueError:
		print("输入不正确!")
	except KeyboardInterrupt:
		print("\n程序已关闭")
		break
