def openFileAndPrint(file: str):
	handle = open(file, 'a')
	handle.write('mawenhao\n')
	handle.close()
	handle = open(file, 'r')
	for line in handle:
		print(line[:-1])
	handle.close()


openFileAndPrint('kids')
