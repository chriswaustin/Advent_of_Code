import csv
import math


def getData():
    with open('day1.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)

        data = []
        for row in reader:
            data.append(int(row[0]))

        return data


def part1():
    data = getData()
    return sum(map(lambda n:  math.floor(n/3) - 2, data))


def part2():
    data = getData()

    fuel = 0

    while len(data) > 0:
        data = calcFuel(data)
        data = list(filter(lambda n: n > 0, data))
        fuel += sum(data)

    return fuel


def calcFuel(data):
    return list(map(lambda n:  math.floor(n/3) - 2, data))


print(part1())
print(part2())
