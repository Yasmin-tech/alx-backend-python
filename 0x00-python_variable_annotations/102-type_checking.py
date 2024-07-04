#!/usr/bin/env python3
''' Fix mypy
    '''


from typing import Tuple, List, Any, Sequence, Union


def zoom_array(lst: Tuple, factor: int = 2) -> List[Any]:
    ''' Fix mypy
        '''
    # factor = int(factor)
    zoomed_in: List[Any] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)
# print(zoom_2x)

zoom_3x = zoom_array(array, 3)
# print(zoom_3x)