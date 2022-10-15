# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def zad_2_9():

    slowo=(input("wprowadź zdanie "))

    print("Czy litery są wielkie?" , slowo.isupper())
    print("Czy litery są male?" , slowo.islower())
    print(slowo.replace(slowo[0:3], 'ABC'))



def zad_2_15():

    slownik = {"m1": "Ford", "m2": "Fiat", "m3": "Opel", "m4": "Skoda", "m5": "Wołga", "m6": "Dacia"}
    slownik2 = slownik.copy()

    print("copy: ",slownik2)
    print("items: ",slownik2.items())
    slownik2.update({"m7":"FSO"})
    print("update: ", slownik2)

def zad_2_16():

    zb_1_elem_1=int(input("podaj liczbe do zbioru 1: "))
    zb_1_elem_2=int(input("podaj liczbe do zbioru 1: "))
    zb_1_elem_3=int(input("podaj liczbe do zbioru 1: "))
    zb_1_elem_4=int(input("podaj liczbe do zbioru 1: "))

    zb_2_elem_1=int(input("podaj liczbe do zbioru 2: "))
    zb_2_elem_2=int(input("podaj liczbe do zbioru 2: "))
    zb_2_elem_3=int(input("podaj liczbe do zbioru 2: "))
    zb_2_elem_4=int(input("podaj liczbe do zbioru 2: "))


    zbior_1={zb_1_elem_1, zb_1_elem_2, zb_1_elem_3, zb_1_elem_4}
    zbior_2={zb_2_elem_1, zb_2_elem_2, zb_2_elem_3, zb_2_elem_4}


    print("zbior 1 : ", zbior_1)
    print("zbior 2 : ", zbior_2)

    print("suma: ", zbior_1.union(zbior_2))
    print("roznica: ", zbior_1.difference(zbior_2))
    print("wspolna ", zbior_1.intersection(zbior_2))


# print("zad 2_9\n")
# zad_2_9()
# print("\nzad 2_15\n")
# zad_2_15()
# print("\nzad 2_16")
# zad_2_16()

# lista 3
def zad_2_17():
    liczba=eval(input("podaj liczbę: "))

    if(liczba>0):
        print("Liczba jest dodatnia ")
    elif(liczba<0):
        print("Liczba jest ujemna ")
    elif(liczba==0):
        print("liczba jest zerem ")

# zad_2_17()



def zad_2_33():


    punkty = eval(input("podaj liczbę punktów, maksymalnie 50: "))
    procent = (punkty * 100) / 50
    if(punkty<=50 and punkty>=0):
        if(procent==100):
            print("Dostałeś ocenę CEL ")
        elif(procent<100 and procent>=85):
            print("Dostałeś ocenę BDB " , "liczba procent: ", procent,"%")
        elif(procent<85 and procent>=70):
            print("Dostałeś ocenę DB " , "liczba procent: ", procent,"%")
        elif (procent < 70 and procent >= 50):
            print("Dostałeś ocenę DST ", "liczba procent: ", procent,"%")
        elif (procent < 50 and procent >= 40):
            print("Dostałeś ocenę DOP ", "liczba procent: ", procent,"%")
        elif (procent < 40 ):
            print("Dostałeś ocenę NDST ", "liczba procent: ", procent,"%")
    else:
        print("niewlasciwa liczba punktow")





 def zad_2_41():

     liczba=input("wprowadz ciag  ")







# See PyCharm help at https://www.jetbrains.com/help/pycharm/
