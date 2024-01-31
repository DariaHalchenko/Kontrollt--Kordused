#5 Вариант
1
n=(int(input("Kirjutage arv vahemikus 1 kuni 9: ")))
for i in range (n):
    for i in range(n-i-1):
        print(i, end="  ")
    print()
    print(i, ' ~~~~~')
    print(i, '/_____' '\ ')  
    print(i, "| []  |")
    print(i, " ----- ")


#2
from random import *
õpilased1=int(input("Kui palju õpilasi klassis on: ")
õpilased2=int(input("Kui palju õpilasi klassis on: ")
hinne1=0
hinne2=0
for i in range(õpilased1):
    hinne1=hinne1+random.randint(1,5)
    keskmine_hinne1=hinne1/õpilased1
for i in range(õpilased2):
    hinne2=hinne2+random.randint(1,5)
    keskmine_hinne2=hinne2/õpilased2
    print("Klassi õpilaste keskmine hinne on: "+str(keskmine_hinne1))
    print("Klassi õpilaste keskmine hinne on: "+str(keskmine_hinne2))
    


#3
import random

opilased=random.randint(10,30)
hinnad = [random.randint(1, 100) for i in range(opilased)]
min_hinne=50
max_hinne=50
print("Õppilaste arv: " + str(opilased))
print("Hinnad: "+ str(hinnad))
for i in hinnad:
    hind=i
    if hind<min_hinne:
        min_hinne=hind
    if hind>max_hinne:
        max_hinne=hind
print("Minimaalne punktisumma: "+str(min_hinne))
print("Maksimaalne punktisumma: "+str(max_hinne))

#4
from random import *
elanikud=randint(1,1000)
ruut=randint(1,1000)
tihedus=0
linnaosad=12
for i in range(linnaosad):
    asustustihedus=linnaosad/ruut
    tiheduse_summa+=asustustihedus
    keskmine_tihedus=tiheduse_summa/linnaosad
print("Piirkonna kui terviku keskmine asustustihedus: "+str(keskmine_tihedus))
