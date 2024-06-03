import random
import os

hangman = ['''   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|\\  |
       |
      ===''', '''
   +---+
   O   |
  /|\\  |
   |   |
      ===''', '''
   +---+
   O   |
  /|\\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\\  |
  / \\  |
      ===''']

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'

animal_words = ["elephant", "tiger", "lion", "giraffe", "zebra", "cheetah",
                "hippo", "rhinoceros", "gorilla", "penguin", "crocodile", "snake", "monkey",
                "leopard", "panda", "kangaroo", "emu", "platypus"]

shape_words = ["Square", "Triangle", "Rectangle", "Circle", "Ellipse", "Rhombus", "Trapezoid", 
               "Hexagon", "Octagon", "Pentagon", "Sphere", "Cube", "Cylinder", "Cone", "Pyramid"]

place_words = ["Cairo", "London", "Paris", "Baghdad", "Istanbul", "Riyadh",  "Tokyo", "Beijing", "Moscow", "Dubai", "Sydney", "Rome", 
               "Berlin", "Madrid", "Mumbai", "Singapore", "Bangkok", "Istanbul", "Seoul", "Athens", "Amsterdam", "Vienna", "Prague"]
word_list = ["elephant", "tiger", "lion", "giraffe", "zebra", "cheetah", "hippo", "rhinoceros", "gorilla", "penguin", "crocodile", "snake", "monkey", "leopard", "panda", "kangaroo", "emu", "platypus",
             "Square", "Triangle", "Rectangle", "Circle", "Ellipse", "Rhombus", "Trapezoid", "Hexagon", "Octagon", "Pentagon", "Sphere", "Cube", "Cylinder", "Cone", "Pyramid",
             "Cairo", "London", "Paris", "Baghdad", "Istanbul", "Riyadh", "Tokyo", "Beijing", "Moscow", "Dubai", "Sydney", "Rome", "Berlin", "Madrid", "Mumbai", "Singapore", "Bangkok", "Istanbul", "Seoul", "Athens", "Amsterdam", "Vienna", "Prague"]

def get_rand_word(word_list):
    return random.choice(word_list)

def display_menu():
    print("Hangman Game - Difficulty Levels")
    print("1. Easy")
    print("2. Moderate")
    print("3. Hard")

def select_level(level):
    global max_missed
    global secret_word
    global word_list

    if level == 'Easy':
        set_choice = input("Select a set (Animal, Shapes, Places): ").lower()
        if set_choice == 'animal':
            word_list = animal_words
        elif set_choice == 'shapes':
            word_list = shape_words
        elif set_choice == 'places':
            word_list = place_words
        else:
            print("Invalid set choice.")
            return

        max_missed = 6
    elif level == 'Moderate':
        word_list = random.choice([animal_words, shape_words, place_words])  # Added for Moderate level
        max_missed = 5
    elif level == 'Hard':
        word_list = random.choice([animal_words, shape_words, place_words])  # Added for Hard level
        max_missed = 3

    secret_word = get_rand_word(word_list)

player_name = input("Enter your name: ")

os.system("clear")

display_menu()
level_choice = input("Choose a level (Easy, Moderate, Hard): ").capitalize()
select_level(level_choice)

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

print(bcolors.UNDERLINE + f"{' '.join(alphabet)}\n" + bcolors.ENDC)

screen = []
guessed = []
game_over = False
counter = 0

for _ in range(len(secret_word)):
    screen += "_"

print(bcolors.OKBLUE + f"\t\t{' '.join(screen)}" + bcolors.ENDC)

while not game_over:
    guess_a_word = input("\nGuess a letter: ").lower()

    os.system("clear")

    if guess_a_word in guessed:
        print(bcolors.FAIL + f"\t\tYou already guessed '{guess_a_word}'!" +  bcolors.ENDC)
    elif guess_a_word not in guessed:
        if guess_a_word not in secret_word.lower():
            counter += 1
        guessed += guess_a_word

    for point in range(len(secret_word)):
        letter_in_word = secret_word[point]
        if guess_a_word == letter_in_word.lower():
            screen[point] = letter_in_word

    print(bcolors.OKBLUE + f"\t\t{' '.join(screen)}" + bcolors.ENDC)
    print(bcolors.OKCYAN + hangman[counter] + bcolors.ENDC)

    if counter == max_missed:
        game_over = True
        print(bcolors.FAIL + f"\n\n-------YOU LOST!--------\n" + bcolors.ENDC)
        print(bcolors.FAIL + f"The answer was --->  " + bcolors.ENDC + bcolors.OKGREEN + f"{secret_word}\n" + bcolors.ENDC)

    if "_" not in screen:
        game_over = True
        print(bcolors.HEADER + "\n\nCongratulations!\nYOU WON THE GAME :)\n" + bcolors.ENDC)
