from sys import argv
from itertools import count
from itertools import cycle

if(argv[1] == "a"):
	startNumber = int(argv[2])
	endNumber = int(argv[3])

	for item in count(startNumber):
		if item > endNumber:
			break
		print(item)
elif(argv[1] == "b"):
	ls = list(argv[2].strip('"[]').split(", "))
	i = 1
	ml = len(ls)
	for item in cycle(ls):
		print(f"{item}")
		i += 1
		if(i > ml):
			break;
else:
	print("unknown command")