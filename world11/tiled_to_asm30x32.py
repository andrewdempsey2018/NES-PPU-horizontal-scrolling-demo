import csv

lookup = ["$%02X" % i for i in range(256)]

# Read entire CSV into memory
data = []

with open('world11.csv', 'r') as file:
    csv_data = csv.reader(file)
    for row in csv_data:
        # convert values to int and handle -1
        int_row = []
        for item in row:
            value = int(item)
            if value == -1:
                value = 0
            int_row.append(value)
        data.append(int_row)

# Transpose the 32x30 input into 30x32
# zip(*data) flips rows and columns
transposed = list(zip(*data))

# Build output
result = ""

for row in transposed:
    result += ".byte "
    for i, value in enumerate(row):
        if i == len(row) - 1:
            result += lookup[value] + "\n"
        else:
            result += lookup[value] + ","

with open("output.txt", "w") as output_file:
    output_file.write(result)
