from models.relai import Relai

class EmployeesManager:
    
    def __init__(self):
        self.employees_ids = []
        self.relai = Relai()

    
    def update(self, updated_list):
        # remove employees_ids out of range
        for i, uuid in enumerate(self.employees_ids):
            if uuid not in updated_list:
                self.relai.publish_exit(uuid)
                self.employees_ids.pop(i)

        # add new employees_ids in range
        for i, uuid in enumerate(updated_list):
            if uuid not in self.employees_ids:
                self.relai.publish_arrival(uuid)
                self.employees_ids.append(uuid)
                

    def employees_count(self):
        print(f"size {len(self.employees_ids)}")
        return len(self.employees_ids)