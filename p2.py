import pandas as pd

df = pd.read_csv('movies.csv')

missingValues = df.isnull().sum

print("Missing Values: ")
print(missingValues)

df.fillna(df.mean(),inplace=True)
