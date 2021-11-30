def game():    
    print("Dit spel is 12+")
    print("How old are you?")
    age = int(input(""))
    if age <= 11:
        allowedAge = False
    if age >= 12:
        allowedAge = True

    if allowedAge != True:
        print("You are not allowed to play this game.")
        exit()

    if not allowedAge == False:
        print("You're allowed to play this game.")

    print("""
    ████████╗██╗░░██╗███████╗  ░██████╗░░█████╗░███╗░░░███╗███████╗
    ╚══██╔══╝██║░░██║██╔════╝  ██╔════╝░██╔══██╗████╗░████║██╔════╝
    ░░░██║░░░███████║█████╗░░  ██║░░██╗░███████║██╔████╔██║█████╗░░
    ░░░██║░░░██╔══██║██╔══╝░░  ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░
    ░░░██║░░░██║░░██║███████╗  ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗
    ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝""")  
    name = input("Type you're username :")
    length = int(input("How tall is ur character in cm? :"))
    if length > 170 and length < 169:
        print("You are quite short, maybe this will come in handy..")
    else:
        print("You are quite tall, maybe this will come in handy..")

    gender = input("Is youre character a man (M) or woman (W)?")
    if gender == 'M' or 'm' or 'W' or 'w':
        print("Nice one!")
    
        
    input("Press enter to start!")
    print("-------")
    print("Character 1 power : Water")
    print("Character 2 power : Fire")
    char1 = input("Welke Character kies je? 1/2? : ")
    if char1 == '1':
        print("-------")
        print("Welcome! U can control the power of water and u live in the Leaf village.")
        print("There is a war and ur helping the other villages : Sand, Mist, Earth and Cloud")
        input("Youre first mission is... press enter.")
        print("-------")
    else:
        print("-------")
        print("Welcome! U can control the power of fire and u live in the Leaf village.")
        print("There is a war and ur helping the other villages : Sand, Mist, Earth and Cloud")
        input("Youre first mission is... press enter.")
        print("-------")

    sand = input("Help defeat the monsters at the Sand village. (1) or the Cloud village! (2) : ")
    if sand == "1":
        print("-------")
        print("Thankyou for coming to the Sand village "+ str(name) + " there is a strong enemy called Zetsu! Can you help us with the fight! ")
        print("Defeat Zetsu (Enemy) ")
    if sand == '2':
        print("-------")
        print("Thankyou for coming to the Cloud village "+ str(name) + " there is a strong enemy called Zetsu! Can you help us with the fight! ")
        print("Defeat Zetsu (Enemy) ")
        input("Press enter to start the fight!")
    print("-------")
    print("Zetsu 10 HP")
    if char1 == '2':
        print("Abilities : 1. Fireball  2. Firepunch")
        fightf = input("Choose the number to use the attack! : ")
        if fightf == '1':
            print("-------")
            print("That was a good hit!")
            print("Zetsu 2 HP left!")       
            print("Zetsu used his Bomb attack!")
            print(str(name) + " 3 HP left.")
            print("-------")
            print("Abilities : 1. Fireball  2. Firepunch")
            fightf1 = input("Choose the number to use the attack! : ")
            if fightf1 == '1':
                print("-------")
                print("That was a good hit!")
                print("Zetsu 0 HP left!")
                print("You have defeated Zetsu!")
                print("-------")
                print("Thank you for helping the village!")
            else:
                print("-------")
                print("That was a good hit!")
                print("Zetsu 0 HP left!")
                print("You have defeated Zetsu!")
                print("-------")
                print("Thank you for helping the village!")
        if fightf == '2':
            print("That was a good hit!")
            print("Zetsu 6 HP left")
            print("Zetsu used his Bomb attack!")
            print(str(name) + " 2 HP left.")
            print("-------")
            print("Abilities : 1. Fireball  2. Firepunch")
            fightf2 = input("Choose the number to use the attack! : ")
            if fightf2 == '1':
                print("-------")
                print("That was a good hit!")
                print("Zetsu 0 HP left!")
                print("You have defeated Zetsu!")
                print("-------")
            if fightf2 == '2':
                print("-------")
                print("That was a good hit!")
                print("Zetsu 0 HP left!")
                print("Zetsu used his Bomb attack again!")
                print("-------")

    if char1 == '1':
        print("Abilities : 1. Waterball 2. Waterpistol")
        fightw = input("Choose the number to use the attack! : ")
        if fightw == '1':
            print("-------")
            print("That was a good hit!")
            print("Zetsu 4 HP left!")  
            print("Zetsu used his Bomb attack!")
            print(str(name) + " 3 HP left.")
            print("-------")
            print("Abilities : 1. Waterball 2. Waterpistol")
            fightw1 = input("Choose the number to use the attack! : ")
            if fightw1 == '1':
                print("-------")
                print("That was a good hit!")
                print("Zetsu 0 HP left!")
                print("You have defeated Zetsu!")
                print("-------")
                print("Thank you for helping the village!") 
            else:
                print("-------")
                print("That was a good hit!")
                print("Zetsu 0 HP left!")
                print("You have defeated Zetsu!")
                print("-------")
                print("Thank you for helping the village!") 
        if fightw == '2':
            print("-------")
            print("That was a good hit!")
            print("Zetsu 3 HP left")
            print("Zetsu used his Bomb attack!")
            print(str(name) + " 3 HP left.")
            print("-------")
            print("Abilities : 1. Waterball 2. Waterpistol")
            fightw2 = input("Choose the number to use the attack! : ")
            if fightw2 == '1':
                print("-------")
                print("That was a good hit!")
                print("Zetsu 0 HP left!")
                print("You have defeated Zetsu!")
                print("-------")
                print("Thank you for helping the village!")
            else:
                print("-------")
                print("That was a good hit!")
                print("Zetsu 0 HP left!")
                print("You have defeated Zetsu!")
                print("-------")
                print("Thank you for helping the village!")
    print(" ")
    home = input("Do you want to stay in this village (1) or go back to you're own village 'The Leaf village' (2) ")
    if home == '2':
        leaf = input("Go home through the Forest (1) or Desert (2) : ")
        if leaf == '1':
            print("-------")
            print("There is a huge rock on the road")
            print("You can destroy the rock with youre abilities!")
            if char1 == '1':
                print("Abilities : 1. Waterball 2. Waterpistol")
                rock = input("Choose the number to use the attack! : ")
                if rock == '1':
                    print("Good hit!")
                    print("It's gone. You can go further.")
                    print("Welcome back home!")
                else:
                    print("Good hit!")
                    print("It's gone. You can go further.")
                    print("Welcome back home!")
            if char1 == '2':
                print("Abilities : 1. Fireball  2. Firepunch")
                rock = input("Choose the number to use the attack! : ")
                if rock == '1':
                    print("Good hit!")
                    print("It's gone. You can go further.")
                    print("Welcome back home!")
                else:
                    print("Good hit!")
                    print("It's gone. You can go further.")
                    print("Welcome back home!")
        if leaf == '2':
            print("-------")
            print("There is a huge rock on the road")
            print("You can destroy the rock with youre abilities!")
            if char1 == '1':
                print("Abilities : 1. Waterball 2. Waterpistol")
                rock = input("Choose the number to use the attack! : ")
                if rock == '1':
                    print("Good hit!")
                    print("It's gone. You can go further.")
                    print("Welcome back home!")
                else:
                    print("Good hit!")
                    print("It's gone. You can go further.")
                    print("Welcome back home!")
            if char1 == '2':
                print("Abilities : 1. Fireball  2. Firepunch")
                rock = input("Choose the number to use the attack! : ")
                if rock == '1':
                    print("Good hit!")
                    print("It's gone. You can go further.")
                    print("Welcome back home!")
                else:
                    print("Good hit!")
                    print("It's gone. You can go further.")
                    print("Welcome back home!")       
    print("-------")
    print("END GAME!")

    if home == '1':
        print("Fun that you're staying here " + str(name) + '!')
        print(" ")
        

    input("Press enter to exit!")
game()
    
            