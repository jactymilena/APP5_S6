import csv
import uuid
from datetime import datetime

# with open('./db/archive.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     field = ["uuid", "name", "arrival_time", "exit_time"]
    
#     writer.writerow(field)
#     writer.writerow([uuid.uuid4(), "Nigeria", datetime.now(), datetime.now()])
#     writer.writerow([uuid.uuid4(), "Ukraine", datetime.now(), datetime.now()])
#     writer.writerow([uuid.uuid4(), "United Kingdom", datetime.now(), datetime.now()])

with open('./db/control.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["uuid"]
    
    writer.writerow(field)
    writer.writerow([uuid.uuid4()])
    writer.writerow([uuid.uuid4()])
    writer.writerow([uuid.uuid4()])