# Fake News Detection

Our group is developing a Neural Network solution to detect first fake news when inputted an article and then classifying as what type of fake news it is.

## Step 1: Fake News Detection

In this first step, we run five different types of NNs and choose the best one (based on the evaluation metrics) to continue with Step 2. The `merged_data.csv` file from the Data Source Folder is used as our dataset. It is splitted into the following ratio: 80-10-10 (training-testing-validation).

### Datasets 
1. Step 1: https://github.com/sophialatessa/FakeNewsDeepLearning
2. Step 2: https://www.kaggle.com/datasets/mrisdal/fake-news

## Running the GUI

To run the GUI:
1. Unzip AIGUI.zip
2. Install the necessary python modules in this environment 
3. Run the GUI using streamlit run aifrontend.py in the directory.

Please take note that model weights are required to be save so that the model are imported correctly.

## Final Model: Model Weights
Separately, model weights are saved to run the combined the model.
