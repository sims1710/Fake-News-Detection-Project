import pandas as pd

# Load the CSV file
df = pd.read_csv('fake.csv')

# Get unique values in the 'type' column
unique_types = df['type'].unique()

# Print unique values
print("Unique values in the 'type' column:")
for value in unique_types:
    print(value)
