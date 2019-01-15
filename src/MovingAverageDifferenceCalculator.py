import csv

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

def calculate_moving_average_differences(moving_averages_global, moving_averages_local):
    result = []

    for index in range(len(moving_averages_local)):
        result.append("{0:.2f}".format(float(moving_averages_global[index][1]) - float(moving_averages_local[index][1])))

    return result

def count_moving_average_differences(start, end, differences):
    amount = 0

    for difference in differences:
        if start <= float(difference) <= end:
            amount +=1

    return amount

print calculate_moving_average_differences(read_and_calculate_moving_average('avg_temp_global', 10), read_and_calculate_moving_average('avg_temp_munich', 10))
print count_moving_average_differences(3.5, 4, calculate_moving_average_differences(read_and_calculate_moving_average('avg_temp_global', 10), read_and_calculate_moving_average('avg_temp_munich', 10)))