# -*- coding: utf-8 -*-
from random import *
x = randint(1,101)
print "x=?"
while True:
    y = input("Sayıyı tahmin edin:")
    if y < x:
        print "Yukarı"
    elif y > x:
        print "aşağı"
    else:
        print "Tebrikler x=",x," doğru yanıt."
        break
