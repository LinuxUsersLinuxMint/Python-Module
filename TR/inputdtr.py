#!/usr/bin/python3
"Copyright© 2023 LinuxUsersLinuxMint"
"Python Calcutator-inputdtr Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır."
"Python Calcutator-inputdtr All Rights Reserved under the GPL(General Public License)."
"Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint"
"A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint"

command=input('calc> ')
comtxt="calc> "
about="Python Hesap Makinesi CLI(Command Line Interface / Komut Satırı Arayüzü) LICENCE=GPL2"
sayi1=input('{0} 1. sayiyi giriniz: '. format(comtxt))
sayi2=input('{0} 2. sayiyi giriniz: '. format(comtxt))
islem=input('{0} Gerçekleştirmek İstediğiniz İşlemi Giriniz: '. format(comtxt))
top=float(sayi1)+float(sayi2)
cık=float(sayi1)-float(sayi2)
carp=float(sayi1)*float(sayi2)
bol=float(sayi1)/float(sayi2)
yuzde=float(sayi1)%float(sayi2)