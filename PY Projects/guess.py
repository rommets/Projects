import random
def guessing_by_us():
    choosen_num=random.randint(1,1000)
    flag=True
    while flag:
        user_guess=int(input("Guess a number berween 1 and 1000: "))
        if user_guess<(choosen_num-200):
            print("much higher")
        elif (user_guess-200)>choosen_num:
            print("much lower")
        elif user_guess<choosen_num:
            print("higher")
        elif user_guess>choosen_num:
            print("lower")
        elif user_guess==choosen_num:
            print("prost <3")
            flag=False
guessing_by_us()
# -----------------------------------
import time
def guessing_by_computer():
    print("Choose your random number in your head...")
    time.sleep(5)
    low=1
    high=1000
    flag=True
    while flag:
        our_guess=random.randint(low,high)
        print(our_guess)
        user_input=input("is your number higher(h) or lower(l) or correct(c)? ")
        if user_input.lower()=="l": 
            high=our_guess-1
        elif user_input.lower()=="h":
            low=our_guess+1
        elif user_input.lower()=="c":
            print("Prost <3")
            flag=False

    
guessing_by_computer() 



