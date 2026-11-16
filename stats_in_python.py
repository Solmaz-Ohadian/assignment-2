import sys
import math

def load_data(filepath:str, column:int)->tuple[list, int]:
    # TODO - Complete the function so it loads the data from the file into a list
    # The function returns a tuple that contains the list of values and the total number 
    # of values in the column
     
    numbers = []
    count = 0

    with open(filepath, "r") as infile:
        for line in infile:
            count += 1
            fields = line.split("\t")

            try:
                if column < 0:
                    raise IndexError
                value = fields[column]
            except IndexError:
                sys.exit(
                    f"Exiting: There is no valid 'list index' in column {column} "
                    f"in line {count} in file: {filepath}"
                )

            try:
                number = float(value)
            except ValueError:
                continue

            if not math.isnan(number):
                numbers.append(number)

    if len(numbers) == 0:
        sys.exit(f"Error: There were no valid number(s) in column {column} in file: {filepath}")

    return numbers, count

    return numbers, count

def calculate_average(numbers:list)->float:
    # TODO - Complete the function to return the average of the list of numbers

     return sum(numbers) / len(numbers)

def get_max_and_min(numbers:list)->tuple[float, float]:
    # TODO - Complete the function to return a tuple with the maximum and minimum
    # values in the list, in that order
    
    return max(numbers), min(numbers)


def calculate_variance(numbers:list)->float:
    # TODO - Complete the function to return the variance of the numbers in the list
    
    count = len(numbers)

    if count == 1:
        return 0.0

    average = calculate_average(numbers)
    squared_total = 0.0

    for number in numbers:
        difference = number - average
        squared_total += difference ** 2

    return squared_total / (count - 1)


def calculate_std_dev(numbers:list)->float:
    # TODO - Complete the function to return the standard deviation of the numbers in the list

    variance = calculate_variance(numbers)
    return math.sqrt(variance)


def calculate_median(number:list)->float:
    # TODO - Complete the function to return the median of the numbers in the list

    sorted_numbers = sorted(number)
    count = len(sorted_numbers)
    middle = count // 2

    if count % 2 == 1:
        return float(sorted_numbers[middle])

    return calculate_average([sorted_numbers[middle - 1], sorted_numbers[middle]])

