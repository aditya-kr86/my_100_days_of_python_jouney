import random
import ascii_art
def random_num_guess():
    print(ascii_art.logo)
    # print("Welcome to the number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    choose_level = input("Type '{e}asy' or '{h}ard' : ").lower()
    random_number = random.randint(1,100)
    # print(random_number)
    if choose_level == "e":
        no_of_attemepts = 10
    elif choose_level == "h":
        no_of_attemepts = 5
    for i in range(no_of_attemepts):
        print(f"You have {no_of_attemepts - (i)} attements remaining guess the number")
        guessed_no = int(input("Make a Guess : "))
        if guessed_no < 1 and guessed_no > 100:
            print("Kindly Choose a Number between 1 and 100.")
        if guessed_no == random_number:
            print(ascii_art.won)
            end_or_not = input("Enter {e}nd the Game or {c}ontinue : ")
            if end_or_not == 'e':
                print("Thanks for Playing Number Guessing Game")
                break
            else:
                random_num_guess()
        elif guessed_no > random_number:
            print("Too High")
            if i < no_of_attemepts-1:
                print("guess again")
        elif guessed_no < random_number:
            print("Too Low")
            if i < no_of_attemepts-1:
                print("guess again")
    else:
        print(ascii_art.loose)
        end_or_not = input("Enter {e}nd the Game or {c}ontinue : ")
        if end_or_not == 'e':
            print("Thanks for Playing Number Guessing Game")
            # break
        else:
            random_num_guess()
if __name__ == "__main__":
    random_num_guess()
