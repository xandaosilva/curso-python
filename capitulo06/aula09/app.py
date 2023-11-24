# Arquivo data.csv gerado através do link 
# https://media.githubusercontent.com/media/datablist/sample-csv-files/main/files/people/people-100.csv

import csv
from pathlib import Path

PATH_CSV = Path(__file__).parent / "data.csv"

print(PATH_CSV)

with open(PATH_CSV, "r") as file:
    file_reader = csv.reader(file)
    print(next(file_reader))

    for line in file_reader:
        print(line)

