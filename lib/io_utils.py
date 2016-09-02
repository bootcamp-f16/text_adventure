import os

def clear_screen():
    os.system('clear')

def draw(contents_to_print=None):
    if contents_to_print is not None:
        print(contents_to_print)

def prompt():
    print("")
    return input(">>> ")
