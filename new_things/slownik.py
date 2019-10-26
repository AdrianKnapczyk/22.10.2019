# slownik = {
#     1: "słowo",
#     2: "element",
#     3: "inne słowo",
#     ("blabla",3): "Gram w szachy"}
# print(slownik)
# print(slownik[3])
# print(slownik[("blabla",3)])

slownik2 = {
    (0, 9): "jenosci",
    (10,99): "dziesiątki",
    (100,999): "setki"
}

# print(slownik2.keys())
# print(slownik2.values())
# print(slownik2.items())

x = 5
lista_ze_slownika = slownik2.items()
for element in lista_ze_slownika:
    if element[0][0] <= x <= element[0][1]:
        print(element[1])
        break