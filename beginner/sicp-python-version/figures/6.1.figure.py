def copy(L1: list, L2: list) -> list:
	if id(L1) == id(L2):
		return L1
	while len(L2) > 0:
		L2.pop()
	for e in L1:
		L2.append(e)
	return L1


def test_copy():
	L1 = [1, 2, 3]
	L2 = [1, 2, 3]
	res = copy(L1, L2)
	print(res)


test_copy()
