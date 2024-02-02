import random
print("bot:i am thinking of a number!")
secretnumber=random.randint(1,10)
attempts=0
while True:
    guess= int(input("guess a number:"))
    attempts=1
    if guess==secretnumber:
        print("Congrats")
    elif guess>secretnumber:
        print("bot:try for a higher number!")
print("bot:try for a lower number!")