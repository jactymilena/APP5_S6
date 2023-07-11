from models.relai import Relai
from db.database import Database

class EmployeesManager:
    
    def __init__(self):
        self.active_employees = []
        self.relai = Relai()
        db = Database('db/control.csv')
        self.employees_db = db.get_all()['uuid'].to_list()

    
    def update(self, updated_list):
        # remove.active_employees out of range
        for i, uuid in enumerate(self.active_employees):
            if uuid not in updated_list:
                self.relai.publish_exit(uuid)
                self.active_employees.pop(i)

        # add new.active_employees in range
        for i, uuid in enumerate(updated_list):
            if uuid in self.employees_db and uuid not in self.active_employees:
                self.relai.publish_arrival(uuid)
                self.active_employees.append(uuid)
                

    def employees_count(self):
        print(f"size {len(self.active_employees)}")
        return len(self.active_employees)