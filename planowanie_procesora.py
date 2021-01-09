def wyswietl_tabelke(tab):
    for element in tab: # wypisanie elementów tablicy
        print(element, end=" | ")
    print()

        

print("Witaj w algorytmie planowania przydziału procesora")
print("Wybierz jaki algorytm chcesz użyć:")
print("FCFS")
print("SJF")
print("SRT") # wywłaszczeniowy
print("RR") # wywłaszczneniowy

ilosc_procesow = int(input("Podaj ile masz procesów:"))
print()

# definiowanie rozmiarów list
P = [ "P" + str(x+1) for x in range(ilosc_procesow)]
CN = [0 for x in range(ilosc_procesow)]
CFP = [0 for x in range(ilosc_procesow)]
priorytety = [0 for x in range(ilosc_procesow)]

# wczytywanie danych podanych przez użytkownika
print("Podaj dane dla każego procesu")
for i in range(ilosc_procesow):
    CN[i] = int(input("Podaj CN dla P" + str(i+1) + ":"))
    CFP[i] = int(input("Podaj CFP dla P" + str(i+1) + ":"))
    priorytety[i] = int(input("Podaj priorytet dla P" + str(i+1) + ":"))
    print()
    

# to zobaczy użytkownik żeby sprawdzić czy dobrze dane wprowadził
print("procesy:")
wyswietl_tabelke(P)
print("CFP:")
wyswietl_tabelke(CN)
print("CN:")
wyswietl_tabelke(CFP)
print("Priorytety")
wyswietl_tabelke(priorytety)

#do zrobienia: no to faktyczne działanie tych algorytmó i wypisanie wyników
# np w postaci   {0} P1 {2} | {2} P2 {4} |  -> FCFS




