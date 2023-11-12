import json

FILE_NAME = 'input.json'


def task() -> float:
    with open(FILE_NAME) as file:
        json_data = json.load(file)

    sum_values = sum([item["score"] * item["weight"] for item in json_data])
    return round(sum_values, 3)


print(task())
