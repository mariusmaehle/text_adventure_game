"""
docstring:

Created by: Marius Heje Mæhle

1) IntroductionPUT INTRO AND PRUPOSE OF THE GAME HERE!

    You have to travel across the desert at Tatooine to find him.
    The dessert is filled with Tusken Raiders, dangerous animals and other unknown dangers.

2) Known bugs/errors: none
"""

print("""Lost in the dessert at Tatooine
 - A Star Wars Adventure\n
""")

import time #time() function returns the number of seconds passed since last function
import random #import random contains things to do with random number generation
#from sys import exit - not used
import sys #import exit function from system

#make the visuals cleaner with seperation function
def pretty_print():
    print("-------------------------------------------------------------------------------------------")

#lost and exit function
def you_lost():
    option = input("You lost the game, would you like to try again? (yes/no) ")
    while option != "yes" or option != "no":
        if option == "yes":
            choose_path()
        elif option == "no":
            sys.exit("Thank you for playing")
        else:
            print("Please enter a valid command\n")
            option = input("Would you like to try again? (yes/no) ")

def print_c3po(username):
    print("\n\n")
    print(r"    /~\    Nice to make your acquaintance " + username)
    print(r"   (O O) _/")
    print(r"    \=/ ")
    print(r"  /  _  \  ")
    print(r" //|/.\|\\ ")
    print(r"||  \_/  || ")
    print(r"|| |\ /| || ")
    print(r" # \_ _/ # ")
    print(r"   | | |  ")
    print(r"   | | |  ")
    print(r"   []|[]  ")
    print(r"   | | |    ")
    print(r"  /_]_[_\ ")

def print_boba():
    print(r"           |~")
    print(r"           |.---.")
    print(r"          .'_____`. /\ ")
    print(r"          |~xxxxx~| ||")
    print(r"          |_  #  _| ||")
    print(r"     .------`-#-'-----.")
    print(r"    (__|\_________/|.`.")
    print(r"     /  | _______ | | |")
    print(r"    /   |/   |   \| | |")
    print(r"   /   /X|  _|_  |/ `.|")
    print(r"  (  --< \\/    \//| |`.")
    print(r"  `.    ~----.-~=====,:=======")
    print(r"    ~-._____/___:__(``/| |")
    print(r"      |    |      XX|~ | |")
    print(r"       \__/======| /|  `.|")
    print(r"       |_\|\    /|/_|    ) ")


def slow_text(text, timer=0.1):
    count = 0
    while count < len(text):
        print(text[count], end="")
        time.sleep(timer)
        count += 1

def captured_tuskens_path():
    print("sadas")


#### Stage 0 - The Desert at Tatooine - Start of the game ####
def start():
    pretty_print()
    slow_text("Well, hello there!\n\n", 0.12)
    print("""  
    You are a Jedi traveling with Obi-Wan Kenobi in the Millenium Falcon. 
    The mission is to find Anakin Skywalker, and bring him to the Jedi Temple to train him. 
    You arrive at the planet Tatooine in the city of Mos Eisley. \n\n""")
    pretty_print()
    name_input = input("Please enter your name to start the adventure Master Jedi: ")
    username = "Master Jedi "

    #capitalize the name input and bind it together with username jedi
    username += name_input.capitalize()
    print_c3po(username)
    slow_text("My name is C-3PO, and I will be joining you through this adventure.")

    input("Press enter to start the adventure " + username)
    choose_path()

#### Stage 1 - Bounty Hunter Boba Fett ####
def choose_path():
    pretty_print()
    print("""
   Rumors says that Skywalker is in the city of Mos Espa on the other side of the desert. 
   As you walk into the desert a bounty hunter tries to attacks you.\n
   1. Fight him with your light saber 
   2. Negotatite a deal with him
   3. Run away\n""")
    print_boba()

    option = input("Choose wisely: \n")

    if  option == "1"  or  option == "fight" or option == "one":
        print("""You fight the bounty hunter, and strike him with the lightsaber.
        He falls into the Great Pit of Carkoon, and dissapears into the monster Sarlac.""")
        input("Press enter to continue further into the desert")
        old_tusken_camp_path()
        print("Done with old tusken camp")

    elif option == "2" or option == "Negotiate" or option == "negotiate" or option == "deal":
        print("The bounty hunter is not exactly on talking terms, but you manage to stay alive.\n")
        input("Press enter to continue the battle")
        choose_path()

    elif option == "3" or option == "run" or option == "away":
        print("""The bounty hunter is catching up to you, and you are not able to fight back in time.""")
        you_lost()
    else:
        print("These aren’t the droids you’re looking for. Please try again")
        input("Press enter to continue the adventure")
        choose_path()

#### Stage 2 - Tusken Raiders ####
def old_tusken_camp_path():
    pretty_print()
    print("""
    As the bounty hunter is now gone, and you are heading the right way on the map, 
    you see that someone is watching you from top of the hills - Tusken Raiders!\n
    As they are closing in they surround you in the valley.\n
    1. Fight them with a light saber
    2. Get C-3PO to negotiate a deal with them
    3. Try to outmanoeuvre and escape them\n""")

    option = input("Choose wisely: \n")

    if  option == "1"  or  option == "fight" or option == "light saber":
        print("There are to many off them, and you lose the fight, and your life.")
        you_lost()

    elif option == "2" or option == "Negotiate" or option == "negotiate" or option == "deal":
        print("""Good choice. Tusken Raiders like valueable assets. 
        C-3PO translates for you, and you manage to make a deal with them for credits.""")
        input("Press enter to leave the desert, and enter the city of Mos Espa")
        pretty_print()
        make_offer_to_watto()

    elif option == "3" or option == "outmanoeuvre" or option == "escape":
        print("Tuskens are Tatooine's natives and you have no chance, and get captured. ")
        captured_tuskens_path()

    else:
        print("These aren’t the droids you’re looking for. Please try again")
        input("Press enter to continue the adventure")
        choose_path()

#### Stage 3 - Mos Espa to make a deal with Watto
def make_offer_to_watto():
    acceptable_amount = False
    print("""You find Anakin Skywalker in the city, who is owned by the junker dealer Watto.\n
    Watto is greedy, and as a Jedi you don't have a lot of money to offer. 
    Luckly Yoda gave you 100 credits for "lunch" money\n""")
    make_bribe = input('Credits is a commodity that is not easy to come by, would you like to offer some of your credits to save Anakin? (yes/no)\n')
    if(make_bribe == '1' or make_bribe == 'yes'):
        while not acceptable_amount:
            value = input('How much are you willing to offer?\n')
            try:
                value = int(value)
            except ValueError:
                print ('The value you entered is invalid. Please make sure you enter a numeric value\n')
                continue

            acceptable_amount = True
            if value >= 75 and value <= 100:
                print("""
                Congratulations, you saved Anakin Skywalker. Mission completed! 
                You fly away in the Millenium Falcon with a new Jedi Apprentice,
                Anakin Skywalker.\n""")
            elif value > 100:
                print("Watto is no fool, and he knows you don't have that kind of money.")
            else:
                print('Oh no, what are we going to do?\n')

    else:
        print("""That's not the Jedi way, and it won't save Anakin's life\n""")
        you_lost()

start()