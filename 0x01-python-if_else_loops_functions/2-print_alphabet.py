#!/usr/bin/python3
"""print the alphabe in lowercase, not followed by a new line."""
for letter in range(97, 123):
    print("{}".format(chr(letter)), end="")
