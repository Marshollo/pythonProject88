# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def zad_2_9():
    slowo = (input("wprowadź zdanie "))

    print("Czy litery są wielkie?", slowo.isupper())
    print("Czy litery są male?", slowo.islower())
    print(slowo.replace(slowo[0:3], 'ABC'))


def zad_2_15():
    slownik = {"m1": "Ford", "m2": "Fiat", "m3": "Opel", "m4": "Skoda", "m5": "Wołga", "m6": "Dacia"}
    slownik2 = slownik.copy()

    print("copy: ", slownik2)
    print("items: ", slownik2.items())
    slownik2.update({"m7": "FSO"})
    print("update: ", slownik2)


def zad_2_16():
    zb_1_elem_1 = int(input("podaj liczbę do zbioru 1: "))
    zb_1_elem_2 = int(input("podaj liczbę do zbioru 1: "))
    zb_1_elem_3 = int(input("podaj liczbę do zbioru 1: "))
    zb_1_elem_4 = int(input("podaj liczbę do zbioru 1: "))

    zb_2_elem_1 = int(input("podaj liczbę do zbioru 2: "))
    zb_2_elem_2 = int(input("podaj liczbę do zbioru 2: "))
    zb_2_elem_3 = int(input("podaj liczbę do zbioru 2: "))
    zb_2_elem_4 = int(input("podaj liczbę do zbioru 2: "))

    zbior_1 = {zb_1_elem_1, zb_1_elem_2, zb_1_elem_3, zb_1_elem_4}
    zbior_2 = {zb_2_elem_1, zb_2_elem_2, zb_2_elem_3, zb_2_elem_4}

    print("zbiór 1 : ", zbior_1)
    print("zbiór 2 : ", zbior_2)

    print("suma: ", zbior_1.union(zbior_2))
    print("różnica: ", zbior_1.difference(zbior_2))
    print("wspólna ", zbior_1.intersection(zbior_2))


def zad_2_17():
    liczba = eval(input("podaj liczbę: "))

    if liczba > 0:
        print("Liczba jest dodatnia ")
    elif liczba < 0:
        print("Liczba jest ujemna ")
    elif liczba == 0:
        print("liczba jest zerem ")


def zad_2_33():
    punkty = eval(input("podaj liczbę punktów, maksymalnie 50: "))
    procent = (punkty * 100) / 50
    if 50 >= punkty >= 0:
        if procent == 100:
            print("Dostałeś ocenę CEL,")
        elif 100 > procent >= 85:
            print("Dostałeś ocenę BDB,", "liczba procent: ", procent, "%")
        elif 85 > procent >= 70:
            print("Dostałeś ocenę DB,", "liczba procent: ", procent, "%")
        elif 70 > procent >= 50:
            print("Dostałeś ocenę DST,", "liczba procent: ", procent, "%")
        elif 50 > procent >= 40:
            print("Dostałeś ocenę DOP,", "liczba procent: ", procent, "%")
        elif procent < 40:
            print("Dostałeś ocenę NDST,", "liczba procent: ", procent, "%")
    else:
        print("niewłaściwa liczba punktów")


def zad_2_40():
    liczba = eval(input("wprowadź liczbę  "))

    wynik = 1

    if liczba == 0:
        print("Wynik silni to, 1")
    else:
        for i in range(1, liczba + 1):
            wynik = wynik * i
        print("Wynik silni to, ", wynik)


def zad_2_41():
    ciag = eval(input("wprowadź ciąg  "))
    x = 0
    y = 1

    for i in range(0, ciag):
        y = y + x
        x = y - x
    print("Wynik ciągu", ciag, "to, ", x)


def zad_2_47():
    liczba = int(input("Wprowadź liczbę większą od 1: "))
    f = 0
    i = 2
    while i <= liczba / 2:
        if liczba % i == 0:
            f = 1
            break
        i = i + 1

    if f == 0:
        print("Wprowadzona liczba jest pierwsza")
    else:
        print("Wprowadzona liczba NIE jest pierwsza")


def zad_2_56():
    str_slowa = ["ALA", "MA", "KOTA"]

    str_slowa = [x.lower() for x in str_slowa]

    print(str_slowa)


############################################### uruchamianie zadań ##########################################
i = True
while i:
    x = eval(
        input("\nWprowadź numer zadania, do wyboru: \n Zadanie 2_9 = 1\n Zadanie 2_15 = 2\n Zadanie 2_16 = 3\n Zadanie "
              "2_17 = 4\n Zadanie 2_33 = 5\n Zadanie 2_40 = 6\n Zadanie 2_41 = 7\n Zadanie 2_47 = 8\n Zadanie 2_56 = "
              "9\n Wyjście = 0\n Wybierasz: "))
    if x == 1:
        zad_2_9()
    elif x == 2:
        zad_2_15()
    elif x == 3:
        zad_2_16()
    elif x == 4:
        zad_2_17()
    elif x == 5:
        zad_2_33()
    elif x == 6:
        zad_2_40()
    elif x == 7:
        zad_2_41()
    elif x == 8:
        zad_2_41()
    elif x == 9:
        zad_2_56()
    elif x == 0:
        i = False
