#stack.append([])   pop
l = list(eval(input()))
o = int(len(l))
M = [[]]
M[0] = l
for u in range(1, o):
    M.append(list(eval(input())))
print(M)

l = list(eval(input()))
N = [[]]
N[0] = l
for u in range(1, o):
    N.append(list(eval(input())))
print(N)

P = [[0]*o]*o
print(P)
for i in range(o):
    for j in range(o):
        for k in range(o):
            P[i][j] += M[i][k]*N[k][j]
print(P)