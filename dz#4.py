wall = [
    [2, 1, 2],
    [2, 3],
    [1, 1, 3],
    [4, 1],
    [2, 1, 1, 1],
]
def func(_wall):
    _dict = {}
    max_val = 0
    for row in _wall:
        _sum = 0
        for brick in row[:-1]:
            _sum += brick
            if _sum in _dict:
                _dict[_sum] += 1
            else:
                _dict[_sum] = 1
            max_val = max(_dict.values())
    return len(_wall) - max_val
print(func(wall))