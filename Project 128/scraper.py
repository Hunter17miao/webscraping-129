from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

#make a page request with request module
wikiData = requests.get(START_URL)
time.sleep(10)

#get all the tables of page with find_all method()
tables = soup.find_all('table')

#create an empty list
td_rows = []

#for loop to take out all the td tags
    for table in tables:
        #get all the <td> tags from the table
        rows = table.find_all('td')
        for row in rows:
            striped_row = row.strip("td")
            #keep all of the td rows in the empty list
            td_rows.append(striped_row)
print(td_rows)

Rows_data = []
for i in range(0,len(td_rows)):
    Star_name = td_rows(i[0])
    Radius = td_rows(i[9])
    Mass = td_rows(i[8])
    Distance = td_rows(i[5])

    row_data = [Star_name, Radius, Mass, Distance]
    Rows_data.append(row_data)


# convert list to pandas dataframe
df= pd.Dataframe(Rows_data)
#save into csv
df.to_csv('brown_dwarfs_data.csv', index=False)




