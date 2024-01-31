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
from random import *
hinne=randint(1,100)
min_hinne=0
max_hinne=0
for i in hinne:
    if hinne<min_hinne:
        min_hinne=hinne 
    if hinne>max_hinne:
        max_hinne=hinne 
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
