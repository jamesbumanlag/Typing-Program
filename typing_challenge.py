import random
import time
import os
from pytimedinput import timedInput

# function to clear the screen everytime the program starts
# it is also compatible to windows and macos
def clear_screen():
    if os.name == 'NT':
        os.system('cls')
    else:
        os.system('clear')

# create a funtion that randomly select a word from the python list of words
# assign the random word to the variable random_word
def ran_word():
    py_words_list = ('len','print','max','min','sum','list','dict','str','int','float','def')
    random_word = random.choice(py_words_list)
    return random_word

# define function to calculate time
def elapsed_time(start_timer,end_timer):
    # Calculate minutes and seconds
    elapsed_time_seconds = end_timer - start_timer
    minutes, seconds = divmod(elapsed_time_seconds, 60)
    # convert to int to eliminate float value
    print(f'Duration is {int(minutes)} min : {int(seconds)} seconds')

# create a time limit function and return its value
def time_limit(timer_start, timer_end):
    timer = timer_end - timer_start
    min_ , sec_ = divmod(timer,60)
    return sec_

# create a function that will validate the user input and check if the input is correct    
def main():
    lives = 5
    correct = 0
    wrong = 0
    time_up = 0
    
    # program loop will start here
    while lives > 0:
        print()
        random_word = ran_word()

        # start the time for the time limit
        timer_start = time.time()
        print(f'Chances: {lives}')
        user_word = timedInput(f'Type the word: {random_word} \n>> ')
        
        # timer limit ends
        # timer_end = time.time()
        # limit = int(time_limit(timer_start,timer_end))

        # this block statement is to set time limit to 5 sec
        if user_word:
            print('Time is up')
            lives -= 1
            time_up += 1
            wrong += 1
            continue

        # check the input if it is correct 
        if user_word == random_word:
            print()
            correct = correct + 1
            print(f'Good Job you got the word {random_word}')
            print(f'Correct: {correct}')
            
            lives  -= 1
            
            continue

        # if the input is wrong   
        else:
            wrong = wrong + 1
            print('Wrong')
            print(f'Wrong answer: {wrong}')
            lives = lives - 1
            continue

    # timer duration ends here
    end_timer = time.time()
   

    print()
    
    # this block statement will set wrong to zero even if it has negative result
    if wrong >=0:
        wrong = 0
    score = correct - wrong

    # display the results
    print(f'Score: {score}\nCorrect: {correct}\nWrong:{wrong} \nTime-up: {time_up}')
    elapsed_time(start_timer,end_timer)


# start of the main program       
clear_screen()
# duration timer starts here
start_timer = time.time()

if __name__ == '__main__':
    main()

