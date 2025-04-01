auta = ["Ford", "Mustang", "Volkswagen", "Zitroen", "Volvo", "Bolt Ace"]:
x= len(auta) 
    print(x) 
for x in auta:
    print(x)
auta[7] = str(input("Zadej sem jaké auto chceš přidat na konec pole.")):
auta.pop(1)
sorted(auta)
reversed(auta)
print(auta)