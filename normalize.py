import pandas as pd
from sklearn import preprocessing


# method 1: bring the data between 0 and 1
df = pd.DataFrame((range(5), range(6, 11)), columns=['a', 'b'])
# Create a minimum and maximum processor object
min_max_scaler = preprocessing.MinMaxScaler()
# Create an object to transform the data to fit minmax processor
df_scaled = min_max_scaler.fit_transform(df)
# Run the normalizer on the dataframe
df_norm = pd.DataFrame(df_scaled, columns=df.columns)
df_norm.head(5)

# method2: bring the data to a unit normal distribution
df_stand = preprocessing.scale(df)
