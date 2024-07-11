import pickle
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.feature_extraction.text import TfidfVectorizer

def mainpreprocess():
    with open(r"C:\Users\deepa\OneDrive\Desktop\Aishu\fake_account_detector\myproject\myapp\FAKE_ACC\trained_model.pkl", 'rb') as model_file:
        model = pickle.load(model_file)

    def preprocess_data(input_data):
        text_columns = ['Username', 'Full Name', 'Bio']
        imputer = SimpleImputer(strategy='constant', fill_value="aa")
        input_data[text_columns] = imputer.fit_transform(input_data[text_columns])
        vectorizers = {}

        for column in text_columns:
            vectorizer = TfidfVectorizer()
            input_data[column] = vectorizer.fit_transform(input_data[column]).toarray()
            vectorizers[column] = vectorizer


        input_data = input_data[input_data.columns]
        y_pred = model.predict(input_data)
        return y_pred 

    input_data = pd.read_csv(r'C:\Users\deepa\OneDrive\Desktop\Aishu\fake_account_detector\myproject\myapp\FAKE_ACC\instagram_user_data.csv')
    return preprocess_data(input_data)