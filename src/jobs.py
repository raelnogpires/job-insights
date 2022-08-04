from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, encoding="utf-8") as file:
        csv_reader = csv.reader(file, delimiter=",", quotechar='"')
        header, *data = csv_reader

    return [header, data]
