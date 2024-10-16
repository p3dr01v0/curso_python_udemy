def repeticao(quantidade=20):
    rep = [0, 1]
    while True:
        rep.append(sum(rep[-2:]))
        if len(rep) == quantidade:
            break
    return print(rep)


repeticao()
