
from pytimedinput import timedInput


userText = timedInput("Please, do enter something: ")

if(userText):
    print('Time is up')
else:
    print(f"User-input: '{userText}'")