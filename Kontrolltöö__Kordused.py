#5 Вариант
#1
n=(int(input("Kirjutage arv vahemikus 1 kuni 9: ")))
for i in range (n):
    for i in range(n-i-1):
        print(i, end="  ")
    print()
    print(i, ' ~~~~~')
    print(i, '/_____' '\ ')  
    print(i, "| []  |")
    print(i, " ----- ")

#1.(2 Вариант)
while True:
    try:
        mitu=int(input("Mitu tk:  "))
        if 1<mitu<10:
            break
    except ValueError:
        print("Vale tüüp")
for i in range(mitu):
    print('/V\ '.center(10, ' ' ), end="")
print()
for i in range(mitu):
    print('/ V \ '.center(10, ' ' ), end="")
print()
for i in range(mitu):
    print(' / V V \  '.center(10, ' ' ), end="")
print()
for i in range(mitu):
    print('/VV V VV\  '.center(10, ' ' ), end="")
print()

#1.2
while True:
    try:
        mitu=int(input("Mitu tk:  "))
        if 1<mitu<10:
            break
    except ValueError:
        print("Vale tüüp")
for i in range(mitu):
    print('~~~~~ '.center(10, ' ' ), end="")
print()
for i in range(mitu):
    print('/_____\ '.center(10, ' ' ), end="")
print()
for i in range(mitu):
    print(' | []  |  '.center(10, ' ' ), end="")
print()
for i in range(mitu):
    print('----- '.center(10, ' ' ), end="")
print()

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

#2.1
from random import *
while True:
    try:
        N=int(input("Kui palju õpilasi:  "))
        if 10<N<30:
            break
    except ValueError:
        print("Vale tüüp")
kesk1=0
kesk2=0
for i in range(N):
    h1=randint(1,5)
    h2=randint(1,5)
    kesk1+=h1
    kesk2+=h2
kesk1/=N
kesk2/=N
print(f"Keskmine hinne 1 klassis on {kesk1}")
print(f"Keskmine hinne 2 klassis on {kesk2}")
    


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

#4.1
from random import *
sum_num=0
sum_km=0
for i in range(12):
    num=randint(1000,10000)
    km=randint(1,1000)
    sum_num+=num 
    sum_km+=km 
    print(f'{i+1}. maakond. \nElanikud: {num}. Pindala: {km}\n Kokku: {sum_num}, {sum_km}')
vastus=sum_num/sum_km
print(f"Keskmine: {vastus:.3f}")


#5 (4 Вариант)
from random import *
while True:
    try:
        K=int(input("Mitu kotleti sul on?  "))
        if K>0:
            break
    except ValueError:
        print("Vale tüüp")
while True:
    try:
        M=int(input("Mitu kotleti ühel pannil?  "))
        if M>0:
            break
    except ValueError:
        print("Vale tüüp")
pann=0
lisapann=0
while K>M:
        K-=M
        pann+=1
        print(f"Praetud: {pann} tk")
        if K<M:
            pann+=1
            print(f"Praetud: {pann} tk")
print(f"Kokku oli praetud: {pann} panni")
print()
