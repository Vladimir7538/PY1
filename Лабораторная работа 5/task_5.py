from random import sample
from string import hexdigits


def get_random_password(n=8) -> str:
    str_ = "".join(sample(hexdigits, n))
    return str_


print(get_random_password())
