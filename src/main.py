import re
from collections import defaultdict

def round_ieee754(value, decimal_places=1):
    multiplier = 10 ** decimal_places
    return int(value * multiplier + 0.5) / multiplier

def main(input_file_name="testcase.txt", output_file_name="output.txt"):
    city_data = defaultdict(list)

    # Use 'with' statement for proper file handling
    with open(input_file_name, "r") as input_file, open(output_file_name, "w") as output_file:
        # Parse the input file
        for line in input_file:
            line = line.strip()
            if not line:  # Skip empty lines
                continue
            # Split the line into city and temperature
            parts = line.split(";")
            if len(parts) == 2:
                city, temp = parts
                try:
                    temp = float(temp)  # Convert temperature to float
                    city_data[city].append(temp)
                except ValueError:
                    continue  # Skip invalid temperatures

        # Process and write output
        for city in sorted(city_data):
            temps = city_data[city]
            min_temp = round_ieee754(min(temps))
            mean_temp = round_ieee754(sum(temps) / len(temps))
            max_temp = round_ieee754(max(temps))
            output_file.write(f"{city}={min_temp}/{mean_temp}/{max_temp}\n")

if __name__ == "__main__":
    main()

# def main(input_file_name = "testcase.txt", output_file_name = "output.txt"):
#     input_file = open(input_file_name, "r")
#     output_file = open(output_file_name, "w")

#     first_line = input_file.readline().strip()
#     first_line = first_line.split(";")

#     output_file.write(f"{first_line[0]}={first_line[1]}/{1}/{1}\n")

#     output_file.close()
#     input_file.close()

# if __name__ == "__main__":
#     main()