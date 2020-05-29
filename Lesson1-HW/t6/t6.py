inKm = float(input("Enter distance in km for the first run: "))
inDesiredKm = float(input("Enter desired distance per run: "))

km = inKm
inc = km/10
days = 1
while(km < inDesiredKm):
	km = km + inc
	days = days + 1

print("The day when desired result will be reached:", days)