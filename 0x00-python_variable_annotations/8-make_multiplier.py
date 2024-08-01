#!/usr/bin/env python3
''' This model contains the type-annotated function make_multiplier.
    It takes an argument multiplier and
    return a function that squares the multiplier.
    '''


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    ''' return the Callable function '''
    def inner_function(x: float) -> float:
        ''' This is the function that should be returned '''
        return float(multiplier * x)
    return inner_function
