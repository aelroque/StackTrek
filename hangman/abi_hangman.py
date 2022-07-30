from random import choice
from Words import words
from hangman_visual import lives_visual_dict
import string
from time import sleep, time

#Greetings & User input
print("\n")
print("""                  w e l c o m e  t o
            █░█ ▄▀█ █▄░█ █▀▀ █▀▄▀█ ▄▀█ █▄░█
            █▀█ █▀█ █░▀█ █▄█ █░▀░█ █▀█ █░▀█
                       g a m e
""")

name = input("Enter your name>> ").upper()
print(f"""Great Day! {name}! 
 
    TO PLAY:
    The computer will randomly chooses a word.
    Guess the letters in the word by typing your letter of choice.
    You were given 30 seconds to guess the word and a limited guesses to 7.
    
    Tease your brain. Enjoy the game. BEST OF GUESS!
    """)
sleep(1)

def get_valid_word(words):
    word = choice(words) #randomly chooses word from the list
    while "-" in word or " " in word:
        word = choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letter = set()
    lives = 7
    
    # timer = 30
    # start_time = time()
    #getting user input
    while len(word_letters) > 0 and lives > 0:

        #letter used
        print(f"You have {lives} lives left.\nLetters used >> ", " ".join(used_letter))
        #current word
        word_list = [letter if letter in used_letter else "-" for letter in word]
        print(lives_visual_dict[lives])
        print("Current word >> ", " ".join(word_list))
        

        
        user_letter = input("Guess Letter >> ").upper()
        if user_letter in alphabet - used_letter:
            used_letter.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("")
            else:
                lives = lives - 1 
                print(f"Your letter {user_letter} is not in the word.")
        elif user_letter in used_letter:
            print(f"You have already used that letter. Guess another letter. ")
        else:
            print("That is not a valid letter. ")

        
    if lives == 0:
        print(lives_visual_dict[lives])
        print(f"""
        ╔═╗╔═╗╔╦╗╔═╗      ╔═╗╦  ╦╔═╗╦═╗
        ║ ╦╠═╣║║║║╣       ║ ║╚╗╔╝║╣ ╠╦╝
        ╚═╝╩ ╩╩ ╩╚═╝  is  ╚═╝ ╚╝ ╚═╝╩╚═ 
           the word was {word}.
        """)
        play_again()
        
    else:
        print(f""" 
                ╦  ╦╦╔═╗╔╦╗╔═╗╦═╗╦ ╦  ┬
                ╚╗╔╝║║   ║ ║ ║╠╦╝╚╦╝  │
                 ╚╝ ╩╚═╝ ╩ ╚═╝╩╚═ ╩   o
                 the word is {word}.
    """)
    # end_time = time()
    # time_rem = end_time - start_time
    # if time_rem > timer:
    #     print("Time is up")
        play_again()

    
def play_again():
    while input("Play again? y | n >> ").lower() == "y":
        hangman()
    else:
        print("\nNICE PLAY! THANK YOU!\n")

hangman()