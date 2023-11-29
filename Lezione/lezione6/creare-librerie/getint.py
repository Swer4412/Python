def get_int(message, x, y):
    """ controlla gli errori di inserimento """
    # controllo degli errori che si possono verificare
    finished = False
    while not finished:
        try:
            value = int(input(message))
            if x <= value <= y:
                finished = True
            else:
                print('Attenzione, il valore intero deve essere compreso tra', x, 'e', y)
        except ValueError:
            print('Attenzione, non hai inserito un numero intero')

    return value


def main():
    """ main program """
    p = get_int('Inserisci un intero (compreso tra 5 e 49): ', 5, 49)
    print('Hai inserito', p, 'Bravo!!!')


if __name__ == '__name__':
    main()
