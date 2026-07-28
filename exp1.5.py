from sklearn.datasets import load_iris
import pandas as pd
iris = load_iris()
df = pd.DataFrame(
iris.data,
columns=iris.feature_names
)
df["target"] = iris.target
print("First Five Records:")
print(df.head())
print("\nNumber of Rows and Columns:")
print(df.shape)
print("\nColumn Names:")
print(df.columns)
print("\nMissing Values:")
print(df.isnull().sum())
print("\nSummary Statistics:")
print(df.describe())
print("\nSamples in Each Class:")
print(df["target"].value_counts())
