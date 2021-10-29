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
        self.include_numbers = string.digits
        self.include_lowercase_characters = string.ascii_lowercase
        self.include_uppercase_characters = string.ascii_uppercase
        self.include_own_symbols = ""
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

    def add_incl_symb(self, symbols):
        """ Add symbols that should be in the password """
        for symbol in symbols:
            self.include_own_symbols += symbol

    def add_excl_symb(self, symbols):
        """ Add symbols that should not be in the password """
        for symbol in symbols:
            self.exclude_symbols.append(symbol)

    def gen_password(self):
        """ Returns the generated password """
        password = ""
        password_kit = self.include_numbers + self.include_lowercase_characters + \
            self.include_uppercase_characters + \
            self.include_symbols + self.include_own_symbols
        while len(password) != self.password_length:
            random_symbol = choice(password_kit)
            if random_symbol in self.exclude_symbols:
                continue
            password += random_symbol
        return password


my_password = Password()
parser = argparse.ArgumentParser(description="Secure password generator")

parser.add_argument("-l", "--lenght", help="password lenght", type=int)
parser.add_argument(
    "--weak", "--easy", help="use only characters and numbers", action="store_true")
parser.add_argument(
    "--strong", "--hard", help="use all punctuation symbols", action="store_true")
parser.add_argument("--include-symbols",
                    help="include symbols that should be in the password")
parser.add_argument("--exclude-symbols",
                    help="exclude symbols that should not be in the password")

args = parser.parse_args()

if args.lenght:
    my_password.set_new_password_length(int(args.lenght))
if args.weak:
    my_password.remove_special_symbols()
if args.strong:
    my_password.add_punctuation_symbols()
if args.include_symbols:
    my_password.add_incl_symb(args.include_symbols)
if args.exclude_symbols:
    my_password.add_excl_symb(args.exclude_symbols)

print(my_password.gen_password())
