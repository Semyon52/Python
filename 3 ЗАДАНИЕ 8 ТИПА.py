letters = 'ТИМОФЕЙ'
count = 0
for a in letters:
    for b in letters:
        for c in letters:
            for d in letters:
                for e in letters:
                    word = a + b + c + d + e
                    if word.count('Т') == 0:
                        continue
                    if word.count('Й') > 1:
                        continue
                    count += 1
print(count)