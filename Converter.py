import csv
import json

with open("Citrust - BossItems.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    data = []

    for row in reader:
        obj = {}
        for key, value in row.items():
            # convert numeric fields to int if possible
            if value.isdigit():
                value = int(value)
            # only add if not zero or empty
            if value != 0 and value != "":
                obj[key] = value
        data.append(obj)

with open("bossItems.json", "w") as jsonfile:
    json.dump(data, jsonfile, indent=2)