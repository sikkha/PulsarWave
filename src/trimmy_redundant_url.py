import sys

# Get the filename from the first command line argument
filename = sys.argv[1]

# Read each line into a list of tuples
data_tuples = []
with open(filename, "r") as file:
    for line in file:
        data_tuples.append(tuple(line.strip().split(',')))

# Create a new list with unique tuples based on URL (the 4th element)
unique_data_tuples = list(dict((x[3], x) for x in data_tuples).values())

# Sort the unique data
unique_data_tuples.sort()

# Print the unique data to stdout
for data_tuple in unique_data_tuples:
    print(','.join(data_tuple))
