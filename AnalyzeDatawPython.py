import pandas as pd


url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors" \
           , "body-style", "drive-wheels", "engine-location", "wheel-base", "length", "width", "height" \
           , "curb-weight", "engine-type", "num-of-cylinders", "engine-size", "fuel-system", "bore" \
           , "stroke", "compression-ratio", "horsepower", "peak-rpm", "city-mpg", "highway-mpg", "price"]

df = pd.read_csv(url, header=None)
df.columns = headers
#print(df)
df.dropna(subset=["price"], axis=0) # drops missing values along price column
df.to_csv('autostest.csv')

# This file reads in the data from the UCI website and saves it as a csv file
