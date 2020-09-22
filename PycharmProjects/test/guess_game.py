from random import randint

def play():
    random_int = randint(0, 100)

    while True:
        user_guess = int(input("what number did we guess (0-100)?"))

        if user_guess == randint:
            print(f"You find the number ({random_int}). Congrats!")
            break

        if user_guess < random_int:
            print("Your number is less than the number we guessed.")
            continue

        if user_guess > random_int:
            print("Your number is more than the number we guessed.")
            continue


if __name__ == '__main__':
    play()
