import random
import asyncio
import collections

async def merge(b0, b1, e1, n):
    b, e0, i = b0, b1, b0
    while b0 < e0 and b1 < e1:
        if L[b0] < L[b1]:
            LL[i] = L[b0]
            b0 += 1
        else:
            LL[i] = L[b1]
            b1 += 1
        i += 1
        
    await asyncio.sleep(0)
    #print(f"-> {n}\t", end="")
    LL[i:e1] = L[b0:e0] + L[b1:e1]
    L[b:e1] = LL[b:e1]

async def joiner():
    n = 0
    for p in range(4):
        tasks = []
        b = 2**(p+1)
        for i in range(0, len(L), b):
            E = collections.defaultdict(asyncio.Event)
            tasks.append(asyncio.create_task(merge(i, i+b//2, i+b, n, E)))
            n += 1
        await asyncio.gather(*tasks)

L = list(eval(input()))
LL = L.copy()
asyncio.run(joiner())
print(L)