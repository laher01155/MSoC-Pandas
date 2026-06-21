import pandas as pd

df = pd.read_csv("/kaggle/input/datasets/yasserh/titanic-dataset/Titanic-Dataset.csv")

print(df[df["Sex"] == "female"])

print(df[df["Age"] > 30])

print(df[df["Survived"] == 1])

print(df[(df["Sex"] == "female") & (df["Survived"] == 1)])

print(df["Age"].mean())

print(df[df["Age"] == df["Age"].max()])