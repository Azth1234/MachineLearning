import pandas as pd
data = {
"Product": ["Laptop", "Mouse", "Keyboard", "Monitor"],
"Price": [50000, 500, 1200, 10000],
"Quantity": [10, 50, 30, 15]
}
df = pd.DataFrame(data)
df["Total Value"] = df["Price"] * df["Quantity"]
print("DataFrame:")
print(df)
print("\nProduct with Highest Total Value:")
print(df.loc[df["Total Value"].idxmax()])
print("\nOverall Inventory Value:")
print(df["Total Value"].sum())
