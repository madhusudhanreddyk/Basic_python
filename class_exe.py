import time
class sample:
    def __init__(self,employee_id,employee_name):
        self.employee_id = employee_id
        self.employee_name = employee_name
    def display(self):
        print(f"{self.employee_id},{self.employee_name}")
ob = sample("8","madhu")
ob.display()
print(ob.employee_id)

del ob
ob.display()
