import textdistance

def dist(s1, s2):
    return textdistance.levenshtein(s1, s2)

s1, s2, m = str(input()), str(input()), str(input())
res = dist(s1, s2)