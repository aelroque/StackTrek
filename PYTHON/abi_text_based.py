#Text_based word game | Slam book based themed
#Tools: list, dictionary, function, 
#Libraries: random.choice, random.shuffle, random.radint
from random import choice
from random import shuffle
from random import randint
from time import sleep
import os

def next_activity():
    sleep(0.5)
    print("""
                MINI GAMES: 
                            MUSIC | MOVIE | HOBBY | FOOD | MOOD 
                            NAME | AGE | NUMBER | NOTHING | EXIT
        
        Choose then type the word. """)
    
    activity = input("\nNext thing to do: >> ").lower()
    if activity == "music":
        music()
    elif activity == "movie":
        movies()
    elif activity == "hobby":
        hobby()
    elif activity == "food":
        food()
    elif activity == "mood":
        mood()
    elif activity == "name":
        name()
    elif activity == "number":
        number()
    elif activity == "age":
        age()
    elif activity == "nothing":
        nothing()
    else:
        print("\nCOME BACK AGAIN, OKAY?\n")


def my_self():
    print("""
                    **** ME, MYSELF AND I ****
                       SLAM BOOK INSPIRED
                      Getting to know you. 
          """)
    player = input("\nEnter your name: ").title()
    player_gender = input("Male | Female | Prefer not to say \nType 'M' or 'F' or 'P' >> ").upper()
    player_count = len(player)
    chat_bot = ["Silent","Bee","Sting",]
    bot_od = choice(chat_bot)

    if player_gender == "F":
        f = "Ms."
        print(f"\n>>> Hi {f} {player}! I am {bot_od} your friendly coder.") #to add more information
        print(f">>> Just saying. You may want to know that your name has {player_count} characters.\n")
    elif player_gender == "M":
        m = "Mr."
        print(f"\n>>> Hi {m} {player}! I am {bot_od} your friendly coder.")
        print(f">>> Just saying. You may want to know that your name has {player_count} characters.\n")
    else:
        print(f"\n>>> Hi Mr./Ms. {player}! I am {bot_od} your friendly coder.")
        print(f">>> Just saying. You may want to know that your name has {player_count} characters.\n")
    #other personal information
    sleep(0.5)
    next_activity()

def nothing():
    print("""
                            **** IDLE TIME **** 
                        But do remember every seconds count.
                            """)
    n = int(input("Enter number from 1 - 50: "))
    n1 = n
    for i in range(1, n1):
        print("Count ", n1)
        sleep(1)
        n1 -= 1
    print(f"\nOpps... I've wasted {n} seconds of your time.\n")
    play_again= input("Try again? Type y | n >> ").lower()
    if play_again == "y":
        nothing()
    else:
        print("Goodbye for now!\n")
        next_activity()

def age():
    print("""
                    **** PLAYFUL DAYS ****
        Answer what is asked and let see what the date tells about it. 
          """)
    day = int(input("Day of birth: "))
    month = str.casefold(input("Month of birth: ")).upper()
    year = int(input("Year of birth: "))
    month1 = month.upper()
    
    if year % 12 == 8:
        animal = "Dragon"
    elif year % 12 == 9:
        animal = "Snake"
    elif year % 12 == 10:
        animal = "Horse"
    elif year % 12 == 11:
        animal = "Sheep"
    elif year % 12 == 0:
        animal = "Monkey"
    elif year % 12 == 1:
        animal = "Rooster"
    elif year % 12 == 2:
        animal = "Dog"
    elif year % 12 == 3:
        animal = "Pig"
    elif year % 12 == 4:
        animal = "Rat"
    elif year % 12 == 5:
        animal = "Ox"
    elif year % 12 == 6:
        animal = "Tiger"
    elif year % 12 == 7:
        animal = "Hare"
    
    print(f"\nBIRTHDAY | {day} {month1} {year}")
    print("\n%d is the year of the %s." % (year, animal))
    print()
    
    play_again= input("Try again? Type y | n  >> ").lower()
    if play_again == "y":
        age()
    else:
        print("Goodbye for now!\n")
        next_activity()

def name():
    
    print("""
                    **** NAME GAME ****
                    LOVE ME, LOVE ME NOT

            Enter the name of a person that is important to you.
            I will tell you if he/she loves you or not.
          """)
    
    crush_name = input("Enter a name: ").title()
    crush_count = len(crush_name)
    if crush_count % 2 >= 1:
        print(f"{crush_name} loves you not!\n")
    else:
        print(f"{crush_name} loves you!\n")
    
    play_again= input("Try again? Type y | n >> ").lower()
    if play_again == "y":
        name()
    else:
        print("Goodbye!\n")
        next_activity()

def number():
    
    print("""
                    **** BET ME NOT ****
                    LOTTO INSPIRED GAME

            Make a bet by entering your lucky numbers.
            The computer will display the lotto game of the day,
            and generate the winning numbers.
                  6/58 | 6/55 | 6/49 | 6/45 | 6/42
            You will enter your 6 betting numbers. Good Luck!
          """)
    ans = input("Bet on your numbers? Press enter to continue")
    lotto = [58, 55, 49, 45, 42]
    lotto_game = choice(lotto)
    print(f"\nLOTTO GAME: 6/{lotto_game}\n")
    x = [int(x) for x in input("Enter 6 numbers followed by comma >> ").split(",")]
    x_sort = sorted(x)
    lotto_num = []
    for i in range(0, 6):
        win_num = randint(1, lotto_game)
        lotto_num.append(win_num)
        lotto_num_sort = sorted(lotto_num)
    if lotto_num_sort == x_sort:
        print(f"\nYOUR NUMBERS ARE: {x}")
        sleep(0.5)
        print(f"\nLOTTO WINNING NUMBERS : {lotto_num}")
        sleep(0.5)
        print("\nYOU WON THE PRICE!")

    print(f"\nYOUR NUMBERS ARE: {x}")
    sleep(0.9)
    print(f"\nLOTTO WINNING NUMBERS : {lotto_num}")
    sleep(0.2)
    print("\nSorry. Better luck next time.\n")
        
    
    play_again= input("Try again? Type y | n >> ").lower()
    if play_again == "y":
        number()
    else:
        print("Goodbye!\n")
        next_activity()

def music():
    print(""" 
                    **** GENRE MATCH UP ****
                Try to match the computer's genre.
          """)
    genre_of_music = ["Rock", "Classical", "Hip-Hop", "Pop", "Jazz", "Country", "Instrumental", "Metal", "Lofi", "Ballad","Alternative","Sentimental"]
    print("""
          ROCK | CLASSICAL | HIP-HOP | POP | JAZZ | COUNTRY
          INSTRUMENTAL | METAL | LOFI | BALLAD| ALTERNATIVE | SENTIMENTAL
          """)
    player_music = input("Music your listening to: >> ").title()
    genre_of_music.append(player_music)
    comp_music = choice(genre_of_music)
    if player_music == comp_music:
        print(f"We both like {player_music} genre.\n")

    else:
        print(f"Your genre: {player_music}\nComputer genre: {comp_music}\n")

    play_again= input("Try again? Type y | n >> ").lower()
    if play_again == "y":
        music()
    else:
        print("Nice choice of song. Goodbye!\n")
        next_activity()

def movies():
    print(""" 
                    **** WATCH OUT ****
                Pretend that the computer is your crush. 
                Share your favorite genre of movies and the computer will try to match yours.
                
                ACTION | HORROR | COMEDY | THRILLER | SCI-FI | ROMANCE
                    DOCUMENTARY | ADVENTURE | MUSICAL | FANTASY
          """)
    genre_of_movies = ["Action", "Horror", "Comedy", "Thriller", "Sci-Fi", "Romance", "Documentary", "Adventure", "Musical", "Fantasy"]
    player_movie = input("Genre of movies >> ").title()
    genre_of_movies.append(player_movie)
    crush_movie = choice(genre_of_movies)
    
    if player_movie == crush_movie:
        print(f"You love watching {player_movie} movie. Your crush also like {crush_movie} movies.")
    else:
        print(f"You love watching {player_movie}. However, your crush like {crush_movie} movies.")
     
    play_again= input("\nTry again? Type y | n >> ").lower()
    if play_again == "y":
        movies()
    else:
        print("Thrilling! But your leaving! Bye for now.\n")
        next_activity()

def food():
    print(""" 
                    **** HEAR YOU BURRRRPPPP ****
                The computer is your chef. Match the menu of the day.
                If you guess it right, I will host you DINNER by CANDLE.
                If not, DELIVERY is on the way.
                
                FRENCH | ITALIAN | CHINESE | JAPANESE | FILIPINO | GREEK
                SPANISH | MEDITERRANEAN | LEBANESE | MOROCCAN | TURKISH
                KOREAN | THAILAND 
          """)
    
    cuisine = ["French","Italian","Chinese","Japanese","Filipino","Greek","Spanish","Mediterranean","Lebanese","Moroccan","Turkish","Korean","Thai",]
    like_food = input("Guess the MENU OF THE DAY? >> ")
    computer_food = choice(cuisine)
    if like_food == computer_food:
        print("Let us have a candle dinner.")
    else:
        print("For delivery. Thank you.")

    play_again= input("\nTry again? Type y | n >> ").lower()
    if play_again == "y":
        food()
    else:
        print("Heard a loud burp. Happy to hear that! Keep safe!\n")
        next_activity()

def hobby():
    print(""" 
                    **** INDOOR OR OUTDOOR ****
                Let us do what you want. Burn or break.
                
                COOKING | DANCING | GARDENING | WRITING | SHOPPING
                GAMES | PHOTOGRAPHY | LEARNING | PAINTING | ACTING
          """)
    hobbies = ["Cooking","Dance","Gardening", "Writing","Shopping","Games","Photography","Learning","Painting","Acting"]
    user_hobby = input("Your favorite past time? >> ").title()
    computer_hobby = shuffle(hobbies)
    computer1 = choice(hobbies)
    if computer1 == user_hobby:
        print(f"I am correct! Your hobby is {computer_hobby}.")
    else:
        print(f"My guess is {computer1}.")
        print(f"{user_hobby}! Why is it so hard to guess your hobby.")
       

    play_again= input("\nTry again? Type y | n >> ").lower()
    if play_again == "y":
        hobby()
    else:
        print("Happy moment! Nice try myself.\n")
        next_activity()

def mood():
    mood_list =["anxious","depressing","foreboding","happy","hopeless","in love","joyful","melancholic","panicked","pessimistic","romantic","stressed","calm","eerie","frightening","humorous","ominous","peaceful","reflective","sad","tense","cheerful","festive","frustrated","idyllic","lonely","optimistic","pensive","restless","sentimental","uneasy"]
    
    print(""" 
                    **** MOOD SWINGS ****
                Tell me how you feel and I will try to match your feelings.""")
    sleep(0.5)
    print("""
                    HOW ARE YOU TODAY?
                    
        ANXIOUS | DEPRESSING | FOREBODING | HOPELESS | JOYFUL
        MELANCHOLIC | PANICKED | PESSIMISTIC | ROMANTIC | STRESSED 
        CALM | EERIE | FRIGHTENING | HUMUROUS | OMINOUS | 
        PEACEFUL | REFLECTIVE | SAD | TENSE | CHEERFUL
        FESTIVE | FRUSTRATED | IDYLLIC | LONELY | OPTIMISTIC
        PENSIVE | RESTLESS | SENTIMENTAL | UNEASY
        """)
    
    feel = input("Choose a word: >> ")
    match = choice(mood_list)
    if feel == match: 
        print(f"How come we feel {match}?")
    else:
        print(f"I'm sorry, you were feeling {feel}! However, I feel {match}.\n")

    play_again= input("\nTry again? Type y | n >> ").lower()
    if play_again == "y":
        mood()
    else:
        print("Happy moment! Nice try myself.\n")
        next_activity()

my_self()