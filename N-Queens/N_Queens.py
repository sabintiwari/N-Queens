import sys

#main method tha executes the program
def main(args):
    #take the n value which is args[1]
    if len(args) == 2 and is_int(args[1]):
        print("peform")
    else:
        print("The program takes exactly one integer argument for the number of queens.")
    print(args)

#Returns True if the value is an integer, else returns False
def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

#Call the main method with arguments
main(sys.argv)