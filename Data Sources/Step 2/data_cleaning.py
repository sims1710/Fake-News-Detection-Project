import pandas as pd
import nltk
from nltk.corpus import stopwords
import string

# Load the CSV file
df = pd.read_csv('filtered_fake_dataset.csv')

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
df['label'] = df['type'].map({'bs': 1, 'bias': 2, 'conspiracy': 3, 'hate': 4, 'satire': 5, 'junksci': 6, 'fake': 7})

# Output the new dataset as final_fake_dataset.csv
df.to_csv('final_fake_dataset.csv', index=False)
print("Final dataset created and saved successfully!")
