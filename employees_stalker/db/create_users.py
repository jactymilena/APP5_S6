import csv
import uuid
from datetime import datetime

with open('./db/users.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["uuid", "name", "last_input", "last_output"]
    
    writer.writerow(field)
    writer.writerow([uuid.uuid4(), "Nigeria", datetime.now(), datetime.now()])
    writer.writerow([uuid.uuid4(), "Ukraine", datetime.now(), datetime.now()])
    writer.writerow([uuid.uuid4(), "United Kingdom", datetime.now(), datetime.now()])