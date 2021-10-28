#!/usr/bin/python3

import sys
import string
from random import choice


if sys.version_info < (3, 6, 0):
    sys.stderr.write("You need python 3.6 or later to run this script\n")
    exit(1)


class Password:
    def __init__(self, password_length: int = 16) -> None:
        self.password_length = password_length
        self.include_symbols = "!?@#$%^&*()-+=~_"
        self.include_own_symbols = ""
        self.include_numbers = string.digits
        self.include_lowercase_characters = string.ascii_lowercase
        self.include_uppercase_characters = string.ascii_uppercase
        self.exclude_symbols = []  # ( { } [ ] ( ) / \ ' " ` ~ , ; : . < > )

    def add_punctuation_symbols(self):
        """ Set new include_symbols - !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ """
        self.include_symbols = string.punctuation

    def set_new_password_length(self, digital: int):
        """ Set new password length """
        self.password_length = digital

    def password(self):
        """ Returns the generated password """
        password = ""
        password_kit = self.include_numbers + self.include_lowercase_characters + \
            self.include_uppercase_characters + \
            self.include_symbols + self.include_own_symbols
        for i in range(self.password_length):
            if i in self.exclude_symbols:
                continue
            password += choice(password_kit)
        return password


my_password = Password()

for i in sys.argv[1:]:
    if not i.startswith("-") and i.isdigit():
        my_password.set_new_password_length(int(i))
    if not i.startswith("-") and not i.isdigit():
        my_password.add_punctuation_symbols()

print(my_password.password())
