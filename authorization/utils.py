from random import choices
from string import ascii_uppercase, digits


def rand_str():
    return ''.join(choices(f'{ascii_uppercase}{digits}', k=100))
