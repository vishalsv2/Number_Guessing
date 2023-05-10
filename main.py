import random
from art import logo
print(logo)
print("Welcome To Number Guessing Game")
choice=input("Do You Want to play then type 'Y' otherwise 'N' : ").lower()

if choice=="y":
    level=input("Choose the level type 'Easy' or 'Hard' : ").lower()
    if level=="easy":
        def easy():
            global defined_number
            defined_number=random.randint(1,100)
            game=True
            loop=10
            while game and loop>0:
                global number
                number = int(input("Guess the between 1 to 100 : "))
                if defined_number==number:
                    print ("You Win, Your Guess is Right")
                    game=False
                else:
                    if number>defined_number:
                        print("Your Guess is Too High")
                    elif number<defined_number:
                        print("Your Guess is Too Low")
                    elif number==defined_number:
                        game=False
                    loop-=1
                print(f"you will have remaining {loop} attempts ")
        easy() 
        if defined_number!=number:
            print("You Lost ") 

    elif level=="hard":
        def hard():
            global defined_number
            defined_number=random.randint(1,5)
            game=True
            loop=5
            while game and loop>0:
                global number
                number = int(input("Guess the between 1 to 100 : "))
                if defined_number==number:
                    print ("You Win, Your Guess is Right")
                    game=False
                else:
                    if number>defined_number:
                        print("Your Guess is Too High")
                    elif number<defined_number:
                        print("Your Guess is Too Low")
                    elif number==defined_number:
                        game=False
                    loop-=1
                print(f"you will have remaining {loop} attempts ")
        hard()  
        if defined_number!=number:
            print("You Lost ")  
    else:
        print("Invalid Input")

elif choice =="n":
    print("Thank you")
else:
    print("Invalid Input")
        


        