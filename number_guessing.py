from random import randint
number_chances = int(input("Enter the number of chances needed to play this game :"))
i=1
score=0 #the score of the game
while i<=number_chances:
    user_input = int(input("Enter the number between 1 and 10 :"))
    random_number = randint(1,10)
    if user_input == random_number:
        print(f"The number you guessed is correct and the number is {user_input}")
        score+=1
    i+=1