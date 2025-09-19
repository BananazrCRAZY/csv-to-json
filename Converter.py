import csv
import json

with open("Citrust - Items.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    data = []

    for row in reader:
        obj = {}

        # Always include ID + name, even if 0/empty
        obj["id"] = int(row["id"])
        obj["name"] = row["name"]

        for key, value in row.items():
            if key in ("id", "name"):  # skip, already added
                continue

            # convert numeric fields to int if possible
            if value.isdigit():
                value = int(value)
            # only add if not zero or empty
            if value != 0 and value != "":
                obj[key] = value
        data.append(obj)

with open("items.json", "w") as jsonfile:
    json.dump(data, jsonfile, indent=2)