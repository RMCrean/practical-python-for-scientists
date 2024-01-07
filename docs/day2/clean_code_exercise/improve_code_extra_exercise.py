"""
This is a bonus exercise.  
"""

# original code
def number_game():
    while True:
        try:
            s = input("Try input something that's not a number: ")
            x = int(s)
            break
        except: 
            print("Try use CTRL-C to exit now")

if __name__ == "__main__":
    number_game() # also fine to write here: "number_game()". 