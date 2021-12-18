import time


# Для получения оценки "1":
def read():
    data = []
    data_in_lines = []
    with open("data.txt") as f:
        for line in f:
            data_in_lines.append([float(x) for x in line.split()])
    for element in data_in_lines:
        for x in element:
            data.append(x)
    return data


def minimum(data):
    min = data[0]
    for x in data:
        if x < min:
            min = x
    return min


def maximum(data):
    max = data[0]
    for x in data:
        if x > max:
            max = x
    return max


def addition(data):
    sum = 0
    for x in data:
        sum += x
    return sum


def multiplication(data):
    mult = 1
    for x in data:
        mult *= x
    return mult


# Для получения оценки "3":
def process(data):
    start_time = time.time()
    minimum(data)
    maximum(data)
    addition(data)
    multiplication(data)
    process_time = time.time() - start_time
    return round(process_time, 2)


# Для получения оценки "4":
def sort(data):
    num = len(data)
    for i in range(num - 1):
        for j in range(num - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                sorted_data = data
    return sorted_data


# Для получения оценки "5":
try:
    data = read()
    minimum(data)
    maximum(data)
    addition(data)
    multiplication(data)
    process(data)
    sort(data)
except OverflowError:
    print("Ошибка переполнения: файл слишком большой.")
