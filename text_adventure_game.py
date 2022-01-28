"""
docstring:

    Created by: Marius Heje Mæhle

1) A Star Wars Text Adventure Game

    Introduction
    The game is based on the Star Wars Saga, and is taking place at the sand planet Tatooine.
    You are a Master Jedi looking for young Anakin Skywalker, which is said to be strong with The Force.
    Your mission is to travel across the desert to find him, and bring him back to the Jedi Temple.

    Round 0: Starting point - Landing in the city of Mos Eisley
    Round 1: Fighting a Bounty Hunter
    Round 2: Confront Tusken Raiders
    Round 3: Enter Mos Espa and make a deal with Watto

    Most of the input from the user is number, unless something else is specified.

    May The Force be with you, always!

2) Known bugs/errors:
    None
"""

#create headline for the text adventure game
print("""Lost in the dessert at Tatooine
         - A Star Wars Adventure\n
""")

import time #time() function returns the number of seconds passed since last function
import sys #import exit function from system

#make the visuals cleaner with seperation function, and input in when needed
def pretty_print():
    print("----------------------------------------------------------------------------")

#lost and exit function
def you_lost():
    option = input("You lost the game, would you like to try again? (yes/no) ")
    while option != "yes" or option != "no":
        if option == "yes":
            start() #jump all the way back to start
        elif option == "no":
            sys.exit("Thank you for playing!")
        else:
            print("Please enter a valid command\n")
            option = input("Would you like to try again? (yes/no) ")


#create ASCII art with of C3PO with text and username
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

#create ASCII art of the bounty hunter Boba Fett
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

#create variabel with slow text, and timer
def slow_text(text, timer=0.1):
    count = 0
    while count < len(text):
        print(text[count], end="") #the end function makes the word appears horizontal, and not vertical
        time.sleep(timer) #use the time.sleep to make the letters appear one at the time
        count += 1 #the += adds the two values together and assigns the final value to a variable


#### Stage 0 - The Desert at Tatooine - Start of the game ####
def start():
    pretty_print()
    slow_text("Well, hello there!\n\n", 0.12) #use slow text and edit the timer speed
    print("""  
    You are a Jedi traveling with Obi-Wan Kenobi in the Millenium Falcon. 
    The mission is to find Anakin Skywalker, and bring him to the Jedi Temple for training. 
    You arrive at the planet Tatooine in the city of Mos Eisley. \n\n""")
    pretty_print()
    name_input = input("Please enter your name to start the adventure Master Jedi: ") #enter the username to make it more personal
    username = "Master Jedi "

    #capitalize the name input and bind it together with username jedi
    username += name_input.capitalize() #capitalize the name in the input function and add the name_input to Master Jedi
    print_c3po(username) #print the ASCII of c3po with the input username
    slow_text("My name is C-3PO, and I will be joining you on this adventure.") #slow text from C3PO

    input("Press enter to start the adventure " + username)
    choose_path() #enter stage 1

#### Stage 1 - Bounty Hunter Boba Fett ####
def choose_path():
    pretty_print()
    print("""
   Rumors says that Skywalker is in the city Mos Espa on the other side of the desert. 
   As you walk into the desert a bounty hunter tries to attacks you.\n
   1. Fight him with your light saber 
   2. Negotiate a deal with him
   3. Run away\n""")
    print_boba() #print the ASCII of the bounty hunter Boba Fett

    option = input("Choose wisely: \n") #input option

    #add if statment for the stage
    if  option == "1"  or  option == "fight" or option == "one": #have a wider range of input option for the player
        print("""
    You fight the bounty hunter, and strike him with the lightsaber.
    He falls into the Great Pit of Carkoon, and dissapears into the monster Sarlac.\n""")
        input("Press enter to continue further into the desert")
        old_tusken_camp_path() #move to the next stage

    elif option == "2" or option == "negotiate" or option == "two" or option == "deal":
        print("The bounty hunter is not exactly on talking terms, but you manage to stay alive.\n")
        input("Press enter to continue the battle")
        choose_path() #go back to the same stage again

    elif option == "3" or option == "run" or option == "three":
        print("""The bounty hunter is catching up to you, and you are not able to fight back in time.""")
        you_lost() #lost
    else:
        print("""
        These aren’t the droids you’re looking for.
        Please try again and enter with number 1, 2, or 3.""")
        input("Press enter to continue the adventure")
        choose_path() #go back to the same stage again because of invalid input

#### Stage 2 - Tusken Raiders ####
def old_tusken_camp_path():
    pretty_print()
    print("""
    As the bounty hunter is now gone, and you are heading the right way on the map. 
    You see that someone is watching you from the hillside - Tusken Raiders!
    As they are closing in, they surround you in the valley.\n
    1. Fight them with a light saber
    2. Get C-3PO to translate, and negotiate a deal for credits
    3. Try to outmanoeuvre and escape\n""")

    option = input("Choose wisely: \n")  #input option

    if  option == "1"  or  option == "fight" or option == "light saber": ##have a wider range of input option for the player
        print("There are to many off them, and you lose the fight, and your life.")
        you_lost() #you lost and have to start the game again

    elif option == "2" or option == "Negotiate" or option == "negotiate" or option == "deal":
        print("""
    Good choice. Tusken Raiders like valueable assets. 
    C-3PO translates for you, and you manage to make a deal.\n""")
        input("Press enter to leave the desert, and enter the city of Mos Espa.")
        make_offer_to_watto() #move on to the next stage

    elif option == "3" or option == "outmanoeuvre" or option == "escape":
        print("As Tuskens are Tatooine's natives you have no chance, and you're captured. ")
        input("Maybe there still is a chance the Tusken Raiders will negotiate a deal?\n\nPress enter to try again\n")
        old_tusken_camp_path()  #you lost and have to start the game again

    else:
        print("""These aren’t the droids you’re looking for.\n""")
        input("Press enter to continue the adventure")
        choose_path() #if none of the right options are used, you will be sent back to the question again

#### Stage 3 - Mos Espa to make a deal with Watto
def make_offer_to_watto():
    pretty_print()
    acceptable_amount = False
    print("""
    You find Anakin Skywalker, who is owned by the junker dealer Watto.
    Watto is greedy, and as a Jedi you don't have a lot of money to offer. 
    Luckly Yoda gave you extra 100 credits for lunch money.\n""")
    make_bribe = input("""
    Credits is a commodity that is not easy to come by.
    Would you like to offer credits to save Anakin? (yes/no)\n""") #make the variable to a a yes or no answer
    if make_bribe == '1' or make_bribe == 'yes': #continues the game
        while not acceptable_amount: #While not loop repeatedly execute the loop until the condition for the loop is met.
            value = input('How much are you willing to offer?\n')
            try:
                value = int(value) #makes the input option to a integer
            except ValueError:
                print ('The value you entered is invalid. Please make sure you enter a numeric value\n') #if the input has the wrong value
                continue

            acceptable_amount = True #if the acceptable amount is correct
            if value >= 75 and value <= 100: #acceptable amount is between or equal to 75 and 100
                print("Mission completed! The Force is strong with this one.\n")
                you_win() #you win
            elif value > 100: #you only had 100 credits
                print("Watto is no fool, and he knows you don't have that kind of money.")
                make_bribe() #returns to the bribe stahe
            else:
                print("The Force knows Anakin is worth more then that.\n")
                input("Press enter to go again, and make Watto an offer he cannot refuse.")
                make_offer_to_watto() #return to the

    elif make_bribe == '2' or make_bribe == 'no': #if the bribe is not confirmed
        print("""A Master Jedi knows the risk. That won't save Anakin.\n""")
        you_lost() #lost
    else:
        print("""
    Oh no, too bad you didn't offer any credits. 
    Jedi mind tricks won't work on Watto.\n""")
        input("Please press enter to continue dealing with Watto")
        make_offer_to_watto() #return to the same stage

#define the winning function and exit the game
def you_win():
    print("""
    Congratulations, you saved Anakin Skywalker. 
    You fly away in the Millenium Falcon with the new Jedi Apprentice.\n""")
    input("Thank you for using The Force with love.\n\nPress enter to exit, Master Jedi") #seperate the lines with \n
    exit(0) #exit the game

start() #start function