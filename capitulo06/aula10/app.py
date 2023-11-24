import csv
from pathlib import Path

PATH_CSV = Path(__file__).parent / "data.csv"

list_clients = [
    { "Name": "Shelby Terrell", "Address": "AV 1, 37"},
    { "Name": "Kristine Travis", "Address": "AV 2, 45"},
    { "Name": "Stacy Newton", "Address": "AV 3, 21"},
]

with open(PATH_CSV, "w") as file:
    columns = list_clients[0].keys()
    writer = csv.writer(file)

    writer.writerow(columns)

    for client in list_clients:
        writer.writerow(client.values())