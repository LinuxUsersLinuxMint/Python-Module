#!/usr/bin/python3
# Copyright© 2023 LinuxUsersLinuxMint
# Python-Module Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
# Python-Module All Rights Reserved under the GPL(General Public License).
# Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint
# A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint

# Hesap Makinesi Değişkenleri / Calcutator inputs

def top():
    sayi1=int(input('1.sayiyi giriniz: '))
    sayi2=int(input('2.sayiyi giriniz: '))
    sonuc = sayi1 + sayi2
    print("{0} + {1} = {2}". format(sayi1,sayi2,sonuc))
    return
def cık():
    sayi1=int(input('1.sayiyi giriniz: '))
    sayi2=int(input('2.sayiyi giriniz: '))
    sonuc = sayi1 - sayi2
    print("{0} + {1} = {2}". format(sayi1,sayi2,sonuc))
    return
def carp():
    sayi1=int(input('1.sayiyi giriniz: '))
    sayi2=int(input('2.sayiyi giriniz: '))
    sonuc = sayi1 * sayi2
    print("{0} + {1} = {2}". format(sayi1,sayi2,sonuc))
    return
def bol():
    sayi1=int(input('1.sayiyi giriniz: '))
    sayi2=int(input('2.sayiyi giriniz: '))
    sonuc = sayi1 / sayi2
    print("{0} + {1} = {2}". format(sayi1,sayi2,sonuc))
    return
def yuzde():
    sayi1=int(input('1.sayiyi giriniz: '))
    sayi2=int(input('2.sayiyi giriniz: '))
    sonuc = sayi1 % sayi2
    print("{0} + {1} = {2}". format(sayi1,sayi2,sonuc))
    return

islem=input('Gerçekleştirmek İstediğiniz İşlemi Giriniz: ')

def addition():
    number1=int(input('Enter the First Number: '))
    number2=int(input('Enter the Second Number: '))
    result = number1 + number2
    print("{0} + {1} = {2}". format(number1,number2,result))
    return
def subraction():
    number1=int(input('Enter the First Number: '))
    number2=int(input('Enter the Second Number: '))
    result = number1 - number2
    print("{0} + {1} = {2}". format(number1,number2,result))
    return
def multiplication():
    number1=int(input('Enter the First Number: '))
    number2=int(input('Enter the Second Number: '))
    result = number1 * number2
    print("{0} + {1} = {2}". format(number1,number2,result))
    return
def division():
    number1=int(input('Enter the First Number: '))
    number2=int(input('Enter the Second Number: '))
    result = number1 / number2
    print("{0} + {1} = {2}". format(number1,number2,result))
    return
def Percentage():
    number1=int(input('Enter the First Number: '))
    number2=int(input('Enter the Second Number: '))
    result = number1 % number2
    print("{0} + {1} = {2}". format(number1,number2,result))
    return


process=input('Enter the action you want to perform: ')

# number,letter inputs (for random)

numbers=[0,1,2,3,4,5,6,7,8,9,10]
letters="a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"