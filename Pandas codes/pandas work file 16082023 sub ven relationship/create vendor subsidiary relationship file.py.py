import csv
from itertools import product

# Vendor master file= Col A:External ID, Col B: Internal ID, col C: ID, col D: Name
# subsidiary to be added file= Col A: Sub name, Col B:Prod Int ID, Col C: SB Int ID

with open("vendor master file.csv", "r") as master_file:
    master_reader = csv.reader(master_file)
    next(master_reader)  # to skip colomn header
    vendors = [row[2] for row in master_reader] #read 3rd coloumn data (index 2 = col 3)


with open("subsidiary to be added.csv", "r") as subsidiary_file:
    subsidiary_reader = csv.reader(subsidiary_file)
    next(subsidiary_reader)  # to skip colomn header
    subsidiaries = [row for row in subsidiary_reader]

# Generate all combinations of vendors and subsidiaries(for all vendors combinations populate subsidiary)
combinations = list(product(vendors, subsidiaries))


with open("output combinations with int ID.csv", "w", newline="") as output_file:
    output_writer = csv.writer(output_file)
    output_writer.writerow(["Vendor", "Subsidiary Col A", "Sub Int ID in Prod", "Sub Int in SB"])  # Header name on output file
    for vendor, subsidiary in combinations:
        output_writer.writerow([vendor] + subsidiary)
