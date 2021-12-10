import math as math
def lvlwhat(sttr, c):
	return c in sttr[1:len(sttr)-1]

sttr = str(input()).split()[0];	sttr = str(input()).split()[0]
H = len(sttr)-2
gas = 1 if lvlwhat(sttr, ".") and not lvlwhat(sttr, "~") and not lvlwhat(sttr, "#") else 0
while not lvlwhat(sttr, "~") and not lvlwhat(sttr, "#"):
	sttr = str(input()).split()[0]
	gas += 1 if lvlwhat(sttr, ".") and not lvlwhat(sttr, "~") and not lvlwhat(sttr, "#") else 0
water = 1 if lvlwhat(sttr, "~") else 0
while not lvlwhat(sttr, "#"):
	sttr = str(input()).split()[0]
	water += 1 if lvlwhat(sttr, "~") and not lvlwhat(sttr, "#") else 0
L = water+gas

print("#"*(L+2))
for i in range(math.trunc(gas*H/L)):
	print("#"+"."*L+"#")
for i in range(math.trunc(water*H/L)+1):
	print("#"+"~"*L+"#")
print("#"*(L+2))
o = int(max(round(gas/max(gas,water)*20), water/max(gas,water)*20))
print("{:<"f"{o}""} {:>"f"{1+len(str(max(gas*H, water*H)))+len(str((water+gas)*H))}""}".format("."*round(gas/max(gas,water)*20),str(gas*H)+"/"+str((water+gas)*H)))
print("{:<"f"{o}""} {:>"f"{1+len(str(max(gas*H, water*H)))+len(str((water+gas)*H))}""}".format("~"*round(water/max(gas,water)*20),str(water*H)+"/"+str((water+gas)*H)))