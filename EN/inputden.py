#!/usr/bin/python3
"Copyright© 2023 LinuxUsersLinuxMint"
"Python Calcutator-inputdtr Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır."
"Python Calcutator-inputdtr All Rights Reserved under the GPL(General Public License)."
"Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint"
"A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint"

command=input('calc> ')
comtxt="calc> "
about="Python Calcutator CLI(Command Line Interface / Komut Satırı Arayüzü) LICENCE=GPL2"
number1=input('{0} Enter The 1st number: '. format(comtxt))
number2=input('{0} Enter The 2st number: '. format(comtxt))
process=input('{0} Enter the Transaction You Want to Perform: '. format(comtxt))
addition=float(number1)+float(number2)
subraction=float(number1)-float(number2)
multiplication=float(number1)*float(number2)
division=float(number1)/float(number2)
Percentage=float(number1)%float(number2)