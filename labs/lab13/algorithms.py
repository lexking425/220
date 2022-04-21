'''
Lex King
algorithms.py
this lab reads the data from a file and searches the list.
this is my code
'''


def read_data(file_name):
    file = open(file_name, 'r')
    lines = file.readline()
    data = []
    while lines != '':
        split_line = lines.split()
        counts = 0
        while counts < len(split_line):
            data.append(int(split_line[counts]))
            counts += 1
        lines = file.readline()
    return data

def is_in_linear(search_val, value):
    counts = 0
    while counts < len(value):
        if search_val == value[counts]:
            return True
        counts += 1
    return False

def is_in_binary(search_val, values):
    midd = values[len(values) // 2]
    while (midd != search_val) and (len(values) != 1):
        if midd > search_val:
            values = values[:midd]
        else:
            values = values[midd + 1:]
        midd = values[len(values) // 2]
    if midd == search_val:
        return True
    else:
        return False

def selection_sort(values):
    for i in range(len(values)):
        lowest = values[i]
        position = i
        for j in range(i, len(values)):
            if values[j] < lowest:
                lowest = values[x]
                position = values.index(lowest)
            values[i], values[position] = values[position], values[i]
        return values

def calc_area(react):
    height = abs(react.getP1().getY() - react.getP2().getY())
    width = abs(react.getP1().getX() - react.getP2().getX())
    return height * width

def react_sort(rectangles):
    area = []
    val = {}
    for rect in rectangles:
        val[calc_area(rect)] = rect
        area.append(calc_area(rect))
    selection_sort(area)
    for i in range(len(area)):
        rectangles[i] = val[i]
    return rectangles