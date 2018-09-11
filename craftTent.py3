#!/usr/bin/env python
# -*- coding: utf-8 -*-
#------------------------------------------------
# 'Crafting Challenge' Game
# More programs at UsingPython.com/programs
#------------------------------------------------

#------------------------------------------------
# Challenge 1: Can you craft a namiot and a palenisko?
# Challenge 2: Can you add more items?
# Challenge 3: Can you create crafting rules
#                   to make more items?
# Challenge 4: Add comments to the code below!
#------------------------------------------------

commands = {
                "i" : "pokaż co masz w skrzyni",
                "c" : "pokaż co można zbudować",
                "zrób [przedmiot]" : "zrób coś z przedmiotów znajdujących się w skrzyni",
           }

#an inventory of items
items = {
            "krzesiwo" : 50,

            "trawa" : 100,
            "siano" : 0,

            "drzewo" : 100,
            "kłoda" : 0,

            "drzewko" : 100,
            "gałązka" : 0,

            "głaz" : 30,
            "skała" : 0,

            "kilof" : 0,
            "siekiera" : 0,

            "palenisko" : 0,
            "namiot" : 0,

            "pochodnia" : 0,
        }

#rules to make new objects
craft = {
            "siano" : { "trawa" : 1 },
            "gałązka" : { "drzewko" : 1 },
            "kłoda" : { "siekiera" : 1, "drzewo" : 1 },
            "siekiera" : { "gałązka" : 3, "krzesiwo" : 1 },
            "namiot" : { "gałązka" : 10, "siano" : 15 },
            "palenisko" : { "głaz" : 5, "kłoda" : 3, "gałązka" : 1, "pochodnia" : 1 },
            "pochodnia" : { "krzesiwo" : 1, "trawa" : 1, "gałązka" : 1 },
            "kilof" : { "krzesiwo" : 2, "gałązka" : 1 }
        }


print("*****************************************")
print("*          ZBUDUJ I PRZEŻYJ             *")
print("*****************************************")
print("Przeróbka gry z  UsingPython.com/programs")
print("-----------------------------------------\n")


print("Spróbuj przeżyć budując namiot i miejsce")
print("na ognisko czyli 'palenisko'.")
print("Napisz '?' aby zobaczyć pomoc")

while True:

    command = input(":").split()

    if len(command) == 0:
        continue

    if len(command) > 0:
        verb = command[0].lower()
    if len(command) > 1:
        item = command[1].lower()

    if verb == "?":
        for key in commands:
            print(key + " : " + commands[key])
        print("\n")

    elif verb == "i":
        for key in items:
            print(key + " : " + str(items[key]))
        print("\n")

    elif verb == "c":
        for key in craft:
            print(key + " można zrobić z:")

            for i in craft[key]:
                print(str(craft[key][i]) + " " + i)

            print("\n")
            
    elif verb == "zrób":

        print("robisz " + item + ":") 
        if item in craft:

            for i in craft[item]:
                print("  potrzebujesz : " + str(craft[item][i]) + " " + i + " a masz " + str(items[i]))

            canBeMade = True

            for i in craft[item]:
                if craft[item][i] > items[i]:
                    print("Ta rzecz nie może być zrobiona\n")
                    canBeMade = False
                    break
            
            if canBeMade == True:
                for i in craft[item]:
                    items[i] -= craft[item][i]

                items[item] += 1

                print("Rzecz gotowa\n")


            if items["namiot"] >= 1 and items["palenisko"] >= 1:
                print("\n**BRAWO! UDAŁO CI SIĘ PRZEŻYĆ!\nDOBRE DZIECKO!")
                break

        else:
            print("Nie możesz")

    else:
        print("Nie możesz")
