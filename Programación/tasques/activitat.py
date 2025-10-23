print("Recollida de dades")
titol1 = input("Nom del llibre; ")
autor1 = input("Nom del autor; ")
preu1 = int(input("Preu del llibre; "))
titol2 = input("Nom del llibre; ")
autor2 = input("Nom del autor; ")
preu2 = int(input("Preu del llibre; "))

titol = "titol"
autor = "autor"
preu = "preu"
print(f"{Titol:^30} {Autor:^20} {Preu:^10}")
for i in range (30):
    print("-", ends= "")
print(ends="")
for i in range (20):
    print("-", ends= "")
print(ends="")
for i in range (10):
    print("-", ends= "")
print(ends="")
print()


print(f"{titol1:^30} {autor1:^20} {preu1:^10.2f}")
print(f"{titol2:^30} {autor2:^20} {preu2:^10.2f}")

dia, mes, year = input("Hola, disme la data en aquest format XX/YY/ZZZZ: ").split(/)
print(f"{dia} del {mes} de {year}")