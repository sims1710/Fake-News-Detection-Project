import csv
import random

# Read CSV file and return rows without the first column
def read_csv(input_file):
    rows = []
    with open(input_file, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            rows.append(row[1:])  # Ignore the first column
    return rows

# Write CSV file with an index column
def write_csv(output_file, merged_data):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['index', 'article', 'real/fake'])  # Write header row
        for index, article in enumerate(merged_data):
            writer.writerow([index] + article)  # Write index column as the first column, followed by data

# Merge two CSV files in a random manner
def merge_csvs(csv1, csv2):
    merged_data = csv1 + csv2
    random.shuffle(merged_data)  # Shuffle the merged data randomly
    return merged_data

# Input file paths
input_file1 = 'labeled_real_data.csv'
input_file2 = 'labeled_fake_data.csv'

# Output file path
output_file = 'merged_data.csv'

# Read data from input CSV files without the first column
data1 = read_csv(input_file1)
data2 = read_csv(input_file2)

# Merge the data from both CSV files
merged_data = merge_csvs(data1, data2)

# Write merged data to a new CSV file with an index column
write_csv(output_file, merged_data)

print("CSV files merged successfully!")

