import pandas as pd

data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor"],
    "Price": [50000, 500, 1500, 12000],
    "Quantity": [5, 20, 15, 7]
}

df = pd.DataFrame(data)

print(df["Product"])

print(df[["Product", "Price"]])

print(df[df["Price"] > 1000])

print(df[df["Quantity"] < 10])

print(df[(df["Price"] > 1000) & (df["Quantity"] < 10)])