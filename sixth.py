import pandas as pd

df = pd.read_csv("/kaggle/input/datasets/yasserh/titanic-dataset/Titanic-Dataset.csv")

# Survival rate by gender
print(df.groupby("Sex")["Survived"].mean() * 100)

# Average age by passenger class
print(df.groupby("Pclass")["Age"].mean())

# Number of passengers in each class
print(df.groupby("Pclass").size())

# Class with highest survival rate
print(df.groupby("Pclass")["Survived"].mean().idxmax())

# Average fare paid by each class
print(df.groupby("Pclass")["Fare"].mean())