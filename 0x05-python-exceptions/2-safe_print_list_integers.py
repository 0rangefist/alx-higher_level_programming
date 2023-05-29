#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    if not isinstance(my_list, list):
        print()
        return 0
    print_count = 0
    for elem in my_list:
        if (x > 0):
            try:
                print("{:d}".format(elem),  end="")
                x = x-1
                print_count = print_count + 1
            except Exception:
                pass
    print()
    return print_count
