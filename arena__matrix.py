m = []

for linha in range(1, 31):
    aux = []
    for coluna in range(1, 41):
        # Horizontal borders
        if linha == 30 or linha == 3:
            aux.append(1)
        # Vertical border
        elif (coluna == 1 or coluna == 40) and linha > 3:
            aux.append(1)

        # Left "]"
        # Up square
        elif coluna == 5 and linha == 11:
            aux.append(1)
        # " | " shape
        elif coluna == 6 and (linha >= 11 and linha <= 20):
            aux.append(1)
        # Down square
        elif coluna == 5 and linha == 20:
            aux.append(1)

        # Right "]"
        # Up square
        elif coluna == 36 and linha == 11:
            aux.append(1)
        # " | " shape
        elif coluna == 35 and (linha >= 11 and linha <= 20):
            aux.append(1)
        # Down square
        elif coluna == 36 and linha == 20:
            aux.append(1)

        # Middle up square
        elif (coluna == 20 or coluna == 21) and (linha >= 6 and linha <= 10):
            aux.append(1)
        # Middle up square
        elif (coluna == 20 or coluna == 21) and (linha >= 22 and linha <= 26):
            aux.append(1)

        # Middle left square
        elif (linha == 15 or linha == 16) and (coluna >= 10 and coluna <= 14):
            aux.append(1)
        # Middle right square
        elif (linha == 15 or linha == 16) and (coluna >= 26 and coluna <= 30):
            aux.append(1)

        # fill zeros
        else:
            aux.append(0)

    m.append(aux)
    print(aux)
