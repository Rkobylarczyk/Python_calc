class calculator():

    def dodaj(self):
        return liczba1+liczba2

    def odejmij(self):
        return liczba1-liczba2

    def pomnoz(self):
        return liczba1*liczba2

    def podziel(a,b):
        return liczba1/liczba2

print("Dobra mordo, takie mamy możliwości")
print("1. dodawanie")
print("2. odejmowanie")
print("3. mnozenie")
print("4. dzielenie")

wybor = input("Co robimy?")

liczba1 = float(input("Pierwsza liczba: "))
liczba2 = float(input("Druga liczba: "))

obj = calculator()

if wybor == 'dodawanie':
   print(liczba1,"+",liczba2,"=",obj.dodaj())

elif wybor == 'odejmowanie':
   print(liczba1,"-",liczba2,"=",obj.odejmij())

elif wybor == 'mnozenie':
   print(liczba1,"*",liczba2,"=",obj.pomnoz())

elif wybor == 'dzielenie':
   print(liczba1,"/",liczba2,"=",obj.podziel())

else:
   print("coś zjebałeś")