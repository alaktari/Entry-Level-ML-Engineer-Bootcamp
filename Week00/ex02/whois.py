from sys import argv

if len(argv) > 2:
    print("AssertionError: more than one argument is provided")
elif len(argv) == 2:
    if argv[1].isdigit():
        number = int(argv[1])
        if number == 0:
            print("I'm Zero.")
        elif number % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    else:
        print("AssertionError: argument is not an integer")
