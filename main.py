import random

def restart():
    restart = input('Do you want to restart? yes/no : ')
    if restart.lower() == 'no':
        print('Ok then!')
        print('Random Number Guesser Shutting down...')
    if restart.lower() == 'yes':
        main()

def main():
    name = input('Hello! What is your name? : ')
    print('Nice to meet you ' + name + '!')
    print('Ok Then Lets Start!')
    numbers = input('How many numbers do you want there to be in the game? : ')
    number = random.randint(0, int(numbers))

    for i in range(int(numbers)):
        guess_number = input('Your Guess : ')
        if int(guess_number) > number:
            print('Guess too high!')
        if int(guess_number) < number:
            print('Guess too low!')
        if int(guess_number) == number:
            print('Yay you did it! You Guessed the number!')
            print('yeah, thats the end of the game and I hope you enjoyed! Bye!')
            restart()
            break
    if int(guess_number) != number:
        print('You ran out of guesses!')
        print('Yeah, thats the end of the program and I hope you enjoyed! Bye!')
        restart()
main()

