#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    print_count = 0
    try:
        for elem in my_list:
            if (x > 0):
                print("{:d}".format(elem),  end="")
                x = x-1
                print_count = print_count + 1
        print()
    except Exception as err:
        print("An error happened: ", err)
    else:
        return print_count
