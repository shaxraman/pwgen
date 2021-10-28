#!/usr/bin/python3

import sys
import string
from random import choice
import argparse

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

    def remove_special_symbols(self):
        """ Remove special symbols - !?@#$%^&*()-+=~_ """
        self.include_symbols = ""

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
parser = argparse.ArgumentParser()

parser.add_argument("-l", "--lenght", help="password lenght", type=int)
parser.add_argument(
    "--weak", "--easy", help="use only characters and numbers", action="store_true")
parser.add_argument(
    "--strong", "--hard", help="use all punctuation symbols", action="store_true")

args = parser.parse_args()

if args.lenght:
    my_password.set_new_password_length(int(args.lenght))
if args.weak:
    my_password.remove_special_symbols()
if args.strong:
    my_password.add_punctuation_symbols()

print(my_password.password())
