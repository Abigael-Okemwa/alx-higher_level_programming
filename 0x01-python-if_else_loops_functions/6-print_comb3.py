#!/usr/bin/python3
# Author - Tolulope Fakunle

for digita in range(0, 10):
    for digitb in range(digita + 1, 10):
        if digita == 6 and digitb == 7:
            print("{}{}".format(digita, digitb))
        else:
            print("{}{}".format(digita, digitb), end=", ")
