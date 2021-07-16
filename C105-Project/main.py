import csv
import math
import statistics
with open('data.csv', newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = [60, 61, 65, 63, 98, 99, 90, 95, 91, 96]


def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total += int(x)
    mean = total/n
    return mean


# squaring and getting the values
squared_list = []
for number in data:
    a = int(number) - mean(data)
    a = a**2
    squared_list.append(a)

# getting sum
sumtotal = 0
for i in squared_list:
    sumtotal = sumtotal+1

# diving by sum by total values
result = sumtotal / (len(data)-1)

std_deviation = math.sqrt(result)

print("Standard deviation by calculation", std_deviation)
print("Standard deviation by formula", statistics.stdev(data))
