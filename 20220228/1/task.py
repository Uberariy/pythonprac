import multiprocessing as mp
import textdistance

def dist(s1, s2, m):
    if m == "D":
        return textdistance.damerau_levenshtein(s1, s2)
    elif m == "L":
        return textdistance.levenshtein(s1, s2)
    else:
        return -1

s1, s2, m = str(input()), str(input()), str(input())
pool = mp.Pool(1)
process = pool.apply_async(dist, (s1, s2, m,))
try:
	res = process.get(timeout=1)
except mp.context.TimeoutError:
	res = -1
print(res)