data = [
    {"name": "Danil", "lastname": "Pohrebniak", "age": 18},
    {"name": "Danil", "lastname": "Pohrebniak", "age": 18},
    {"name": "Danil", "lastname": "Ivanov", "age": 19}
]
keys = ["name", "lastname"]
def func(first, second):
    elem = []
    temp = []
    for _dict in first:
        values = [value for key, value in _dict.items() if key in second]
        if values not in elem:
            elem.append(values)
            temp.append(_dict)

    return temp


    #return temp
print(func(data, keys))