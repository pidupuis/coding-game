from collections import Counter

def partial_anagram(a, b):
    return False if Counter(a) - Counter(b) else True

def compute_score(s):
    return sum([(
        'eaionrtlsu' +
        'dg'    *  2 +
        'bcmp'  *  3 +
        'fhvwy' *  4 +
        'k'     *  5 + 
        'jx'    *  8 +
        'qz'    * 10
    ).count(c) for c in s])

dic = [input() for _ in range(int(input()))]
letters = input()

anagrams = [(compute_score(w), w) for w in dic if partial_anagram(w, letters)]
print(next((a for a in anagrams if a[0] == max(anagrams)[0]))[1])
