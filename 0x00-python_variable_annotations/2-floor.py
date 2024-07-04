#!/usr/bin/env python3
''' This model contains the type-annotated function floor:
    takes a float n as it argument
    and return the floor
    '''

from math import floor as f


def floor(n: float) -> int:
    ''' return the floor of the float n
        '''
    return f(n)
