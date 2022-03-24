"""
Lex King
hw1.py
made codes to calculate the area, volume, shooting percentage, total amount of coffee, and converting kilometers to miles.
this is my code
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("enter the height: "))
    volume = length * width * height
    print("volume =", volume)


def shooting_percentage():
    total= eval(input("Enter the player's total shots: "))
    made= eval(input("Enter how many shots the player made: "))
    percent = made / total * 100
    print("Shooting percentage =", percent)


def coffee():
    cost_per_pound = 10.50
    shipping_costs = .86
    fixed_cost = 1.50
    pounds = eval(input("How many pounds of coffee would you like? "))
    total = cost_per_pound * pounds + shipping_costs * pounds + fixed_cost
    print("You're total is: ", total)



def kilometers_to_miles():
    kilometers = eval(input("How many kilometers did you travel?" ))
    miles = kilometers / 1.61
    print("You traveled", miles, "miles!")


if __name__ == '__main__':
    pass
