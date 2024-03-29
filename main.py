import json
import datetime

def get_types(data):
    types_dict = {}
    for ride in data:
        if ride["type"] in types_dict:
            types_dict[ride["type"]] += 1
        else: types_dict[ride["type"]] = 1
    return types_dict

def get_sum_of_no(data):
    sum = 0
    for ride in data:
        if ride["no"]:
            sum += int(ride["no"])
    return sum

def get_lines(data):
    lines = {}
    for ride in data:
        if ride["line"]:
            line = ride["type"] + " " + ride["line"]
        else:
            line = ride["type"] + " " + ride["no"]
        if line in lines:
            lines[line] += 1
        else:lines[line] = 1
    return lines

def get_first_timestamp(data):
    return datetime.datetime.fromtimestamp(data[-1]["checkin_ts"])

def main():
    filename = "input-data/history.json"
    with open(filename, encoding="utf-8") as f:
        data = json.load(f)
    print(f"Fahrten gesamt: {len(data)}")
    print(f"Nach Fahrzeug: {get_types(data)}")
    print(f"Summe der Fahrtnummern: {get_sum_of_no(data)}")
    print(f"Erste Fahrt: {get_first_timestamp(data)}")
    print(f"Gefahrene Linien: {get_lines(data)}")

if __name__ == "__main__":
    main()
