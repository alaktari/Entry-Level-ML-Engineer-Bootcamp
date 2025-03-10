from sys import argv

if len(argv) > 1 :
    merged_params = ((" ".join(argv[1:])) [::-1]).swapcase()
    print(merged_params)