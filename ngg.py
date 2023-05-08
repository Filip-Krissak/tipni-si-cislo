import random
while True:
    try:
        c = int(input('ake najvacsie cislo chces? ' ))
        break
    except ValueError:
        print('napis cislo')
def cislo():
    global number
    number = random.randint(0,c)
cislo()

pokusy = 1

def nova_hra():
    global pokusy
    pok = input('chces ist este raz? (a/n) ' )
    if pok == 'a':
        pokusy = 1
        cislo()
        hra()
    elif pok == 'n':
        quit()
    else:
        print('napis: a alebo n')
        nova_hra()

def hra():
    global number
    global pokusy
    print(f'uhadni cislo od 0 do {c}')
    while True:
        try:
            guess = int(input())
            break
        except ValueError:
            print('napis cislo')
    if guess == number:
        print(f'trafil si sa, pocet pokusov: {pokusy}')
        nova_hra()
    elif guess <= number:
        print('trafil si moc nizke cislo')
        pokusy += 1
        hra()
    elif guess >= number:
        print('trafil si moc vysoke cislo')
        pokusy += 1
        hra()
    print(number)
hra()
