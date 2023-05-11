#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv) - 1
    sum = 0
    if argc == 0:
        print("{}".format(argc))
    else:
        for i in range(1, argc + 1):
            sum = sum + int(sys.argv[i])
        print("{}".format(sum))
