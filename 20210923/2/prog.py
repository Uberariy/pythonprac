sum = 0
while sum<=21:
    a = int(input())
    sum += a
    if a<=0:
        print(a)
        break
else:
    print(sum)