#!/usr/bin/python3
# Author - Bamidele Adefolaju
s = 0
for d in range(ord('z'), ord('a') -1, -1):
    print("{}".format(chr(d - s)), end="")
    s = 32 if s == 0 else 0
