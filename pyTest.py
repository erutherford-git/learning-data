import bs4
import requests
import pandas as pd
import numpy as np
import boto3
from IPython.display import display
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)  # this will have all rows columns displayed

def get_basketball_stats(link='https://en.wikipedia.org/wiki/Michael_Jordan'):
    """
    This function was copied from the final assignment notebook for the edX course in
    python for data science
    :param link: we pass this function a wikipedia link for a basketball player
    :return: returns a dict with the information in the stats table
    """
    # read the webpage
    response = requests.get(link)
    # create a BeautifulSoup object to parse the HTML
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    # the player stats are defined  with the attribute CSS class set to 'wikitable sortable';
    # therefore we create a tag object "table"
    table = soup.find(class_='wikitable sortable')

    # the headers of the table are the first table row (tr) we create a tag object that has the first row
    headers = table.tr
    # the table column names are displayed  as an abbreviation; therefore we find all the abbr tags and returs an Iterator
    titles = headers.find_all("abbr")
    # we create a dictionary  and pass the table headers as the keys
    data = {title['title']: [] for title in titles}
    # we will store each column as a list in a dictionary, the header of the column will be the dictionary key

    # we iterate over each table row by fining each table tag tr and assign it to the objed
    for row in table.find_all('tr')[1:]:

        # we iterate over each cell in the table, as each cell corresponds to a different column we all obtain the correspondin key corresponding the column n
        for key, a in zip(data.keys(), row.find_all("td")[2:]):
            # we append each elment and strip any extra HTML contnet
            data[key].append(''.join(c for c in a.text if (c.isdigit() or c == ".")))

    # we remove extra rows by finding the smallest list
    Min = min([len(x) for x in data.values()])
    # we convert the elements in the key to floats
    for key in data.keys():
        data[key] = list(map(lambda x: float(x), data[key][:Min]))

    return data


# contains the links for the basketball players' wikipedia pages
links = ['https://en.wikipedia.org/wiki/Michael_Jordan' \
    , 'https://en.wikipedia.org/wiki/Kobe_Bryant' \
    , 'https://en.wikipedia.org/wiki/LeBron_James' \
    , 'https://en.wikipedia.org/wiki/Stephen_Curry']
names = ['Michael Jordan', 'Kobe Bryant', 'Lebron James', 'Stephen Curry']

# here we create a dict for the stats of each basketball player
michael_jordan=get_basketball_stats(links[0])
kobe_bryant=get_basketball_stats(links[1])
lebron_james=get_basketball_stats(links[2])
steph_curry=get_basketball_stats(links[3])
# print(michael_jordan)

# The following code block creates a data frame from the dicts created above
mj_df = pd.DataFrame(michael_jordan)
kb_df = pd.DataFrame(kobe_bryant)
lj_df = pd.DataFrame(lebron_james)
sc_df = pd.DataFrame(steph_curry)
dframes = [mj_df, kb_df, lj_df, sc_df]
print(mj_df)

# prints the player name and their stats
'''
for i in range(4):
    print(names[i])
    print(dframes[i].head())
'''

plt.plot(mj_df[['Points per game']])
plt.xlabel('years')
plt.ylabel('Points per game')
plt.show()

# this saves the dataframe to a csv file
mj_df.to_csv('mj.csv')
