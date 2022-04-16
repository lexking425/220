'''
Lex King
sales_person.py
this code creates a class that uses employee id, name and compares sales.
this is my code
'''

class SalesPerson:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales.append(float(sale))

    def total_sales(self):
        return sum(self.sales)

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        return self.total_sales() >= quota

    def compare_to(self, other):
        value = None
        if self.total_sales() < other.total_sales():
            value = -1
        if self.total_sales() > other.total_sales():
            value = 1
        if self.total_sales() == other.total_sales():
            value = 0
        return value

    def __str__(self):
        return "{}-{}: {}".format(self.employee_id, self.name, self.total_sales())
