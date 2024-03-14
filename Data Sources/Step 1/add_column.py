import csv

# Read CSV file and add labels
def add_labels(input_file, label):
    labeled_rows = []
    with open(input_file, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            row.append(label)  # Append the label to each row
            labeled_rows.append(row)
    return labeled_rows

# Write labeled CSV to a new file
def write_output(output_file, labeled_data):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(labeled_data)

# Input file paths
real_input_file = 'real.csv'
fake_input_file = 'fake.csv'

# Output file paths
real_output_file = 'labeled_real_data.csv'
fake_output_file = 'labeled_fake_data.csv'

# Add labels to the real CSV file
labeled_real_data = add_labels(real_input_file, 'Real')

# Write labeled real data to a new file
write_output(real_output_file, labeled_real_data)

# Add labels to the fake CSV file
labeled_fake_data = add_labels(fake_input_file, 'Fake')

# Write labeled fake data to a new file
write_output(fake_output_file, labeled_fake_data)

print("Labels added successfully.")
