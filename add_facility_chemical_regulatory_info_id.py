import csv
import uuid
import sys

def add_uuid_column(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
        
    data[0].insert(0, "Facility Chemical Regulatory Info ID")
    
    for row in data[1:]:
        row.insert(0, str(uuid.uuid4()))
        
    writer = csv.writer(sys.stdout)
    writer.writerows(data)

if __name__ == "__main__":
    add_uuid_column(sys.argv[1])