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

number_game()


## solution:
def number_game():
    while True:
        try:
            s = input("Input a number: ")
            x = int(s)
            break
        except ValueError: # Exception:  # still better to use ValueError
            print("Not a number, try again")
number_game()


# ## solution v2:
# def number_game():
#     while True:
#         try:
#             s = input("Input a number: ")
#             x = int(s)
#             break
#         except ValueError: # Exception:  # still better to use ValueError
#             print("Not a number, try again")

# def main():
#     number_game()

# if __name__ == "__main__":
#     main() # also fine to write here: "number_game()". 