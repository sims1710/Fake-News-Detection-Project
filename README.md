# Fake News Detection and Classification

## Description
The purpose of this project is to devise an AI model that is able to detect whether an article of news is fake or real, and thus classify the fake news type. There are 7 predefined classes of fake news:

* BS (Bullshit): Fabricated nonsense to mislead and confuse.
* Bias: Manipulating facts to favour one side.
* Conspiracy: Wild claims without credible evidence presented.
* Hate: Intentional misinformation to incite division and animosity.
* Satire: Mocking with exaggerated or humorous fiction.
* Junksci (Junk Science):  Pseudoscience packaged as credible research.

Our model is composed of 2 different classification models working together to correctly detect fake news and classify the type of fake news article. The first model is a text-based binary classification of fake news vs real news, while the second model is a text-based multi-class classification of the type of fake news. The figure below shows the pipeline of our combined model. If the intermediary output is ‘fake’, the second model will be called to identify the type of fake news.
 

We first explored four different models (CNN, GRU, LTSM and GPT2) and then chose the best algorithm for each model, combined them and rendered our combined model. The best model is decided based on the following evaluation metrics:

* Accuracy: The proportion of correct predictions among all predictions made by the model.
* Precision: The proportion of correct positive predictions among all positive predictions made by the model.
* Recall: The proportion of actual positive instances that were correctly predicted by the model.
* F1 Score:  A combined metric that balances precision and recall, providing a single score that reflects both aspects of model performance.

### The Graphic User Interface
The GUI for our project is mainly implemented using the Streamlit python module. We saved our models and placed them in a convenient location with the GUI python file for easy reference and loading. The saved models contain the weight as well since they are crucial to run our models in GUI. The article is taken in as text, cleaned, and then passed to the respective models to be tokenized and subsequently analysed. This GUI is not deployed and can be run via streamlit run aifrontend.py. Please note that the GUI has to be used with the saved models included.

### Running the GUI

To run the GUI:
1. Unzip AIGUI.zip
2. Install the necessary python modules in this environment 
3. Run the GUI using streamlit run aifrontend.py in the directory.

Please take note that model weights are required to be save so that the model are imported correctly.

## Final Model: Model Weights
Separately, model weights are saved to run the combined the model.

### Datasets Source
1. Step 1: https://github.com/sophialatessa/FakeNewsDeepLearning
2. Step 2: https://www.kaggle.com/datasets/mrisdal/fake-news

## Project Status
The project is currently complete!
