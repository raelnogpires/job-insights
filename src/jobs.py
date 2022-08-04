from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, encoding="utf-8") as file:
        result = []
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            result.append(row)

        return result
