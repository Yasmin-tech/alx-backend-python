#!/usr/bin/env python3
''' This model contains a type-annotated function to_kv:
    It takes a string k and an int or float v arguments
    returns a tuple. The first element of the tuple is the string k.
    The second element is the square of the int/float v
    and should be annotated as a float in the Tuple.
    '''


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Computes the sum of a list of floating-point numbers and integers.
    '''
    return k, float(v ** 2)
