
import string
from sys import argv


def text_analyzer(parameter=""):
    if parameter == "":
        parameter = input("What is the text to analyze?\n>> ")
    printableChars = sum(c.isprintable() for c in parameter)
    uppers = sum(c.isupper() for c in parameter)
    lowers = sum(c.islower() for c in parameter)
    punctuation_count = sum(c in string.punctuation for c in parameter)
    spaces = sum(c.isspace() for c in parameter)

    print("The text contains", printableChars, "printable character(s):")
    print("-", uppers, "upper letter(s)")
    print("-", lowers, "lower letter(s)")
    print("-", punctuation_count, "punctuation mark(s)")
    print("-", spaces, "space(s)")


if len(argv) != 2:
    print("Error: one argument is provided")
else:
    text_analyzer(argv[1])
