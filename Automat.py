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
            if (o1==1):
                f1 = ("\U0001F600")
            if (o1 == 2):
                f1 = ("\U0001F352")
            if (o1 == 3):
                f1 = ("\U0001F34E")
            if (o2==1):
                f2 = ("\U0001F600")
            if (o2 == 2):
                f2 = ("\U0001F352")
            if (o2 == 3):
                f2 = ("\U0001F34E")
            if (o3 == 1):
                f3 = ("\U0001F600")
            if (o3 == 2):
                f3 = ("\U0001F352")
            if (o3 == 3):
                f3 = ("\U0001F34E")
            print ("___________________________________")
            print ("|                                 |")
            print ("|                                 |")
            print ("|          ",f1, f2, f3,"             |")
            print ("|                                 |")
            print ("|                                 |")
            print ("___________________________________")
            if (f1==f2 and f2==f3):
                time.sleep(0.2)
                os.system("cls")
                print("___________________________________")
                print("|                                 |")
                print("|                                 |")
                print("|          ", f1, f2, f3, "             |")
                print("|             Výhra               |")
                print("|                                 |")
                print("___________________________________")
                penazenka = penazenka + (vklad * 3)
                print (penazenka)
                time.sleep(3)
            else :
                print (penazenka)
                time.sleep(1.5)
                os.system("cls")
        else:
            if (o1==1):
                f1 = ("\U0001F600")
            if (o1 == 2):
                f1 = ("\U0001F352")
            if (o1 == 3):
                f1 = ("\U0001F34E")
            if (o2==1):
                f2 = ("\U0001F600")
            if (o2 == 2):
                f2 = ("\U0001F352")
            if (o2 == 3):
                f2 = ("\U0001F34E")
            if (o3 == 1):
                f3 = ("\U0001F600")
            if (o3 == 2):
                f3 = ("\U0001F352")
            if (o3 == 3):
                f3 = ("\U0001F34E")
            print("___________________________________")
            print("|                                 |")
            print("|                                 |")
            print("|          ", f1, f2, f3, "             |")
            print("|                                 |")
            print("|                                 |")
            print("___________________________________")
            time.sleep(0.2)
while (True):
    os.system("cls")
    if (penazenka == 0 ):
        print ("nemaaz penaze looool")
        time.sleep (3)
        break
    else :
        print (penazenka)
        vklad =int(input("Kelo Vsádzaš: "))
        while (vklad > penazenka):
            print(penazenka)
            os.system("cls")
            vklad = int(input("Kelo Vsádzaš: "))
        penazenka = penazenka - vklad
        hra(vklad)