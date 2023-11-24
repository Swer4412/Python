def is_invertible(dct: dict) -> bool:
    """ verifica se un dizionario è invertibile """
    return len(dct.values()) == len(set(dct.values()))


my_dictionary: dict = {'A': 1, 'B': 2, 'C': 3}
print(is_invertible(my_dictionary))

if is_invertible(my_dictionary):
    my_inverse_dictionary = {value: key for key,
                             value in my_dictionary.items()}
    print(my_inverse_dictionary)
else:
    print('Il dizionario non è invertibile')
