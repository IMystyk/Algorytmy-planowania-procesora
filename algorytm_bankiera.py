def wyswietl_tabelke(tab):
    for linia in tab:  # wypisanie elementów tablicy 2D
        for element in linia:
            print(element, end=" | ")
        print()

def suma_kolumn(tab,ilosc_proc, x): # tab musi być 2D
    suma = 0
    if( x == 0 ):
        return 0

    for y in range(ilosc_proc+1):
        if( y == 0 ):
            continue
        suma = suma + int(tab[y][x])
    return suma

def tabelki_z_pliku():
    f1 = open("tabelka_przydzial.txt",'r')
    f2 = open("tabelka_max.txt",'r')


    # wyliczenie rozmiaru tabelek czyli ilosc procesów i zasobów
    ile_procesow = 0
    ile_zasobow = 0
    j = 0
    for linia in f1: # liczy z tabelki ile procesow jest tam
        if( linia == "" ):
            continue

        ile_procesow = ile_procesow + 1
        if( j == 0 ): # tylko liczy raz ilosc zasobów bo po co za każdym razem
            # liczy ilosc zasobow
            linia = linia.rstrip("\n")
            linia = linia.rstrip(" ")
            pom_tab = linia.split(' ')
            ile_zasobow =  len(pom_tab)
            j = j + 1

    f1.seek(0) # powraca na poczt pliku

    # zdefiniowanie rozmiaru tabelek
    tabelka_przydz = [[0 for x in range(ile_zasobow + 1)] for y in range(ile_procesow + 1)]  # deklaracja tabelki
    tabelka_maxim = [[0 for x in range(ile_zasobow + 1)] for y in range(ile_procesow + 1)]  # deklaracja tabelki

    # dopisanie do tabelek kilku ważnych rzeczy
    slownik = ["-", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    for x in range(ile_zasobow + 1):
        tabelka_przydz[0][x] = tabelka_maxim[0][x] = slownik[x]

    for i in range(ile_procesow + 1):
        if (i == 0):
            continue
        tabelka_przydz[i][0] = tabelka_maxim[i][0] = "P" + str(i)


    # przepisanie wartości do tabelek
    x = 1
    y = 0

    for linia in f1: # bierze z tabelki linie dla danego procesu
        if( linia == "" ):
            continue
        y = y + 1 # iteruje po wierszach
        x = 1  # warto x = 1 dla kazdego wiersza
        linia = linia.rstrip("\n")
        linia = linia.rstrip(" ")
        pom_tab = linia.split(' ')
        for element in pom_tab: # przepisanie warotści z tabelki pom do tabelki przydzielone
            tabelka_przydz[y][x] = int(element)
            x = x + 1
        #tabelka_przydz[y] = pom_tab
        '''
        for i in linia: # wczytuje zasoby dla danego procesu
            if( i == ' ' or i == '\n'): # pomija spacje
                 continue
            x = x + 1
            tabelka_przydz[y][x] = i
        '''

    x = 1
    y = 0
    for linia2 in f2: # bierze z tabelki linie dla danego procesu
        if( linia2 == "" ):
            continue
        y = y + 1 # iteruje po wierszach
        x = 1 # warto x = 1 dla kazdego wiersza
        linia2 = linia2.rstrip("\n")
        linia2 = linia2.rstrip(" ")
        pom_tab = linia2.split(' ')
        for element in pom_tab: # przepisanie warotści z tabelki pom do tabelki przydzielone
            tabelka_maxim[y][x] = int(element)
            x = x + 1
        #tabelka_maxim[y] = pom_tab
        '''
        for i2 in linia2: # wczytuje zasoby dla danego procesu
            if( i2 == ' ' or i2 == '\n'): # pomija spacje
                 continue
            x = x + 1
            tabelka_maxim[y][x] = i2
        '''
    # zamknięcie plików

    f1.close()
    f2.close()
    return ile_procesow,ile_zasobow,tabelka_przydz,tabelka_maxim
#def plik_do_tablicy

# zmienna globalna
aktualizacja_danych = 0
while( aktualizacja_danych != 3 ):

    if( aktualizacja_danych == 0 ):  # to do obsług żądań
        print("Witaj w algorytmie bankiera")
        print("1 - Podaje dane z konsoli")
        print("2 - Podaje dane z pliku")
        jak = int(input(">>>>:"))
        tabelki_z_pliku()
        if( jak == 1 ):
            ilosc_procesow = int(input("Ile jest procesów:"))
            ilosc_zasobow = int(input("Ile jest zasobów (zasob to A,B...)(max to 9 w tym programie):"))

        slownik = ["-","A","B","C","D","E","F","G","H","I","J"]

        # deklaracja tabelek
        if( jak == 1 ):
            tabelka_przydzielone = [[0 for x in range(ilosc_zasobow+1)] for y in range(ilosc_procesow+1)] # deklaracja tabelki
            tabelka_max = [[0 for x in range(ilosc_zasobow+1)] for y in range(ilosc_procesow+1)] # deklaracja tabelki
            tabelka_dostępne = [[0 for x in range(ilosc_zasobow+1)] for y in range(ilosc_procesow+1)] # deklaracja tabelki
            tabelka_potrzebne = [[0 for x in range(ilosc_zasobow+1)] for y in range(ilosc_procesow+1)] # deklaracja tabelki

        if( jak == 2 ):
            ilosc_procesow,ilosc_zasobow,tabelka_przydzielone,tabelka_max = tabelki_z_pliku()

            # deklaracja tabelek
            tabelka_dostępne = [[0 for x in range(ilosc_zasobow + 1)] for y in range(ilosc_procesow + 1)]  # deklaracja tabelki
            tabelka_potrzebne = [[0 for x in range(ilosc_zasobow + 1)] for y in range(ilosc_procesow + 1)]  # deklaracja tabelki



        # dopisanie do tabelek kilku ważnych rzeczy
        for x in range(ilosc_zasobow+1):
            tabelka_przydzielone[0][x] = tabelka_max[0][x] = tabelka_dostępne[0][x] = tabelka_potrzebne[0][x] = slownik[x]

        for i in range(ilosc_procesow+1):
            if( i == 0 ):
                continue
            tabelka_przydzielone[i][0] = tabelka_max[i][0] = tabelka_potrzebne[i][0] = "P" + str(i)
            tabelka_dostępne[i][0] = "P?"



        # użytkownik podaje dane
        if( jak == 1 ):
            print("Zawsze jako dane masz full tabelke przydzielone i max, więc teraz je uzupełnisz")
            print()
            print("Tabelka przydzielone")
            wyswietl_tabelke(tabelka_przydzielone)

            for y in range(ilosc_procesow+1):
                if( y == 0 ):
                    continue

                for x in range(ilosc_zasobow+1):
                    if( x == 0 ):
                        continue
                    tabelka_przydzielone[y][x] = int(input("Podaj teraz wartośc dla P" + str(y) + "-" + tabelka_przydzielone[0][x] + ":"))
                    wyswietl_tabelke(tabelka_przydzielone)
            print("-----------------------------------------")
            print()
            print("Tabelka max")
            wyswietl_tabelke(tabelka_max)

            for y in range(ilosc_procesow+1):
                if( y == 0 ):
                    continue

                for x in range(ilosc_zasobow+1):
                    if( x == 0 ):
                        continue
                    tabelka_max[y][x] = int(input("Podaj teraz wartośc dla P" + str(y) + "-" + tabelka_max[0][x] + ":"))
                    wyswietl_tabelke(tabelka_max)
        print("-----------------------------------------")
        print()
        print("Tabelka dostępne")
        print("Teraz są 2 opcje")
        print(" 1.Masz pierwszy wiersz podany")
        print(" 2.Masz podaną liczbę egzemplaży w systemie")

        wybor = int(input("Co ty masz:"))

        if( wybor == 1 ):
            print("Podaj pierwszy wiersz w tabelce dostępne ( resztę wyliczy sam program )")
            for x in range(ilosc_zasobow+1):
                if( x == 0 ):
                    continue
                tabelka_dostępne[1][x] = int(input("Podaj teraz wartośc dla " + tabelka_dostępne[0][x] + ":"))


        if( wybor == 2 ):
            print("Podasz liczbę egzemplarzy w ststemie ( np. A:11,B:3...)")
            for x in range(ilosc_zasobow+1):
                if( x == 0 ):
                    continue

                wartosc = int(input("Podaj wartość dla " + tabelka_dostępne[0][x]+ ":"))
                tabelka_dostępne[1][x] = wartosc - suma_kolumn(tabelka_przydzielone,ilosc_procesow,x)

        wyswietl_tabelke(tabelka_dostępne)

    if( aktualizacja_danych == 0 or aktualizacja_danych == 1 ):
        # teraz wszystko program wyliczy

            # tabelka potrzebne
        for y in range(ilosc_procesow+1):
            if( y == 0 ):
                continue

            for x in range(ilosc_zasobow+1):
                if( x == 0 ):
                    continue

                tabelka_potrzebne[y][x] = tabelka_max[y][x] - tabelka_przydzielone[y][x]

        #print()
        #wyswietl_tabelke(tabelka_potrzebne)
            # tabelka dostępne, czyli całkowici algorytm

        procesy_uzyte = [0 for x in range(ilosc_procesow+1)] # wskazuje, które procesy zostały już użyte
        #zakonczone = 1 # zakładamy, że znaleziono bezpieczne ułożenie procesów

        for y in range(ilosc_procesow+1): # iteruje po wierszach tabelki dostępne
            if( y == 0 ):
                continue
            znaleziony = 1 # zakładamy, że jest taki proces co pasuje
            for y2 in range(ilosc_procesow + 1): # iteruje po wiersza tabelki potrzebne
                if( y2 == 0 ):
                    continue
                for x in range(ilosc_zasobow+1): # iteruje po x w obu tabelkach
                    if( x == 0 ):
                        continue
                    if( tabelka_dostępne[y][x] < tabelka_potrzebne[y2][x] ):
                        znaleziony = 0 # jeśli nie znajdzie w tym wierszu odpowiedniego procesu zwroci 0

                if( znaleziony == 0 ):
                    znaleziony = 1 # gdy nie znaleziono musi szukać dalej
                    continue

                if( znaleziony == 1 ): # gdy znajdzie taki proces
                    #uzyty = 0 # zakładamy, że proces nie jest użyty
                    #for i in range(ilosc_procesow+1): # sprawdza czy proces nie jest użyty
                    if( procesy_uzyte[y2] == 1 ): # proces jest już użyty
                        continue # no to szukamy innego procesu
                    # gdy nie jest proces użyty
                    procesy_uzyte[y2] = 1 # zmieniamy stan na użyty
                    tabelka_dostępne[y][0] = "P" + str(y2) # wstawiamy proces do tabelki
                     # teraz zwolnienie zasobów procesu i przydzielenie do dostępnych
                    for j in range(ilosc_zasobow+1):
                        if( j == 0 ):
                            continue
                        if( y+1 > ilosc_procesow): # dalej już nas nie iteresuje
                            break
                        tabelka_dostępne[y+1][j] = tabelka_dostępne[y][j] + tabelka_przydzielone[y2][j]
                    break
        # finalne wyniki
        print("--------------------")
        print()
        print("Finalnie wszystkie tabelki:")

        print("-----------------")
        print("tabelka przydzielone:")
        print()
        wyswietl_tabelke(tabelka_przydzielone)
        print()

        print("-----------------")
        print("tabelka max:")
        print()
        wyswietl_tabelke(tabelka_max)
        print()

        print("-----------------")
        print("tabelka dostępne:")
        print()
        wyswietl_tabelke(tabelka_dostępne)
        print()

        print("-----------------")
        print("tabelka potrzebne:")
        print()
        wyswietl_tabelke(tabelka_potrzebne)
        print()


    print("Teraz obsługa żądań:")
    print("1. Mam żadania")
    print("2. Kończ już ten program")
    co = int(input("wybor>>>:"))
    print()

    # Obsługa żądania

    if( co == 1 ):
        print("Teraz podasz wszystkie żądania:")
        while(1):
            print("(-1 konczy działanie programu)")
            print()
            print("Żadanie:")
            proces = int(input("Podaj numer procesu: (p4 to podaj 4):")) # czyli dla list -1 nr
            zasob = int(input("Podaj numer zasoby: (A to 1, B to 2...):"))
            ile = int(input("Podaj ile chce tego zasobu:"))
            print()
            if( ile == -1 ):
                aktualizacja_danych = 3
                break
            if( ile > tabelka_potrzebne[proces][zasob] ): # 1 warunek ktory odrzuca żądanie
                print("Żadanie zasobu dla tego procesu jest większe niż wartośc potrzebne dla tego procesu dla tego zasobu")
                print("w tabelce Potrzebne")
                print()
                continue

            if (ile > tabelka_dostępne[1][zasob]):  # 2 warunek ktory odrzuca żądanie
                print("Żadanie zasobu dla tego procesu jest większe niż wartośc w pierwszym wierszu dostępne dla tego zasobu")
                print("W tabelce Dostępne")



            else:
                # zmiana danych w tabelce i wykonanie algorytmu bankiera
                tabelka_dostępne[1][zasob] = tabelka_dostępne[1][zasob] - ile
                tabelka_przydzielone[proces][zasob] = tabelka_przydzielone[proces][zasob] + ile
                tabelka_potrzebne[proces][zasob] = tabelka_potrzebne[proces][zasob] - ile
                aktualizacja_danych = 1
                print("Po wykonaniu żądania:")
                break

    if( co == 2 ):
        aktualizacja_danych = 3
        break