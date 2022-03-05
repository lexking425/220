"""
Lex King
hw7.py
in this code changes the format of a sentence, finds hourly wage, calculates and sends messages.
this is my code
"""


def number_words(in_file_name, out_file_name):
    with open(in_file_name, 'r') as in_file:
        with open(out_file_name, 'w') as out_file:
            lines = in_file.readlines()
            acc = 1
            for line in lines:
                word = line.split()
                for j in range(0, len(word)):
                    print(str(acc) + " " + word[j])
                    acc += 1
number_words("walrus.txt","walrus_out.txt")


def hourly_wages(in_file_name, out_file_name):
    with open(in_file_name, 'r') as in_file:
        with open(out_file_name, 'w') as out_file:
            lines = in_file.readlines()
            for line in lines:
                words = line.split(' ')
                new_wage = int(words[2]) + 1.65
                weekly = new_wage * int(words[3])
                print(str(words[0]) + " " + str(words[1]) + " " + str(round(weekly, 2)))
hourly_wages("hourly_wages.txt", "hourly.txt")

def calc_check_sum(isbn):
    acc = 0
    acc2 = 10
    for i in isbn:
        acc += int(i) * acc2
        acc2 -= 1
    return acc
calc_check_sum("072946520")

def send_message(file_name, friend_name):
    with open(file_name + 'r') as in_file:
        with open(friend_name + 'w') as out_file:
            lines = in_file.readline()
            for i in lines:
                print(i ,end=' ')
send_message("bob.txt", "friend.txt")

def encode():
    pass


def send_safe_message(file_name, friend_name, key):
    pass


def send_uncrackable_message(file_name, friend_name, pad_file_name):
    with open(file_name + 'r') as in_file:
        with open(friend_name + 'r') as friend_file:
            with open(pad_file_name + 'w') as out_file:


if __name__ == '__main__':
    pass
