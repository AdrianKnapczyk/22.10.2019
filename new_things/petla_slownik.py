import csv

def get_domain(email):
    podzielony_email = email.split("@")
    return podzielony_email[1]
#I sposób

# gmail = 0
# kancelaria = 0
# others = 0
# nasz_slownik = {}
#
# with open("nowe_dane.csv") as plik:
#     slownik = csv.DictReader(plik)
#     # print(dict(slownik))
#     for linia in slownik:
#         # print(dict(linia))
#         email_address = linia[slownik.fieldnames[1]]
#         domain = get_domain(email_address)
#         if domain == "gmail.com":
#             gmail = gmail + 1
#         elif domain == "kancelaria.pl":
#             kancelaria = kancelaria + 1
#         else:
#             others = others +1

# alternatywa dla else
        # elif domain != "gmail.com" and domain != "kancelaria.pl":
        #     others = others + 1

#tworzenie słownika z wyników
# nasz_slownik['gmail'] = gmail
# nasz_slownik['kancelaria'] = kancelaria
# nasz_slownik['others'] = others
# print(nasz_slownik)

#Printowanie wyników I sposobu
# print("Poczta gmail: ",gmail)
# print("Poczta kancelaria: ",kancelaria)
# print(others)



    # for linijka in plik:
    #     print(linijka, end='')

# II sposób .
gmail = 0
kancelaria = 0
others = 0
nasz_slownik = {}

with open("nowe_dane.csv") as plik:
    slownik = csv.DictReader(plik)
    # print(dict(slownik))
    for linia in slownik:
        # print(dict(linia))
        email_address = linia[slownik.fieldnames[1]]
        domain = get_domain(email_address)
        if domain in nasz_slownik:
            nasz_slownik[domain] = nasz_slownik[domain] + 1
        else:
            nasz_slownik[domain] = 1

print(nasz_slownik)
