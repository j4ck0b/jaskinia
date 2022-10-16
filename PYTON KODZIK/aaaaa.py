import main
print("Zaje**isty Kalkulator")

wyjscie = False
while wyjscie == False:
 
    print("::Menu::")
    print("1 v_szescian")
    print("2 v_ostroslup_czworokatny")
    print("3 v_walec")
    print("4 v_kuli")
    print("5 v_piramidy")
    print("6 p_kwadratu ")
    print("7 p_prostokątu")
    print("0 Wyjście")
 
    choice = input("Wybierz (1/2/3/4/5/6/7/0):")
 
    if choice == '0':
        pytanie = input("Wyjść z programu? (Tak/Nie): ")
        if pytanie == 'Tak':
            print('Koniec programu!')
            exit()
        else: print('Powrót do programu')

    elif choice == '1': print(main.v_szescian())
    elif choice == '2': print(main.v_ostroslup_czworokatny())
    elif choice == '3': print(main.v_walec())
    elif choice == '4': print(main.v_kuli())
    elif choice == '5': print(main.v_piramidy())
    elif choice == '6': print(main.p_kwadratu())
    elif choice == '7': print(main.p_prostokatu())


    else: print("Wybraleś nieistniejącą opcje!")