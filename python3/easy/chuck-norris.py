def text_to_bits(text):
    return "".join(
        b.zfill(7 * ((len(b) + 6) // 7)) for b in [
            bin(int.from_bytes(x.encode(), 'big'))[2:] for x in text
        ]
    )

seq = text_to_bits(input())

answer = ""
current = seq[0]
cpt = 0
for i, c in enumerate(seq):
    if c != current:
        answer += "0 " if int(current) else "00 "
        answer += cpt * "0"
        answer += " "
        current = c
        cpt = 1
    else:
        cpt += 1
    
    if i == len(seq) - 1:
        answer += "0 " if int(current) else "00 "
        answer += cpt * "0"

print(answer)
