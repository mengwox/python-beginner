Techs = ['MIT', 'Caltech']
Ivys = ['Harvard', 'Yale', 'Brown']
Univs = [Techs, Ivys]
Univs1 = [['MIT', 'Caltech'], ['Harvard', 'Yale', 'Brown']]

print('Univs =', Univs)
print('Univs1 =', Univs1)
print('Univs == Univs1:', Univs == Univs1)

print(id(Univs) == id(Univs1))
print('Id of Univs is', id(Univs))
print('Id of Univs1 is', id(Univs1))

Techs1 = Techs[:]
print(id(Techs1) == id(Techs))
for e in Univs:
	print('Univs contains', e)
	print(' which contains')
	for u in e:
		print(' ', u)
