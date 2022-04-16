'''
Lex King
sales_force.py
this code creates a sales force file and uses the sales person file.
this is my code
'''

from sales_person import SalesPerson

class SalesForce:
    def __int__(self):
        self.sales_people = []

    def add_data(self, file_name):
        with open(file_name, 'r') as file:
            for line in file:
                split = line.split(",")
                sales = split[2].split()
                self.sales_people.append(SalesPerson(int(split[0]), (split[1])[1:]))
                for sale in sales:
                    self.sales_people[-1].enter_sale(float(sale))

    def quota_report(self, quota):
        report = []
        for i in self.sales_people:
            temp = [int(i.get_id()), i.get_name(), float(i.total_sales()), i.met_quota(quota)]
            report.append(temp)
        return report

    def top_seller(self):
        top_seller = []
        current = 0
        for i in self.sales_people:
            if i.total_sales() > current:
                current = i.total_sales()
        for i in self.sales_people:
            if i.total_sales() == current:
                top_seller.append(i)
        return top_seller

    def individual_sales(self, employee_id):
        for i in self.sales_people:
            if i.get_id() == employee_id:
                return i
        return None

    def get_sale_frequencies(self):
        pass
