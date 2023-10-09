import time
import threading
from playsound import playsound
def bgMusic():
  playsound('bg_m.ogg')
music_thread = threading.Thread(target=bgMusic)
music_thread.start()
def theStory(text, t_speed=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(t_speed)
    print()
def intro(theStory):
    theStory('In the mystical land of Eldoria, a legend has been passed down.')
    theStory('You are a brave adventurer in search of the Lost Legacy treasure.')
    time.sleep(2)
    start_game(theStory)
def start_game(theStory):
    theStory('You stand at the entrance of the Enigma Forest.')
    theStory('Wich path will you choose?')
    theStory('1. Follow the winding river depper into the forest.')
    theStory('2. Venture into the dark cave entrance to your left.')
    choice = input()
    if choice == '1':
        follow_river(theStory)
    elif choice == '2':
        enter_cave(theStory)
    else:
        theStory('Invalid choice. Please enter "1" or "2".')
        start_game(theStory)
def follow_river(theStory):
    theStory('You decide to follow the winding river.')
    theStory('As you go deeper into the forest, it becomes denser and more ominous...')
    theStory('What will you do?')
    theStory('1. Continue following the river.')
    theStory('2. Leave the river and cut through the dense underbrush.')
    choice = input()
    if choice == '1':
        discover_journal(theStory)
    elif choice == '2':
        find_statue(theStory)
    else:
        theStory('Invalid choice. Please enter "1" or "2".')
        follow_river(theStory)   
def enter_cave(theStory):
    theStory('With brave heart, you enter the dark cave.')
    theStory('The air is dump, and the walls seem to close in around you...')
    theStory('What will you do?')
    theStory('1. Press on further into the cave.')
    theStory('2. Decide to retreat and return to the forest\'s entrance.')
    choice = input()
    if choice == '1':
        discover_cave_chest(theStory)
    elif choice == '2':
        start_game(theStory)
    else:
        theStory('Invalid choice. Please enter "1" or "2".')
        enter_cave(theStory)
def discover_journal(theStory):
    theStory('You continue following the river and discover a mysterious journal.')
    theStory('It appears to be a journal with writings and drawings.')
    theStory('What will you do?')
    theStory('1. Examine the journal closely.')
    theStory('2. Ignore the journal and continue deeper into the forest.')
    choice = input()
    if choice == '1':
        theStory('The journal contains clues that lead you to the treasure!')
        theStory('Congrats! You have found the Lost Leagacy!')
        end_game(theStory)
    elif choice == '2':
        theStory('You continue depper into the forest but nothing of interest.')
        follow_river(theStory)
    else:
        theStory('Invalid choice. Please enter "1" or "2".')
        discover_journal(theStory)
def find_statue(theStory):
    theStory('Leaving the river, you cut through the dense underbrush.')
    theStory('You stumble upon a hidden glade with an ancient statue and inscription.')
    theStory('What will you do?')
    theStory('1. Inspect the statue and its inscription.')
    theStory('2. Leave the glade and head back to the river.')
    choice = input()
    if choice == '1':
        theStory('The inscription reveals a clue about the trasure\'s location!')
        theStory('Congrats! You have found the Lost Legacy!')
        end_game(theStory)
    elif choice == '2':
        theStory('You leave the glade and return to river.')
        follow_river(theStory)
    else:
        theStory('Invalid choice. Please enter "1" or "2".')
        find_statue(theStory)
def discover_cave_chest(theStory):
    theStory('You brave the cave\'s darkness and continue deeper.')
    theStory('You emerge into cavern bathed in an eerie blue light.')
    theStory('In the center of the cavern, you find a chest with mystical symbols.')
    theStory('What will you do?')
    theStory('1. Approach the chest cautiously.')
    theStory('2. Leave the cavern and head back to the forest.')
    choice = input()
    if choice == '1':
        theStory('The chest contains the Lost Legacy treasure!')
        theStory('Congrats! You have found the Lost Legacy!')
        end_game(theStory)
    elif choice == '2':
        theStory('You leave the cavern and return to the forest.')
        start_game(theStory)
    else:
        theStory('Invalid choice. Please enter "1" or "2".')
        discover_cave_chest(theStory)
def end_game(theStory):
    theStory('Congratulations, you have successfully found the Lost Legacy treasure!')
    theStory('Thank you for playing!')
    exit()
intro(theStory)