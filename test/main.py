#!/usr/bin/python3
from inputd import *

select=input('İşlem Giriniz: ')

if select=="top":
    top()
elif select=="cık":
    cık()
elif select=="carp":
    carp()
elif select=="bol":
    bol()
elif select=="yuzde":
    yuzde()
else:
    print("Hiç bir işlem girilmedi...")