import random

# random numbers between 1 - 10
# random_number = random.randint(1, 10)
# guess = None

# while guess != random_number:
#     # must be inside the while loop
#     guess = input("pick a number from 1 to 10: ")
#     guess = int(guess)
#
#     if guess < random_number:
#         print("Too Low!, Answer is " + str(random_number))
#     elif guess > random_number:
#         print("Too High!! " + str(random_number))
#         guess = input("pick a number from 1 to 10: ")
#         guess = int(guess)
#     else:
#         print("You got it!")
#     break


# using while true
random_number = random.randint(1, 10)

while True:
    # must be inside the while loop
    guess = input("pick a number from 1 to 10: ")
    guess = int(guess)

    if guess < random_number:
        print("Too Low!, Answer is " + str(random_number))
    elif guess > random_number:
        print("Too High!! Answer is " + str(random_number))
    else:
        print("You got it!")
        play_again = input("Do you want to play again? (y/n)")
        if play_again == "y":
            random_number = random.randint(1, 10)
            guess = None
        else:
            print("Thank you for playing:")
            break