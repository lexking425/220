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