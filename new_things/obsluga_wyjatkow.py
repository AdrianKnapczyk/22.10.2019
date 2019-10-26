zmienna1 = input("Podaj liczbę: ")
zmienna2 = input("Podaj liczbę: ")

try:
    a = int(zmienna1)
    b = int(zmienna2)
    print(f"suma liczba to {a+b}")

except Exception:
    print("Nie byłem w stanie zrzutować na inta")

print("Koniec")

