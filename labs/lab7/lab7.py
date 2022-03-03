'''
Lex King
lab7.py

this is my code
'''

def weighted_average(in_file_name, out_file_name):
    with open(in_file_name, 'r') as in_file:
        with open(out_file_name, 'w') as out_file:
            lines = in_file.readlines()

            class_average = 0
            total_students = 0
            for line in lines:
                line_split = line.split(':')
                name = line_split[0]
                numbers = line_split[1].split()
                weight = 0
                for i in numbers[::2]:
                    weight += int(i)

                average = 0
                if weight == 100:
                    for j in range(len(numbers[::2])):
                        average += int(numbers[j]) * int(numbers[j + 1])
                    average = average / 100
                    print(name + "'s average: " + str(average))
                    class_average += average
                    total_students += 1
                elif weight > 100:
                    print(name + "'s average: ERROR: The weights are more than 100.")
                elif weight < 100:
                    print(name + "'s average: ERROR: The weights are less than 100.")
            class_average = class_average / total_students
            print("Class average: " + str(class_average))

weighted_average("grades.txt", "avg.txt")






