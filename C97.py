import random
print("Number Guessing game")
number=random.randint(1,9)
chances=0

print("Gues a number (between 1 and 9):")
while chances<5:
    
    guess=int(input("Enter Your Guess:-"))
    if guess==number:
        print("CONGRATULATIONS YOU WON!")
        break
    elif guess<number:
        print("Your guess was too low: Guess a number higher than",guess)
    else:
        print("Your guess was too high: Guess a number lower than",guess)
    chances += 1
    if not chances<5:
        print("COME ON! The number was",number)
