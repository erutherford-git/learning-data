# In this file, we clean the data that we collected in the first one

import matplotlib as plt
from matplotlib import pyplot
import pandas as pd
import numpy as np

# Following code designates the path to the file and opens it
autos_path = 'C:\\users\\efrut\\Pycharmprojects\\AnalyzeDatawPython\\autostest.csv'
autos_frame = pd.read_csv(autos_path)
# print(autos_frame)
# print(autos_frame.dtypes) # shows data types
# print(autos_frame.describe(include="all")) # shows information about each column
# print(autos_frame.columns) # prints headers
# print(autos_frame[['length']].describe() # describes only length column

autos_frame.replace("?", np.nan, inplace = True)
# above we replace each ? with NaN (default python value) to make later steps easier
# print(autos_frame.head(5))

missing_data = autos_frame.isnull()
# Here we replace values with a bool that indicates if they are null or not
# print(missing_data)

'''
for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print("")  
# This loop prints out the number of missing values per column
'''

avg_norm_loss = autos_frame["normalized-losses"].astype("float").mean(axis=0)
# print("Average of normalized-losses:", avg_norm_loss)
autos_frame['normalized-losses'].replace(np.nan, avg_norm_loss, inplace=True)
# calculate mean of column and then replace the values

avg_bore = autos_frame['bore'].astype('float').mean(axis=0)
# print("Average of bore:", avg_bore)
autos_frame['bore'].replace(np.nan, avg_bore, inplace=True)
# calculate the mean and replace the values

avg_stroke = autos_frame['stroke'].astype('float').mean(axis=0)
autos_frame['stroke'].replace(np.nan, avg_stroke, inplace=True)
# calculate the mean and replace the values

avg_horsepower = autos_frame['horsepower'].astype('float').mean(axis=0)
autos_frame['horsepower'].replace(np.nan, avg_horsepower, inplace=True)

avg_peakrpm=autos_frame['peak-rpm'].astype('float').mean(axis=0)
autos_frame['peak-rpm'].replace(np.nan, avg_peakrpm, inplace=True)

# print(autos_frame['num-of-doors'].value_counts())
# we see that 4 doors are the most common
autos_frame['num-of-doors'].replace(np.nan, 'four', inplace=True)

autos_frame.dropna(subset=['price'], axis=0, inplace=True)
# we drop the rows with no price
autos_frame.reset_index(drop=True, inplace=True)
# we make sure to reset the indices because we dropped rows

autos_frame[["bore", "stroke"]] = autos_frame[["bore", "stroke"]].astype("float")
autos_frame[["normalized-losses"]] = autos_frame[["normalized-losses"]].astype("int")
autos_frame[["price"]] = autos_frame[["price"]].astype("float")
autos_frame[["peak-rpm"]] = autos_frame[["peak-rpm"]].astype("float")
autos_frame["horsepower"]=autos_frame["horsepower"].astype(int, copy=True)
# as we saw at the beginning, some of the columns are the wrong data type
# This block of code changes the data types to the appropriate values

autos_frame['length'] = autos_frame['length']/autos_frame['length'].max()
autos_frame['width'] = autos_frame['width']/autos_frame['width'].max()
autos_frame['height'] = autos_frame['height']/autos_frame['height'].max()
# now we normalize the length, width, height columns so none outweighs the other

'''
plt.pyplot.hist(autos_frame["horsepower"])
# set x/y labels and plot title
plt.pyplot.xlabel("horsepower")
plt.pyplot.ylabel("count")
plt.pyplot.title("horsepower bins")
pyplot.show()
# This gives us a histogram so we can see how horsepower is distributed
'''

bins = np.linspace(min(autos_frame["horsepower"]), max(autos_frame["horsepower"]), 4)
# creates the cutoffs for our bins
hp_names = ['Low', 'Medium', 'High']
autos_frame['horsepower-binned'] = pd.cut(autos_frame['horsepower'], bins, labels=hp_names, include_lowest=True)
# assign the rows to the correct bin
'''
pyplot.bar(hp_names, autos_frame['horsepower-binned'].value_counts())
plt.pyplot.xlabel("Horsepower")
plt.pyplot.ylabel("Count")
plt.pyplot.title("Horsepower binned counts")
pyplot.show()
# here we produce a graph that shows the results of our binning
'''
'''
plt.pyplot.hist(autos_frame["horsepower"], bins = 3)
plt.pyplot.xlabel("horsepower")
plt.pyplot.ylabel("count")
plt.pyplot.title("horsepower bins")
pyplot.show()
# another way to show the distribution
'''

fuel_dummy = pd.get_dummies(autos_frame['fuel-type'])
# print(fuel_dummy.head(100))
fuel_dummy.rename(columns={'fuel-type-diesel':'gas', 'fuel-type-diesel':'diesel'}, inplace=True)
# print(fuel_dummy.head())
autos_frame = pd.concat([autos_frame, fuel_dummy], axis=1)
# merge auto_frame with fuel_dummy
autos_frame.drop("fuel-type", axis=1, inplace=True)
# drop the original fuel-type column

aspiration_dummy = pd.get_dummies(autos_frame['aspiration'])
aspiration_dummy.rename(columns={'std':'aspiration-std', 'turbo': 'aspiration-turbo'}, inplace=True)
# print(aspiration_dummy)
autos_frame = pd.concat([autos_frame, aspiration_dummy], axis=1)
autos_frame.drop('aspiration', axis=1, inplace=True)

autos_frame.to_csv('C:\\users\\efrut\\Pycharmprojects\\AnalyzeDatawPython\\autostestClean.csv')
print("hello")

