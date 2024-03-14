import pandas as pd

# Load the fake.csv file
df = pd.read_csv('fake.csv')

# Define the allowed types
allowed_types = ['bs', 'bias', 'conspiracy', 'hate', 'satire', 'junksci', 'fake']

# Filter rows based on allowed types
filtered_df = df[df['type'].isin(allowed_types)]

# Create a new DataFrame with the desired columns
new_df = filtered_df[['title', 'text', 'type']].copy()

# Reset the index
new_df.reset_index(drop=True, inplace=True)

# Add an index column starting from 0
new_df.insert(0, 'index', range(len(new_df)))

# Save the new dataset to a CSV file
new_df.to_csv('filtered_fake_dataset.csv', index=False)

print("New dataset created and saved successfully.")
