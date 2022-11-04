"""
Follow up:
如果空地数量远大于房子，有没有办法优化
之前的做法是枚举空地，现在可以枚举房子

"""
from typing import (
    List,
)
class GridType:
    EMPTY = 0
    HOUSE = 1
    WALL = 2
class Solution:
    """
    