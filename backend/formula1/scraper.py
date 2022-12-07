import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_data_detail():

    columns = []
    column_check = False
    df = pd.DataFrame()

    for year in range(1950,2022):
        url = f'https://www.formula1.com/en/results.html/{year}/team.html'
        pageReq = requests.get(url)
        bSoup = BeautifulSoup(pageReq.text, 'lxml')
        raw_data = bSoup.find("table", class_="resultsarchive-table")

        if(not column_check):
            for column_name in raw_data.find_all("th"):
                if(len(column_name.text)==0):
                    continue
                else:
                    item = column_name.text
                    columns.append(item)
            column_check = True
            columns.append('Year')
            df = pd.DataFrame(columns=columns)

        for data in raw_data.find_all('tr')[1:]:
            row_data = data.find_all('td')
            row_data = [i.text for i in row_data]
            row_data.pop()
            row_data.pop(0)
            row_data = [x.replace("\n"," ") for x in row_data]
            row_data = [y.strip() for y in row_data]
            year_info = bSoup.find("h1", class_="ResultsArchiveTitle")
            year_info = year_info.text
            year_info = year_info.replace("\n", " ").strip()
            row_data.append(year_info)
            df.loc[len(df)] = row_data

    return print(requests.df)

    # if __name__ == '__main__':
    #     get_data_detail()
