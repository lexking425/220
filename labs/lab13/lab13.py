'''
Lex King
lab13.py
this code alerts and warns the user when the stock market is moving.
this is my code
'''

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
                lowest = values[j]
                position = values.index(lowest)
            values[i], values[position] = values[position], values[i]
        return values

def calc_area(rect):
    height = abs(rect.getP1().getY() - rect.getP2().getY())
    width = abs(rect.getP1().getX() - rect.getP2().getX())
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

def trade_alert(filename):
    file = open(filename, 'r')
    read = file.read().split()
    int = []
    for i in read:
        int.append(int(i))
    sec = 0
    for i in int:
        sec += 1
        if i > 830:
            print("Alert at {} seconds! Value = {}".format(sec, i))
        elif i > 500:
            print("Warning at {} seconds! Value = {}".format(sec, i))

if __name__ == '__main__':
    trade_alert('trades.txt')





