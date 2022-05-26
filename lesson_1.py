import random


def main():
    while True:
        random_number = random.randint(0, 10)
        user_number = int(input("Enter number "))

        if user_number == random_number:
            print("You win!")
        else:
            print("You lose!")

        answer = input("Do you want to play again? (y/n) ")

        if answer == "y":
            continue
        elif answer == "n":
            break


if __name__ == "__main__":
    main()