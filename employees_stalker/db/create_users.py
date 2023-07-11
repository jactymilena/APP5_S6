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
    writer.writerow(["7f3bfd87-a46d-4a51-bdeb-7a479432a8f8"])
    writer.writerow(["5b964c48-2edc-43b3-b6bf-c50a563460a2"])
    writer.writerow(["cc94b74a-f2ec-4c66-88fc-558813b475b0"])
    writer.writerow([uuid.uuid4()])
    writer.writerow([uuid.uuid4()])
    writer.writerow([uuid.uuid4()])

