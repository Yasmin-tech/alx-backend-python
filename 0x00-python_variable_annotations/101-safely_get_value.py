#!/usr/bin/env python3
''' duck-typed annotations
    '''


from typing import Mapping, Any, Optional, TypeVar, Union

T = TypeVar("T")


# The types of the elements of the input are not know
def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    ''' duck-typed annotations
        '''
    if key in dct:
        return dct[key]
    else:
        return default
