import itertools

def get_best_overlap(a, b):
    results = [a + b] # No match
    if a in b: # If contained
        results.append(b)
    for i in range(1, min(len(a), len(b))):
        if a[-i:] == b[:i]: # If overlap
            results.append(a + b[i:])
    # Return shortest value
    return min(results, key=len)

sequences = [input() for _ in range(int(input()))]
min_len = len("".join(sequences))
for p in list(itertools.permutations(sequences)):
    # For each permutations of the list of sequences
    # merge all permutations two by two using best overlap
    # until there is only one sequence left
    while(len(p) > 1):
        p=[get_best_overlap(p[0], p[1]), *p[2:]]
    min_len = min(min_len, len(p[0]))
print(min_len)
