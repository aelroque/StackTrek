#QUIZ_GAME |SOFTWARE ENGINEERING related topic| Abigael R. Roque | Date: July 2022
#Simplest form #reduction of correct and wrong message
#Tools used: list, function, if-else, random.shuffle(), lower(), lower(), \n, for loop, f string,sleep()
#To-Do: Insert label - Question 1 to 10, random number used as the number of item to be answered,

#Libraries used
from Question import questions
from random import shuffle
from time import sleep
from math import floor

def introduction():
    #player input / name input
    player_name = input("\nEnter your name? >> ").upper()
    print(f"Nice to meet you, {player_name}!") #string format
    sleep(0.5) # suspend execution for a period of time
    #Decision of the user
    print("""                                        welcome to
                                        ██████  ██    ██ ██ ███████ 
                                       ██    ██ ██    ██ ██    ███  
                                       ██    ██ ██    ██ ██   ███   
                                       ██ ▄▄ ██ ██    ██ ██  ███    
                                        ██████   ██████  ██ ███████ 
                                            ▀▀ game | SOFTWARE ENGINEERING

    Multiple-choice:
    /..\ The level of difficulty determines the set of questions randomly prepared for you. 
    (\/) You may choose from easy, medium, and hard.
    |__| Select the best answer and type the letter of choice in the space provided.
    'uu' Let those neurons work!!! Good luck!
    """)

    answer = input("Type A to proceed >> ").upper() #all input is converted to uppercase
    sleep(0.4)

def quiz(questions): 
    shuffle(questions)
    print()
    #randomly choose set a, set b, set c
    user_input = input("""
                      CHOOSE LEVEL OF DIFFICULTY
                        Easy   | 10 questions 
                        Medium | 20 question
                        Hard   | 30 questions \n\nEnter the word: """).lower()
    if user_input == "easy":
        sublist_of_questions = questions[:10]
    elif user_input == "medium":
        sublist_of_questions = questions[:20]
    elif user_input == "hard":
        sublist_of_questions = questions[:30]
    
    print("Loading questionnaires...")
    sleep(0.8)

    score = 0
    total_question = len(sublist_of_questions)
    count = 0
    for question, answer in sublist_of_questions:
        count += 1
        print(f"\nQuestion {count}                             |{count} out of {total_question}|")
        user_letter = input(question)
        # if user_letter != answer:
        #     print("  Invalid input.\n")
        if user_letter.lower() == answer.lower():
            print("  You got it right!\n")
            sleep(0.3)
            score += 1
        else:
            print("  Add to your review list\n")
            sleep(0.3)
    
    print("-----------------------E-N-D--O-F--Q-U-I-Z-----------------------")
    sleep(1)
    rating = floor((score/total_question)*100)
    print(f""" 
             ^ ^              
            (O,O) Score: {score}/{total_question}
            (   ) Rating: {rating}%
            -"-"--------------
          """)
    
    return score

def running_game():
    display_question = quiz(questions)
    play_again()

def play_again():
    ask_player = input("Try again? Y or N >> ").lower()
    if ask_player == "y":
        running_game()
    else:
        print(""" 
                ╔╗ ╔═╗╔═╗╔╦╗  ╔═╗╔═╗  ╦  ╦ ╦╔═╗╦╔═  ┬
                ╠╩╗║╣ ╚═╗ ║   ║ ║╠╣   ║  ║ ║║  ╠╩╗  │
                ╚═╝╚═╝╚═╝ ╩   ╚═╝╚    ╩═╝╚═╝╚═╝╩ ╩  o
                        COME BACK AGAIN!
              """)

# ---- main ----
introduction()
running_game()
