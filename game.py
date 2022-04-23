"""
Welcome to my first python project!

This is made with the help of the Codecademy team!
Great site ! Does guys know what they are doing ;) 

This is an simple quiz game. Don't judge me to hard :D 

Start of the project: 22/04/2022

--------------------------------------------------------------------------------------------------
What is this game?

A text- based adventure in a fantasy world ! 
It's like a short D&D thing :) 

"""
# imports
import keyboard

# Classes
class Player:
    def __init__(self, name, race, class_player, description):
        self.race = race
        self.class_player = class_player
        self.description = description
        self.name = name


# Functions
def makePlayer():
    print("Welcome, brave adventurer !")
    print("Can you type your name for me?")
    name = input()
    print("What race are you?")
    print("Choose between \"Dragonborn\", \"Elf\", \"Dwarf\" or \"Human\"")
    race = input()
    print("Which Class do you want to be?")
    print("Choose between \"Paladin\", \"Rogue\", \"Cleric\", \"Mage\" or \"Warrior\"")
    class_player = input()
    print("How would you describe yourself?")
    description = input()

    player = Player(name, race, class_player, description)
    print("Welcome {name} !".format(name=player.name))
    print("You are ready to go on an adventure !") 


def entry():
    print("Welcome to your Adventure!")
    print("This is still a work in progress ;) ")
    print("You can only make a player character now, but later we can go on an adventure!")
    print("Press \"SpaceBar\" to continue...")
    keyboard.wait("spacebar")
    makePlayer()
 
def gameStory():
    print("You walk out of a cave.")
    print("You look around you...")


#The Start of the progam
entry()