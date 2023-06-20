#!/usr/bin/env python3

def remove_duplicates(input_file, output_file):
    with open(input_file, 'r') as f:
        data = f.readlines()

    unique_data = []
    seen = set()

    for line in data:
        line = line.strip()  # Remove leading/trailing white space
        if line:  # Skip empty lines
            tuple_line = tuple(line.split(','))
            if tuple_line not in seen:
                unique_data.append(line)
                seen.add(tuple_line)

    with open(output_file, 'w') as f:
        f.write('\n'.join(unique_data))

# Call the function with your specific file names
remove_duplicates('accu_process_tweet.txt', 'revised_accu_process_tweet.txt')

