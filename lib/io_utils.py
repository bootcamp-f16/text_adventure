import os

def clear_screen():
    os.system('clear')

def draw(contents_to_print=""):
    print(contents_to_print)

def prompt():
    print("")
    return input(">>> ")
