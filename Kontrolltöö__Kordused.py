﻿#5 Вариант
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
klass1=(3,4,5,5,3,2,5,4,4,3,2,5,5,3,4,2,5,5,3,2)
klass2=(5,4,5,5,4,3,3,4,5,5,3,4,3,4,5,5,3,3,4,5)
summa1=0
summa2=0
õpilased1=0
õpilased2=0
for hinne in klass1:
    summa1+=hinne
    õpilased1+=1
    keskmine1=summa1/õpilased1
for hinne in klass2:
    summa2+=hinne
    õpilased2+=1
    keskmine2=summa2/õpilased2
print("Klassi õpilaste keskmine hinne on(A): "+str(keskmine1))
print("Klassi õpilaste keskmine hinne on(B): "+str(keskmine2))
    


#3
from random import *
õpilased=randint(10,30)
hinnad = [randint(1, 100) for i in range(õpilased)]
min_hinne=50
max_hinne=50
print("Õppilaste arv: " + str(õpilased))
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
kogu_rahvastikust=0
kogupindala=0
linnaosad=12
for i in range(linnaosad):
    elanikkonnast=randint(1,1000)
    piirkond=randint(1, 1000)
    tihedus=elanikkonnast/piirkond
    kogu_rahvastikust+=elanikkonnast
    kogupindala+=piirkond
keskmine_tihedus=kogu_rahvastikust/kogupindala
print("Piirkonna kui terviku keskmine asustustihedus: "+str(keskmine_tihedus))
