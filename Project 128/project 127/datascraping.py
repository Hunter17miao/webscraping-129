from bs4 import BeautifulSoup
import time
import pandas as pd

URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser = webdriver.Chrome()
browser.get(URL)


scraped_data = []


def scrape():

    for i in range():
        print()

    bright_star_table = soup.find("table", attrs={"class", "wikitable"})

    table_body = bright_star_table.find("tbody")

    table_rows = table_body.find_all("tr")

    for rows in table_rows:
        table_cols = rows.find_all("td")
        print(table_cols)

        temp_list = []
        for col_data in table_cols:

         print(cols_data.text)

            data = col_data.text.strip()

            temp_list.append(data)

            scraped_data.append(temp_list)

star_data= []

for i in range(0,len(scraped_data)):

    Star_names= scraped_data(i[1])
    Distance= scraped_data(i[3])
    Mass= scraped_data(i[5])
    Radius= scraped_data(i[7])
    Lum= scraped_data(i[9])

    required_data= [Star_names, Distance, Mass, Radius, Lum]
    star_data.append(required_data)

star_df_1= pd.Dataframe(star_data, columns= headers)
headers = ["Star_names", "Distance", "Mass", "Radius", "Luminosity"]

scrape()

star_df_1.to_csv('scraped_data.csv',index=True, index_label="id")
