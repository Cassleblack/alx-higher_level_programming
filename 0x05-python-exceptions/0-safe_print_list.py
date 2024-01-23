#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nb = 0

    for n in range(x):
        try:
            print(my_list[n], end="")
            nb += 1
        except IndexError:
            pass
    print()
    return nb
