import sys
import info
import brick

name = open("profile.txt", "r")
print("Hello" + " ", name.readline())
name.close()
print("You can quit by 'q'")
print("Call the 'brick_wall' function by 1")
print("Call the function with data and keys by 2")
print("Call the sorting function by 3")
rename = input("if it is not your name enter 'an', else another symbol: ")


try:
    f = open("profile.txt", "r")
except FileNotFoundError:
    f = open("profile.txt", "w")
    f.write(input("Enter your name: "))
else:
    if rename == "an":
        f = open("profile.txt", "w")
        f.write(input("Enter the right name: "))
        sys.exit()
finally:
    f.close()


wall = [
    [2, 1, 2],
    [2, 3],
    [1, 1, 3],
    [4, 1],
    [2, 1, 1, 1],
]


data = [
    {"name": "Danil", "lastname": "Pohrebniak", "age": 18},
    {"name": "Danil", "lastname": "Pohrebniak", "age": 18},
    {"name": "Danil", "lastname": "Ivanov", "age": 19}
]
keys = ["name", "lastname"]


def sorting_func(_list):
    if len(_list) <= 1:
        return _list

    base = _list[0]
    left = [element for element in _list if element < base]
    middle = [element for element in _list if base == element]
    right = [element for element in _list if base < element]

    return sorting_func(left) + middle + sorting_func(right)


while True:
    enter = str(input("Enter the symbol: "))
    valid_choices = ["1", "2", "3", "q"]
    if enter == "q":
        break
    elif enter == "1":
        print(brick.brick_wall(wall))
        continue
    elif enter == "2":
        print(info.func(data, keys))
        continue
    elif enter == "3":
        nums = list(map(int, input("Enter the list of numbers: ")))
        print(set(sorting_func(nums)))
        continue
