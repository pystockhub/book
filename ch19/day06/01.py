import pandas as pd

df = pd.read_html("./table.html")[0]
print(df)
print(df.ix[0])
print(df.ix[1])
print(df[0])
