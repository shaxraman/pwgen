#!/usr/bin/env python

import sys
import string
from random import choice


if sys.version_info < (3, 6, 0):
    sys.stderr.write("You need python 3.6 or later to run this script\n")
    exit(1)


dig = False
dificult = False


def password(length=12, special=False):
    """ Возвращает сгенерированный пароль """
    password = ""
    if special:
        password_kit = string.ascii_letters + string.digits + string.punctuation
    else:
        password_kit = string.ascii_letters + string.digits
    for i in range(length):
        password += choice(password_kit)
    return password


for i in sys.argv[1:]:
    if not i.startswith("-") and i.isdigit():
        dig = int(i)
    if not i.startswith("-") and not i.isdigit():
        dificult = True


if dig and dificult:
    print(password(dig, dificult))
elif dig:
    print(password(dig))
elif dificult:
    print(password(special=dificult))
else:
    print(password())
