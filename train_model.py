# -*- coding: utf-8 -*-
"""Titanicsurvibal.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WzF3YgojzqgDU2NwZ1ATMSwB5b22Rto4

# __Project Title:__ Analysis and prediction of Titanic Dataset to sorts of people who more likely survived

# __Problem Statement__
In this challenge, we ask you to build a predictive model that answers the question: “what sorts of people were more likely to survive?” using passenger data (ie name, age, gender, socio-economic class, etc).

# Dataset Overview
## About this file
The sinking of the Titanic is one of the most infamous shipwrecks in history.

On April 15, 1912, during her maiden voyage, the widely considered “unsinkable” RMS Titanic sank after colliding with an iceberg. Unfortunately, there weren’t enough lifeboats for everyone on board, resulting in the death of 1502 out of 2224 passengers and crew.

While there was some element of luck involved in surviving, it seems some groups of people were more likely to survive than others.

# Running Dependies
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# For Spliting and fine tuning
from sklearn.model_selection import train_test_split, GridSearchCV

''' for label encoding and transformation,
For standaring of data use standard scaler
for binary transformation we use on hot encoding
'''
from sklearn.preprocessing import LabelEncoder, StandardScaler, OneHotEncoder

# for Evaluation model
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

# for saving model
import pickle
import joblib

# for avoid unwanted Warning
import warnings
warnings.filterwarnings('ignore')

"""## Loading Dataset"""

# reading file using pandas

df = pd.read_csv('/content/Titanic-Dataset.csv')

# To Print First Five Ro
df.head()

"""Apply EDA"""

# To print Volume Of data
df.shape

# To Print Desciption (Buera)
df.info()

# To Print Mathematical Description
df.describe()

# To Check Null value
df.isna().sum()

"""In tis dataset there is a noise and biaseness has present in the following colun: Age, Cabin, Embarked .

    Hence Data Cleaning is Required Here

# Applying Data Cleaning
"""

# Handling missing Vlaue
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Cabin'] = df['Cabin'].fillna(df['Cabin'].mode()[0])
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

df.isna().sum()

"""# Feature Enginnering"""

# To Select Need ColumnS
df=df[['Pclass','Sex', 'Fare' ,'Survived' ]]

"""# Label Encoding"""

# Change String Data value to Numeric
le = LabelEncoder()
df['Sex'] = le.fit_transform(df['Sex'])

"""# Feature Selction"""

# Data Selection Feature(X) and Target(y)
X = df.drop('Survived' , axis=1)
y= df['Survived']

"""# Data Training, testing and Spliting"""

# Data Training and testing
X_train , X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 42)

"""# Fine Tuning"""

# applying hyperparametertuning to increase the Accuracy
param_grid = {
    'n_estimators':[50 , 100],
    'max_depth':[3, 5, 7],
    'min_samples_split':[2, 5]
}

# Model Creating
from sklearn.ensemble import RandomForestClassifier

grid = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=5)
grid.fit(X_train, y_train)

"""# Model Evaluation"""

# Best Model Evaluation
best_model = grid.best_estimator_
y_pred = best_model.predict(X_test)
print(f"Best Model Accuracy: {accuracy_score(y_test, y_pred)*100:2f}%")

# Feature Importance plot

importance = best_model.feature_importances_
feature = X.columns
sns.barplot(x=importance, y=feature)
plt.title("Feature Importance")
plt.xlabel("Importance")
plt.ylabel("Feature")
plt.tight_layout()
plt.show()

"""# Save Model

# Checking model from user input
"""

# 10. Take user input explicitly
print("\n🔍 Predict Survival for a New Passenger\n")
pclass = int(input("Enter Pclass (1, 2, or 3): "))
sex_input = input("Enter Sex (male/female): ").strip().lower()
age = float(input("Enter Age: "))
fare = float(input("Enter Fare: "))

# Convert sex to numeric
sex = le.transform([sex_input])[0] if sex_input in ['male', 'female'] else 1

# Prepare input
user_data = pd.DataFrame([[pclass, sex,  fare]], columns=['Pclass', 'Sex', 'Fare'])
prediction = best_model.predict(user_data)[0]

# Output
print("\n✅ Survival Prediction:", "Survived ✅" if prediction == 1 else "Did Not Survive ❌")

"""# Save model"""

# Save Model
joblib.dump(best_model, 'titanic_model.joblib')
print("Model saved as  'titanic_model.joblib' .")

