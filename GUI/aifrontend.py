import streamlit as st
import pandas as pd
from PIL import Image
import torch
import io
import pickle
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from sklearn.preprocessing import LabelEncoder
from keras.preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
import numpy as np 
import tensorflow as tf
import joblib
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


image = Image.open('./news-man.jpg')
st.image(image)

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('words')

# Function to remove non-English words and stopwords
def clean_text(text):
    english_words = set(nltk.corpus.words.words())
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    cleaned_words = [word.lower() for word in words if word.lower() in english_words and word.lower() not in stop_words]
    return ' '.join(cleaned_words)

st.title('FakeNews Detection and Classification')

st.write('This is a simple web app aims to detect fake news given the aritcle. It then will classify the type of FakeNews.')
st.write('If a piece of news is classified as FakeNews, it will be categorised into one of the following categories:')

col1, col2 = st.columns(2)
with col1:
    st.markdown('- **BS (Bullshit):** Fabricated nonsense to mislead and confuse.')
    st.markdown('- **Bias:** Manipulating facts to favour one side.')
    st.markdown('- **Conspiracy:** Wild claims without credible evidence presented.')
    st.markdown('- **Hate:** Intentional misinformation to incite division and animosity.')

with col2:
    st.markdown('- **Satire:** Mocking with exaggerated or humorous fiction.')
    st.markdown('- **Junksci (Junk Science):** Pseudoscience packaged as credible research.')
    st.markdown('- **State:** Government-backed propaganda, often with ulterior motives.')


st.markdown('### Usage')
article_input = clean_text(st.text_area("Paste article to be analysed here", height=300))

#------------ Model 1
def predict(text):

    if article_input != "":
        # Load the trained model
        model1 = AutoModelForSequenceClassification.from_pretrained("model1/model", num_labels=2)

        # Load the tokenizer
        tokenizer = AutoTokenizer.from_pretrained("model1/model")

        # Load the LabelEncoder
        with open("./model1/label_encoder.pkl", "rb") as le_file:
            label_encoder = pickle.load(le_file)

        # Tokenize the input text
        inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
        # Perform inference
        with torch.no_grad():
            outputs = model1(**inputs)
        # Get predicted label
        predicted_label_id = torch.argmax(outputs.logits).item()
        # Check if predicted label index is within bounds
        if predicted_label_id < len(label_encoder.classes_):
            predicted_label = label_encoder.classes_[predicted_label_id]
        else:
            # Handle out of bounds index 
            predicted_label = "Unknown"
        return predicted_label


# ------------ Model 2  
def classify(text):
    tokenizer2 = joblib.load("./model2/tokenizer2.sav")
    model2 = joblib.load("./model2/model2.sav")

    combined_sample_tokenised = tokenizer2.texts_to_sequences([[text]])
    combined_sample_train_data = pad_sequences(combined_sample_tokenised, maxlen=199)

    combined_predicted = model2.predict(combined_sample_train_data, batch_size=1024, verbose=1)

    df_combined_pred = pd.DataFrame(combined_predicted)
    df_combined_pred = df_combined_pred.where(df_combined_pred!=0).rank(1, ascending=False, method='dense').eq(1).astype(int)

    return df_combined_pred



# Styled button using HTML and CSS
button_style = """
    <style>
    .styled-button {
        display: flex;
        justify-content: center;
        align-items: center;
        background-image: linear-gradient(to right, #8d9377, #96a5a0);
        border-radius: 5px;
        color: white;
        padding: 10px 20px;
        border: none;
        cursor: pointer;
        font-size: 16px;
    }
    </style>
"""

# Add the styled button
st.markdown(button_style, unsafe_allow_html=True)

# Add functionality to the button
if st.markdown("<button class='styled-button' type='submit'>Check this article!</button>", unsafe_allow_html=True):
    prediction = predict(article_input)

    if prediction == 'real':
        prediction = 'Real News'
        st.markdown("<h4 style='color: green;'>Prediction: " + prediction + "</h4>", unsafe_allow_html=True)


    if prediction == 'fake':
        prediction = 'Fake News'
        st.markdown("<h4 style='color: red;'>Prediction: " + prediction + "</h4>", unsafe_allow_html=True)
        classification = classify(article_input)
        classification = pd.from_dummies(classification)
        classification.columns = ["type"]
        classification.type = classification.type.replace({0:"bias", 1:"bs",2: "conspiracy", 3:"fake", 4:"hate",5:"junksci", 6:"satire",7: "state"})
        class_type = classification.iloc[0,0]
        st.write('Category:', class_type.capitalize())




    












