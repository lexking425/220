"""
Lex King
lab3.py
writing program to analyze traffic patterns
This is my code
"""

def traffic():
    roads = eval(input("How many roads were surveyed? "))
    total_cars = 0
    for i in range(roads):
        print("How many days was road", i + 1, "surveyed?")
        days = eval(input(" "))
        average = 0
        for j in range(days):
            print("How many cars traveled on day", j + 1, "?")
            cars = eval(input(" "))
            average = average + cars
            total_cars = total_cars + cars
            final_average = total_cars / roads
        print("Road",i + 1, "average vehicles per day: ", average/ days)
    print("Total number of vehicles traveled on all roads: ", total_cars)
    print("Average number of vehicles per road: ", final_average)