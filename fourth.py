import pandas as pd

df4 = pd.read_csv("/kaggle/input/datasets/yasserh/titanic-dataset/Titanic-Dataset.csv")

print(df4.head(10))
print(df4.shape)
print(df4.columns)
print(df4.isna().sum())
print(df4.describe())