import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [21, 19, 22, 20],
    "City": ["Delhi", "Mumbai", "Ahmedabad", "Pune"]
}

df = pd.DataFrame(data)

print(df.head(2))

print(df.columns)

print(df.shape)

print(df.info())