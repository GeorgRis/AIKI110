def main():
    o = open("problem.txt", "r")
    o_tekst = o.read()
    lr = o_tekst.split('\n')
    tall = lr[0]
    x = int(tall[0])
    y = int(tall[2])
    print(f'{x} {y}')
    for retning in lr:
        for endring in retning:
            if endring == 'S':
                y += 1
            elif endring == 'N':
                y -= 1
            elif endring == 'E':
                x += 1
            elif endring == 'W':
                x -= 1
        if x > 7:
            x = 7
        elif x < 0:
            x = 0
        if y > 7:
            y = 7
        elif y < 0:
            y = 0
    print(f'{x} {y}')

    save = open("geris3014.txt", "w")
    save.write(f'{x} {y}')
    save.close()
if __name__ == "__main__":
    main()
