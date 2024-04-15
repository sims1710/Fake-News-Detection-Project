import pandas as pd
import nltk
from nltk.corpus import stopwords
import string

# Load the CSV file
df = pd.read_csv('fake.csv')

# Merge title and body
df['text'] = df['title'] + ' ' + df['text']

# Delete the extra columns after merging
df.drop(columns=['title'], inplace=True)

# If package isn't downloaded:
nltk.download('stopwords')

def remove_stopwords_and_punctuation(text):
    if isinstance(text, str):
        stop_words = set(stopwords.words('english'))
        words = nltk.word_tokenize(text)
        words_filtered = [word for word in words if word not in stop_words and word not in string.punctuation]
        return " ".join(words_filtered)
    else:
        return text

# Remove stopwords and punctuation from 'text' column
df['text'] = df['text'].apply(remove_stopwords_and_punctuation)

# Create a new column: It contains the labels mapped to numbers
df['label'] = df['type'].map({'bs': 1, 'bias': 2, 'conspiracy': 3, 'hate': 4, 'satire': 5, 'junksci': 6, 'fake': 7, 'state': 8})

df['label'] = df['label'].replace([7, 1], 1)

bs_df = df[df['label'] == 1]

# Randomly select 400 rows
reduced_bs_df = bs_df.sample(n=400, random_state=1)

# Get the rest of the data
other_df = df[df['label'] != 1]

label_counts = df['type'].value_counts()

# Concatenate the reduced bs data with the rest of the data
new_df = pd.concat([other_df, reduced_bs_df])

new_df['type'] = new_df['type'].replace('fake', 'bs')

# Print all the unique values in the dataset
unique_types = new_df['type'].unique()
print("Unique values in the 'type' column:")
for value in unique_types:
    print(value)

# Format dataset to make sure only the columns text, type and label are present in the dataset
new_df = new_df[['text', 'type', 'label']]

# Add an index integer column as the first column
new_df.reset_index(inplace=True)

new_df.to_csv('cleaned_fake.csv', index=False)
print("Final dataset created and saved successfully!")
