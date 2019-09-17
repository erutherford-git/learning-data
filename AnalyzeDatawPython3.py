import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sys
import scipy.stats as stats

pd.set_option('display.max_column',None)
pd.set_option('display.max_rows',None)
pd.set_option('display.max_seq_items',None)
pd.set_option('display.max_colwidth', 500)
pd.set_option('expand_frame_repr', True)

# here we want to open our new csv that has been cleaned
autos_path = 'C:\\users\\efrut\\Pycharmprojects\\AnalyzeDatawPython\\autostestClean.csv'
autos_frame = pd.read_csv(autos_path)

# we can check how many of each value we have for categorical variables
print(autos_frame['drive-wheels'].value_counts())

# we can use a box plot to see how price varies by drivetrain
# sns.boxplot(x='drive-wheels', y='price', data=autos_frame)
# remember to show the graph!
# plt.show()

# We can also use a scatter plot to show two continuous variables
'''
scatter_xaxis = autos_frame['engine-size']
scatter_yaxis = autos_frame['price']
plt.scatter(scatter_xaxis, scatter_yaxis)
plt.title('Price vs engine size')
plt.xlabel('engine size')
plt.ylabel('price')
plt.show()
# note pycharm will only pull up one at a time - the second will appear when the first is exited
'''

# suppose we want to know avg price and how it differs by body styles and drive systems
autos_test = autos_frame[['body-style', 'drive-wheels', 'price']]
autos_group = autos_test.groupby(['drive-wheels', 'body-style'], as_index=False).mean()
print(autos_group)
# data grouped by category and only average price of each subcategory is shown
# however this is kinda hard to read

autos_pivot = autos_group.pivot(index='drive-wheels', columns='body-style')
# using the sys stdout write we can print the whole dataframe, but it must be converted to a string first
# sys.stdout.write(autos_pivot.to_string())
print(autos_pivot)

# we can convert that pivot table to a heat map
# plt.pcolor(autos_pivot, cmap='RdBu')
# plt.colorbar()
# plt.show()

# we can also use seaborn to make the heatmap
# sns.heatmap(autos_pivot)
# plt.show()

''' # unable to get the anova working, not sure what the problem is - will return later
anova_df = autos_frame[['make', 'price']]
anova_df_grouped = anova_df.groupby(['make'])
# anova_1 = stats.f_oneway(anova_df_grouped.get_group('honda'['price']), anova_df_grouped.get_group('subaru'['price']))
print(anova_df_grouped)
'''

# lets look at the correlation between engine size and price
sns.regplot(x='engine-size', y='price', data=autos_frame)
plt.ylim(0,)
plt.show()

# Pearson correlation
pearson_coef = stats.pearsonr(autos_frame['horsepower'], autos_frame['price'])
print(pearson_coef)

# here we can create a heatmap that shows the correlations between the variables. Pretty cool!
correlations = autos_frame.corr()
sns.heatmap(correlations, xticklabels=correlations.columns, yticklabels=correlations.columns, annot=False)
plt.show()


