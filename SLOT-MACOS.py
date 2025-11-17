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
        os.system("clear")
        o1 = random.randrange(1, 4)
        o2 = random.randrange(1, 4)
        o3 = random.randrange(1, 4)
        if (i==9):
            if (o1 == 1):
                f1 = ("\U0001F349")
            if (o1 == 2):
                f1 = ("\U0001F352")
            if (o1 == 3):
                f1 = (" 7")
            if (o2 == 1):
                f2 = ("\U0001F349")
            if (o2 == 2):
                f2 = ("\U0001F352")
            if (o2 == 3):
                f2 = (" 7")
            if (o3 == 1):
                f3 = ("\U0001F349")
            if (o3 == 2):
                f3 = ("\U0001F352")
            if (o3 == 3):
                f3 = (" 7")
            print("ALPHA RELEASE")
            print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
            print("Your Balance:", penazenka)
            print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
            print("____________________________")
            print("|       SLOT MACHINE       |")
            print("|     _____ ____ _____     |")
            print("|     |", f1, "|", f2, "|", f3, "|     |")
            print("|     ‾‾‾‾‾ ‾‾‾‾ ‾‾‾‾‾     |")
            print("|                          |")
            print("____________________________")
            if (o1==3 and o2==3 and o3==3):
                print("ALPHA RELEASE")
                print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                print("Your Balance:", penazenka, "+", (vklad * 6))
                print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                print("____________________________")
                print("|       SLOT MACHINE       |")
                print("|     _____ ____ _____     |")
                print("|     |", f1, "|", f2, "|", f3, "|     |")
                print("|     ‾‾‾‾‾ ‾‾‾‾ ‾‾‾‾‾     |")
                print("|         JACKPOT!         |")
                print("____________________________")
                penazenka = penazenka + (vklad * 6)
                input("Press Enter to continue...")
            elif (f1==f2 and f2==f3):
                os.system("clear")
                print("ALPHA RELEASE")
                print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                print("Your Balance:", penazenka,"+",(vklad*3))
                print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                print("____________________________")
                print("|       SLOT MACHINE       |")
                print("|     _____ ____ _____     |")
                print("|     |", f1, "|", f2, "|", f3, "|     |")
                print("|     ‾‾‾‾‾ ‾‾‾‾ ‾‾‾‾‾     |")
                print("|           WIN!           |")
                print("____________________________")
                penazenka = penazenka + (vklad * 3)
                input("Press Enter to continue...")
            else :
                os.system("clear")

                print("ALPHA RELEASE")
                print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                print("Your Balance:", penazenka)
                print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                print("____________________________")
                print("|       SLOT MACHINE       |")
                print("|     _____ ____ _____     |")
                print("|     |", f1, "|", f2, "|", f3, "|     |")
                print("|     ‾‾‾‾‾ ‾‾‾‾ ‾‾‾‾‾     |")
                print("|          LOOSE!          |")
                print("____________________________")
                input("Press Enter to continue...")
        else:
            if (o1 == 1):
                f1 = ("\U0001F349")
            if (o1 == 2):
                f1 = ("\U0001F352")
            if (o1 == 3):
                f1 = (" 7")
            if (o2 == 1):
                f2 = ("\U0001F349")
            if (o2 == 2):
                f2 = ("\U0001F352")
            if (o2 == 3):
                f2 = (" 7")
            if (o3 == 1):
                f3 = ("\U0001F349")
            if (o3 == 2):
                f3 = ("\U0001F352")
            if (o3 == 3):
                f3 = (" 7")
            print("ALPHA RELEASE")
            print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
            print("Your Balance:", penazenka)
            print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
            print("____________________________")
            print("|       SLOT MACHINE       |")
            print("|     _____ ____ _____     |")
            print("|     |", f1, "|", f2, "|", f3, "|     |")
            print("|     ‾‾‾‾‾ ‾‾‾‾ ‾‾‾‾‾     |")
            print("|                          |")
            print("____________________________")
            time.sleep(0.2)
while (True):
    os.system("clear")
    if (penazenka == 0 ):
        print ("No more money \U0001F600")
        time.sleep (3)
        break
    else :

        while True:
            os.system("clear")
            print("ALPHA RELEASE")
            print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
            print("Your Balance:", penazenka)
            print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
            try:
                print ("Type 0 to exit or ")
                vklad = int(input("Enter your bet: "))
                if (vklad == 0):
                    exit()
                if (vklad < 0):
                    os.system("clear")
                    print ("bet must be higher than 0")
                    time.sleep(0.5)
                    input("Press Enter to continue...")
                    continue
                if vklad > penazenka:
                    os.system("clear")
                    print("Not enough money")
                    time.sleep(0.5)
                    input("Press Enter to continue...")
                    continue
                break
            except ValueError:
                os.system("clear")
                print ("bet must be A NUMBER")
                time.sleep(0.5)
                input("Press Enter to continue...")

        penazenka = penazenka - vklad
        hra(vklad)