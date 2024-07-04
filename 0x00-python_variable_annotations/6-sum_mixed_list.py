#!/usr/bin/env python3
''' This model contains a type-annotated function sum_mixed_list:
    It takes a list mxd_lst of floats and integers as argument
    returns their sum as a float.
    '''


from typing import List, Union


def sum_mixed_list(input_list: List[Union[int, float]]) -> float:
    '''Computes the sum of a list of floating-point numbers and integers.
    '''
    return float(sum(input_list))
