import csv
import math

def read_and_calculate_moving_average(filename, moving_average_year_span):
    with open(filename + '.csv') as csvfile:
        reader = csv.DictReader(csvfile)

        moving_averages = {}
        calculated_moving_averages = []

        for row in reader:
            current_average = row['avg_temp']

            calculated_moving_averages.append(float(current_average if current_average else calculate_moving_average(calculated_moving_averages)))

            if len(calculated_moving_averages) == moving_average_year_span:
                moving_averages[row['year']] = calculate_moving_average(calculated_moving_averages)
                calculated_moving_averages.pop(0)

        return sorted(moving_averages.items())

def calculate_moving_average(calculated_moving_averages):
    return "{0:.2f}".format(sum(calculated_moving_averages) / len(calculated_moving_averages))

def calculate_correlation_coefficient(moving_average_global, moving_average_local):
    average_global = calculate_average(moving_average_global)
    average_local = calculate_average(moving_average_local)

    length = len(moving_average_global) if len(moving_average_global) < len(moving_average_local) else len(moving_average_local)
    counter = 0
    denominator_global = 0
    denominator_local = 0

    for index in range(length):
        counter += (float(moving_average_global[index][1]) - average_global) * (float(moving_average_local[index][1]) - average_local)
        denominator_global += math.pow(float(moving_average_global[index][1]) - average_global, 2)
        denominator_local += math.pow(float(moving_average_local[index][1]) - average_local, 2)

    return "{0:.2f}".format(counter / (math.sqrt(denominator_global) * math.sqrt(denominator_local)))

def calculate_average(moving_averages):
    average = 0

    for moving_average in moving_averages:
        average += float(moving_average[1])

    return average / len(moving_averages)

print calculate_correlation_coefficient(read_and_calculate_moving_average('avg_temp_global', 10), read_and_calculate_moving_average('avg_temp_munich', 10))