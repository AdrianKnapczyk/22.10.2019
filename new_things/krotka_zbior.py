#zmienna = 0
#while zmienna < 5:
 #   print(zmienna)
    #zmienna += 1
  #  zmienna = zmienna + 1

# Kalkulator : powinno wypisywać
# 5
# 4
# 3
# 2
# 1

# def funkcja_ktora_odlicza(n):
#    while n > 0:
#        print(n)
#        n -= 1
#         n = n - 1
# funkcja_ktora_odlicza(5)

# a = "MOJE IMIE TO ADRIAN".lower()
# print(a)
# a_list = a.split(" ")
# print(a_list)
# a_list[0] = a_list[0].capitalize()
# a_list[3] = a_list[3].capitalize()
# print(a_list)
# print(" ".join(a_list))

# sprawdzanie domeny maili
dane = ["adrian.knapczyk@gmail.com",
        "jan.kowalski@gmail.com",
        "jan.nowak@onet.pl",
        "adam.adam@gmail.com"]

# x = "adrian.knapczyk@gmail.com"



def get_domain(email):
    podzielony_email = email.split("@")
    return podzielony_email[1]

def get_domains(dane):
    for element in dane:
        print(get_domain(element))


# otwieranie pliku i wypisywanie linijek pliku
with open("plik.csv") as plik:
    for linijka in plik:
        print(linijka)
    print(plik)
#
# lista = [1,2,3]
# krotka = (1,1,1,2,3,4)
#
# zbior = { 1,2,3,4,5,5,5,5,}
# print(zbior)