# this allows us to use code from
# the open-source pygame libary
# throughout this file

import pygame

def main():
    print("Starting Asteroids!")

# this line ensures the main() function
# is only called when this file is
# run directly; it won't run if it's 
# imported as a module. It's considered the
# "pythonic" way tostructure an executable
# program in Python

if __name__ == "__main__":
    main()
