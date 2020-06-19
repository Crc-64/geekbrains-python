from sys import argv
import sys

if(len(argv) < 4):
    print("insufficient arguments. Syntax:")
    print("  py l4t1.py [Time] [SalatyPerHour] [SalaryBonus]")
    sys.exit()

t = argv[1]
sph = argv[2]
b = argv[3]

if(not (str.isdecimal(t) or str.isdecimal(sph) or str.isdecimal(b))):
    print("only numbers are accepted")

t = int(t)
sph = int(sph)
b = int(b)
r = t * sph + b

print(f"salary: {r}")
