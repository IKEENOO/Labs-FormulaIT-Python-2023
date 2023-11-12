import json
import csv

INPUT_FILE = 'input.csv'
OUTPUT_FILE = 'output.json'


def task() -> None:
    with open(INPUT_FILE) as file:
        lines = [line for line in csv.DictReader(file)]

    with open(OUTPUT_FILE, "w") as file:
        json.dump(lines, file, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILE) as output_f:
        for line in output_f:
            print(line, end="")
