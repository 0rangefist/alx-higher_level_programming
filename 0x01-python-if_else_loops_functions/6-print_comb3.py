#!/usr/bin/python3
count = 0
for i in range(0, 10):
    for j in range(0, 10):
        count = count = i * 10 + j
        if i < j:
            print("{}{}".format(i, j),  end=", " if i * 10 + j < 89 else "\n")
