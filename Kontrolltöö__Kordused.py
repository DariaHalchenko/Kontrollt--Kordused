﻿5 Вариант
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


2
A=(4,5,4,3,5)
B=(4,5,2,3,5)


3
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

4
