import math

def getValue(file, key):
    f = open(f"./data/files/{file}.txt", "r")

    for line in f.read(5120).splitlines():
        k, v = line.strip().split(":")

        if k == key:
            return float(v.strip()) if v.isnumeric() else v.strip()