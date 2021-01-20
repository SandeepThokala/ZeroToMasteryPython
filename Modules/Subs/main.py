from Subs.Chars import full_name, names


def bird(user='Charlie', name='Dee'):
    print(f'{full_name(user)}: \"{name}\'s a bird..!!\"')


def attack(user='Naruto', name='Rasengan'):
    print(f'{full_name(user)}: \"{name}..!!\"')


attack('Madara', 'Susano\'s')
attack('Hashirama', 'Wood style: 1000 arms')
bird('Frank', 'Madara')
print(names)
