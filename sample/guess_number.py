import random

correct_answer = random.randint(1,100)
print(correct_answer)

guess_right = False

small, large = 1, 100

while not guess_right:

    print(f"{small} < ? < {large}")
    my_guess = int(input("Enter your guess: "))

    if my_guess == correct_answer:
        print("BINGO")
        guess_right = True

    elif my_guess < correct_answer:
        print(f"{my_guess} is smaller, guess larger")
        small = my_guess

    elif my_guess > correct_answer:
        print(f"{my_guess} is larger, guess smaller")
        large = my_guess

    

