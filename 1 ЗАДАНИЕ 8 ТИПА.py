letters = 'ГЕПАРД'
count = 0
for a in letters:
    for b in letters:
        for c in letters:
            for d in letters:
                for e in letters:
                    word = a + b + c + d + e
                    if word.count('Г') != 1:
                        continue
                    if word[0] == 'А':
                        continue
                    if word[4] == 'Е':
                        continue
                    count += 1
print(count)