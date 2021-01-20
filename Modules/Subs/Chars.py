names = ['Naruto Uzumaki', 'Charlie Kelly', 'Deandra Reynolds', 'Dennis Reynolds', 'Sasuke Uchiha', 'Kakashi Hatake',
         'Frank Reynolds', 'Ronald McDonald', 'Konohamaru Sarutobi', 'Madara Uchiha', 'Hashirama Senju']


def last_name(name):
    for i in names:
        if name == i.split()[0]:
            return i.split()[1]


def full_name(name):
    for i in names:
        if name == i.split()[0]:
            return i