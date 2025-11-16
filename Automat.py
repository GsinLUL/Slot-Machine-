import random
import emoji
import time
import string
import os
import math
penazenka = 500
def hra(vkald):
    global penazenka
    for i in range (10) :
        os.system("cls")
        o1 = random.randrange(1, 4)
        o2 = random.randrange(1, 4)
        o3 = random.randrange(1, 4)
        if (i==9):
            if (o1 == 1):
                f1 = ("\U0001F349")
            if (o1 == 2):
                f1 = ("\U0001F352")
            if (o1 == 3):
                f1 = ("\U0001F34A")
            if (o2 == 1):
                f2 = ("\U0001F349")
            if (o2 == 2):
                f2 = ("\U0001F352")
            if (o2 == 3):
                f2 = ("\U0001F34A")
            if (o3 == 1):
                f3 = ("\U0001F349")
            if (o3 == 2):
                f3 = ("\U0001F352")
            if (o3 == 3):
                f3 = ("\U0001F34A")
            print("Your Balance:", penazenka)
            print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
            print("____________________________")
            print("|                          |")
            print("|                          |")
            print("|     |", f1, "|", f2, "|", f3, "|     |")
            print("|                          |")
            print("|                          |")
            print("____________________________")
            if (f1==f2 and f2==f3):
                os.system("cls")
                print("Your Balance:", penazenka,"+",(vklad*3))
                print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                print("____________________________")
                print("|                          |")
                print("|                          |")
                print("|     |", f1, "|", f2, "|", f3, "|     |")
                print("|           win!           |")
                print("|                          |")
                print("____________________________")
                penazenka = penazenka + (vklad * 3)
                input("Press Enter to continue...")
            else :
                input("Press Enter to continue...")
        else:
            if (o1==1):
                f1 = ("\U0001F349")
            if (o1 == 2):
                f1 = ("\U0001F352")
            if (o1 == 3):
                f1 = ("\U0001F34A")
            if (o2==1):
                f2 = ("\U0001F349")
            if (o2 == 2):
                f2 = ("\U0001F352")
            if (o2 == 3):
                f2 = ("\U0001F34A")
            if (o3 == 1):
                f3 = ("\U0001F349")
            if (o3 == 2):
                f3 = ("\U0001F352")
            if (o3 == 3):
                f3 = ("\U0001F34A")
            print("Your Balance:", penazenka)
            print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
            print("____________________________")
            print("|                          |")
            print("|                          |")
            print("|     |", f1, "|", f2, "|", f3, "|     |")
            print("|                          |")
            print("|                          |")
            print("____________________________")
            time.sleep(0.2)
while (True):
    os.system("cls")
    if (penazenka == 0 ):
        print ("No more money \U0001F600")
        time.sleep (3)
        break
    else :

        while True:
            os.system("cls")
            print("Your Balance:", penazenka)
            print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
            try:
                vklad = int(input("Your bet: "))
                if (vklad <= 0):
                    os.system("cls")
                    print ("bet must be higher than 0")
                    time.sleep(0.5)
                    input("Press Enter to continue...")
                    continue
                if vklad > penazenka:
                    os.system("cls")
                    print("Not enough money")
                    time.sleep(0.5)
                    input("Press Enter to continue...")
                    continue
                break
            except ValueError:
                os.system("cls")
                print ("bet must be A NUMBER")
                time.sleep(0.5)
                input("Press Enter to continue...")

        penazenka = penazenka - vklad
        hra(vklad)