import csv
import matplotlib.pyplot as plt

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

def draw_calculated_moving_averages(moving_averages_global, moving_averages_local, city_name):
    relevant_years = get_relevant_years(moving_averages_global, moving_averages_local)
    relevant_moving_averages_local= get_relevant_moving_averages(moving_averages_global, moving_averages_local)
    relevant_moving_averages_global = get_relevant_moving_averages(moving_averages_local, moving_averages_global)

    plt.plot(relevant_years, relevant_moving_averages_local)
    plt.plot(relevant_years, relevant_moving_averages_global)
    plt.xlabel('years')
    plt.ylabel('average temperature (Celsius)')
    plt.title('moving average temperature of the world (blue) and ' + city_name + ' (green)')
    plt.show()


def get_relevant_years(moving_averages_global, moving_averages_local):
    result_list = []

    for year_in_moving_average_global in moving_averages_global:
        for year_in_moving_average_local in moving_averages_local:
            if year_in_moving_average_global[0] == year_in_moving_average_local[0]:
                result_list.append(year_in_moving_average_local[0])

    return result_list

def get_relevant_moving_averages(averages_to_compare, averages_to_work):
    result = []

    for average_to_compare in averages_to_compare:
        for average_to_work in averages_to_work:
            if average_to_work[0] == average_to_compare[0]:
                result.append(average_to_work[1])

    return result

draw_calculated_moving_averages(read_and_calculate_moving_average('avg_temp_global', 10), read_and_calculate_moving_average('avg_temp_munich', 10), 'Munich')
#draw_calculated_moving_averages(read_and_calculate_moving_average('avg_temp_global', 10), read_and_calculate_moving_average('avg_temp_new_york', 10), 'New York')
#draw_calculated_moving_averages(read_and_calculate_moving_average('avg_temp_global', 10), read_and_calculate_moving_average('avg_temp_belo_horizonte', 10), 'Belo Horizonte')