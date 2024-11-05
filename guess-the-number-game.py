import random
import sys

print('Input two numbers, minimum number and maximum number. First, input the minimum number: ')
sys.stdout.flush()
min_num = int(sys.stdin.readline())
print('The minimum number you entered is ' + str(min_num) + '. Now, input the maximum number: ')
sys.stdout.flush()
max_num = int(sys.stdin.readline())

while max_num <= min_num:
    print('The maximum number should be greater than the minimum number. Please input the maximum number again: ')
    sys.stdout.flush()
    max_num = int(sys.stdin.readline())

random_num = random.randint(min_num, max_num)
print('The maximum number you entered is ' + str(max_num) + '. Now, guess the number between ' + str(min_num) + ' and ' + str(max_num) + ': ')
sys.stdout.flush()
guess_num = int(sys.stdin.readline())

while guess_num != random_num:
    if guess_num < random_num:
        print('The number is greater than ' + str(guess_num) + '. Guess again: ')
    else:
        print('The number is less than ' + str(guess_num) + '. Guess again: ')
    sys.stdout.flush()
    guess_num = int(sys.stdin.readline())

print('Congratulations! You guessed the number ' + str(random_num) + ' correctly!')
