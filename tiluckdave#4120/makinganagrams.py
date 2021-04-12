from collections import Counter

def makingAnagrams(s1, s2):
    return len(s1)+len(s2)-sum((Counter(s1) & Counter(s2)).values())*2