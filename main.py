# this allows us to use code from
# the open-source pygame libary
# throughout this file
import pygame

# import everything from the module
# constants.py into the current file
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

# this line ensures the main() function
# is only called when this file is
# run directly; it won't run if it's 
# imported as a module. It's considered the
# "pythonic" way tostructure an executable
# program in Python
if __name__ == "__main__":
    main()
