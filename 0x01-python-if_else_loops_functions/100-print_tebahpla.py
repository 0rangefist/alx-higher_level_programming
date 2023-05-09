#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    # lowercase z is ascii 122(even number)
    # convert odd number ascii to upper case
    print('{}'.format(chr(i) if i % 2 == 0 else chr(i - 32)), end='')
