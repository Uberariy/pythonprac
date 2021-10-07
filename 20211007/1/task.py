def Pareto(*l):
	M = []
	# [(x,y) for x,y in l for a,b in l if all([x>=a and y>=b and (x>a or y>b) for a, b in l])
	for xy in l:
		a = 1
		for ab in l:
			if xy == ab:
				continue
			if not (xy[0] >= ab[0] and xy[1] >= ab[1] and (xy[0] > ab[0] or xy[1] > ab[1])):
				a = 0
				continue
		if a == 1:
			M.append(xy)
	return(tuple(M))

print(Pareto((1,2), (3,4), (2,2), (4,3), (7,0), (1,8)))

