for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if not((x == (not y)) <= ((z<=(not w)) and (w <= y))):
                    print(w, x, y, z)