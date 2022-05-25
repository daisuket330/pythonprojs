from random import randrange
from xxlimited import foo

def main():
    number = randrange(10)
    while True:
        try:
            guess = int(input(" ?"))
        except ValueError:
            continue
        if guess == number:
            print("You win!")
            break
        else:
            print("try again")

if __name__ == '__main__' :
    main()

