import argparse

"""
    self.password_length = password_length
    self.include_symbols = "!?@#$%^&*()-+=~_"
    self.include_own_symbols = ""
    self.include_numbers = string.digits
    self.include_lowercase_characters = string.ascii_lowercase
    self.include_uppercase_characters = string.ascii_uppercase
    self.exclude_symbols = []  # ( { } [ ] ( ) / \ ' " ` ~ , ; : . < > )
"""

parser = argparse.ArgumentParser()

parser.add_argument("-l", "--lenght", default=16, help="password lenght", type=int)
args = parser.parse_args()

print(args.lenght)