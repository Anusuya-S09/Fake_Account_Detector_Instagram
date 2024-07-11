import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.impute import SimpleImputer
import pickle

users_data = pd.read_csv(r"C:\Users\deepa\OneDrive\Desktop\Aishu\fake_account_detector\myproject\myapp\FAKE_ACC\users.csv")
fusers_data = pd.read_csv(r"C:\Users\deepa\OneDrive\Desktop\Aishu\fake_account_detector\myproject\myapp\FAKE_ACC\fusers.csv", encoding='ISO-8859-1')
users_data['Label'] = 0
fusers_data['Label'] = 1
combined_data = pd.concat([users_data, fusers_data], ignore_index=True)
text_columns = ['Username', 'Full Name','Bio']
imputer = SimpleImputer(strategy='constant', fill_value='aa')
combined_data[text_columns] = imputer.fit_transform(combined_data[text_columns])


combined_data[text_columns] = combined_data[text_columns].astype(str)
X = combined_data.drop(columns=['Label'])  # Features
y = combined_data['Label']                # Target variable

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

vectorizers = {}
for column in text_columns:
    vectorizer = TfidfVectorizer()
    X_train[column] = vectorizer.fit_transform(X_train[column]).toarray()
    X_test[column] = vectorizer.transform(X_test[column]).toarray()
    vectorizers[column] = vectorizer


X_train = X_train[X.columns]
X_test = X_test[X.columns]
imputer = SimpleImputer(strategy='constant', fill_value=0)
X_train = imputer.fit_transform(X_train)
X_test = imputer.transform(X_test)

classifier = RandomForestClassifier(random_state=42)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
print(report)


with open(r"C:\Users\deepa\OneDrive\Desktop\Aishu\fake_account_detector\myproject\myapp\FAKE_ACC\trained_model.pkl", 'wb') as model_file:
    pickle.dump(classifier, model_file)
    print("Model saved")