"""
Lex King
lab1.py
developing a simple python program that asks for input, does arithmetic, and provides output.
This is my code.
"""

def monthly_interest():
    annual_rate = eval(input("What is your annual interest rate?"))
    billing_cycle = eval(input("How many days are in your billing cycle?"))
    net_balance = eval(input("What is your previous net balance?"))
    payment_amount = eval(input("What is your payment amount?"))
    payment_day = eval(input("What day was your payment made?"))

    step_1 = net_balance * billing_cycle
    step_2 = payment_amount * (billing_cycle - payment_day)
    step_3 = step_1 - step_2

    avg_daily_balance = step_3 / billing_cycle
    monthly_rate = (annual_rate / 100) / 12
    interest_rate = avg_daily_balance * monthly_rate

    print("Your monthly interest is:$", interest_rate)