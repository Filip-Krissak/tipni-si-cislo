import random
# nefunguje
min = 0
pokusy = 1

def gen_cislo(max=100):
    return random.randint(min, max)

def nh():
    hrat_znova = input('chces hrat znova? (a/n) ' )
    if hrat_znova == 'a':
        hra()
    elif hrat_znova == 'n':
        quit()
    else:
        print('napis a/n ')
        return nh()

def hra():
    global pokusy
    max = None
    while max is None:
        try:
            max = int(input('ake najvacsie cislo chces ' ))
        except ValueError:
            print('napis cislo')
    cislo = gen_cislo(max)
    guess = None
    while guess is None:
        try:
            guess = int(input('tipni si cislo ' ))
        except ValueError:
            print('napis cislo')
    if guess == cislo:
        print(f'tafil si sa pokusy:{pokusy}')
        nh()
    elif guess >= cislo:
        print('tipol si si moc vysoke cislo')
        pokusy +=1
        hra()
    elif guess <= cislo:
        print('tipol si si moc nizke cislo')
        pokusy +=1
        hra()
        
hra()
