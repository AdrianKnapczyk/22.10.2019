pusty_slownik = dict()

pusty_slownik['klucz'] = 'wartosc'
print(pusty_slownik)
pusty_slownik[1] = 'inna wartosc'
print(pusty_slownik)
pusty_slownik['gmail.com'] = 0

print(pusty_slownik)

pusty_slownik['gmail.com'] = pusty_slownik['gmail.com'] + 1
print(pusty_slownik)

