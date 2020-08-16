
import pandas as pd

# data = pd.read_csv('./20170930.csv')
data = pd.read_csv('./20170930.csv', sep=";", encoding='latin-1', nrows=1000, skiprows=[2,4])

# print(data)

print(data.shape)
print(data.describe())
print(data.head(2))

