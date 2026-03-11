letters = 'ИВАН'
count = 0
for a in letters:
    for b in letters:
        for c in letters:
            for d in letters:
                for e in letters:
                    word = a + b + c + d + e
                    if word.count('И') == 0:
                        continue
                    count += 1
print(count)