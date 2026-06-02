import json

filename = "data.json"

try:
    with open(filename, "r") as file:
        data = json.load(file)

        print("----- JSON DATA -----")
        print(json.dumps(data, indent=4))

except FileNotFoundError:
    print("File not found! Please check filename.")

except json.JSONDecodeError:
    print("Invalid JSON format in file.")