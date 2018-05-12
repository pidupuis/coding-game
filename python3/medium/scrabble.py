from collections import Counter

def partial_anagram(a, b):
    if Counter(a) - Counter(b):
         return False
    return True

def compute_score(s):
    return sum([{
        "e": 1, "a": 1, "i": 1, "o": 1, "n": 1, "r": 1, "t": 1, "l": 1, "s": 1, "u": 1,
        "d": 2, "g": 2,
        "b": 3, "c": 3, "m": 3, "p": 3,
        "f": 4, "h": 4, "v": 4, "w": 4, "y": 4,
        "k": 5,
        "j": 8, "x": 8,
        "q": 10, "z": 10,
    }[c] for c in s])

dic = [input() for _ in range(int(input()))]
letters = input()

anagrams = [(compute_score(w), w) for w in dic if partial_anagram(w, letters)]
for anagram in anagrams:
    if anagram[0] == max(anagrams)[0]:
        print(anagram[1])
        break

