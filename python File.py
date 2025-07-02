import random
number = random.randint(1,10)
tries = 0
print("Guess the number (1 to 10)")
while True:
    guess = int(input("Your guess: "))
    tries +=1
    if guess == number:
        print(f'Correct! you guess it in {tries} tries.')
        break
    elif guess < number:
        print('Too low')
    else:
        print('Too high')
