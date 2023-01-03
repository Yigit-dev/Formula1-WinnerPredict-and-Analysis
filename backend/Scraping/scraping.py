import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from selenium import webdriver
import sqlite3
import random
from datetime import datetime

#Attention!! The given path is set according to the developer, you need to set the path according to yourself and make sure that it is correct.
db = sqlite3.connect('E:\\Formula1-WinnerPredict-and-Analysis\\backend\\db.sqlite3') 
cursor = db.cursor()

def SaveToDatabase(data, table):
    id = int(datetime.now().microsecond) * random.randint(1,1000)
    cursor.execute(f"INSERT INTO {table} VALUES(?,?)", [id, data])
    db.commit()

def team_table():
    cols = []
    col_check = False
    # create team dataframe
    team_df = pd.DataFrame()

    # pulling data between 1958 and 2022
    for year in range(1958,2022): 
        # pulling team data table
        link = f'https://www.formula1.com/en/results.html/{year}/team.html' 
        req = requests.get(link)
        soup = BeautifulSoup(req.text, 'lxml')
        # pull raw df from formula1 web site
        raw_df = soup.find("table", class_="resultsarchive-table") 
        
        # pull column data from formula1 website data table 
        if(not col_check):
            # loop in html table "th" and pull all columns
            for col_name in raw_df.find_all("th"):
                if(len(col_name.text)==0):
                    continue
                else:
                    item = col_name.text
                    cols.append(item)
            col_check = True
            cols.append('Year')
            # adding column data as a column to the generated dataframe
            team_df = pd.DataFrame(columns=cols)
        
        # collecting row data from tr and td tag on website
        for data in raw_df.find_all('tr')[1:]:
            row_data = data.find_all('td')
            row_data = [i.text for i in row_data]
            row_data.pop()
            row_data.pop(0)
            row_data = [x.replace("\n"," ") for x in row_data]
            row_data = [y.strip() for y in row_data]
            # pull data year
            year_info = soup.find("h1", class_="ResultsArchiveTitle")
            year_info = year_info.text
            year_info = year_info.replace("\n", " ").strip()
            row_data.append(year_info)
            # add row data in team dataframe table
            team_df.loc[len(team_df)] = row_data

    return team_df

def races_table():
    cols = []
    col_check = False
    # create races dataframe
    races_df = pd.DataFrame()

    # pulling data between 1958 and 2022
    for year in range(1958,2022):
        # pulling races data table
        link = f'https://www.formula1.com/en/results.html/{year}/races.html'
        req = requests.get(link)
        soup = BeautifulSoup(req.text, 'lxml')
        # pull raw df from formula1 web site
        raw_df = soup.find("table", class_="resultsarchive-table") 
        
        # pull column data from formula1 website data table 
        if(not col_check):
            # loop in html table "th" and pull all columns
            for col_name in raw_df.find_all("th"):
                if(len(col_name.text)==0):
                    continue
                else:
                    item = col_name.text
                    cols.append(item)
            col_check = True
            cols.append('Year')
            # adding column data as a column to the generated dataframe
            races_df = pd.DataFrame(columns=cols)
        
        # collecting row data from tr and td tag on website
        for data in raw_df.find_all('tr')[1:]:
            row_data = data.find_all('td')
            row_data = [i.text for i in row_data]
            row_data.pop()
            row_data.pop(0)
            row_data = [x.replace("\n"," ") for x in row_data]
            row_data = [y.strip() for y in row_data]
            # pull data year
            year_info = soup.find("h1", class_="ResultsArchiveTitle")
            year_info = year_info.text
            year_info = year_info.replace("\n", " ").strip()
            row_data.append(year_info)
            # add row data in team dataframe table
            races_df.loc[len(races_df)] = row_data
    
    # split date column as day, month, year
    new = races_df["Date"].str.split(" ", n = 2, expand = True)
    races_df["Day"] = new[0].astype(str).astype(int)
    races_df["Month"] = new[1]
    races_df["Year"] = new[2].astype(str).astype(int)

    return races_df

def drivers_table():
    cols = []
    col_check = False
    # create drivers dataframe
    drivers_df = pd.DataFrame()

    # pulling data between 1958 and 2022
    for year in range(1958,2022):
        # pulling drivers data table
        link = f'https://www.formula1.com/en/results.html/{year}/drivers.html'
        req = requests.get(link)
        soup = BeautifulSoup(req.text, 'lxml')
        # pull raw df from formula1 web site
        raw_df = soup.find("table", class_="resultsarchive-table")
        
        # pull column data from formula1 website data table 
        if(not col_check):
            # loop in html table "th" and pull all columns
            for col_name in raw_df.find_all("th"):
                if(len(col_name.text)==0):
                    continue
                else:
                    item = col_name.text
                    cols.append(item)
            col_check = True
            cols.append('Year')
            # adding column data as a column to the generated dataframe
            drivers_df = pd.DataFrame(columns=cols)
        
        # collecting row data from tr and td tag on website
        for data in raw_df.find_all('tr')[1:]:
            row_data = data.find_all('td')
            row_data = [i.text for i in row_data]
            row_data.pop()
            row_data.pop(0)
            row_data = [x.replace("\n"," ") for x in row_data]
            row_data = [y.strip() for y in row_data]
            # pull data year
            year_info = soup.find("h1", class_="ResultsArchiveTitle")
            year_info = year_info.text
            year_info = year_info.replace("\n", " ").strip()
            row_data.append(year_info)
            # add row data in team dataframe table
            drivers_df.loc[len(drivers_df)] = row_data
    return drivers_df

def wikipedia_table():
    # pull 'season,country,latitude,longitude and url' datas from api
    races_table = {'season': [], 'country': [], 'lat': [], 'long': [], 'url': []}

    # pulling data between 1958 and 2022
    for year in list(range(1958,2022)):
        link = 'https://ergast.com/api/f1/{}.json'
        req = requests.get(link.format(year))
        # pulls data as json
        json = req.json()

        # converting json data to dataframe data
        for i in json['MRData']['RaceTable']['Races']:
            try:
                races_table['season'].append(int(i['season']))
            except:
                races_table['season'].append(None)

            try:
                races_table['country'].append(i['Circuit']['Location']['country'])
            except:
                races_table['country'].append(None)

            try:
                races_table['lat'].append(float(i['Circuit']['Location']['lat']))
            except:
                races_table['lat'].append(None)

            try:
                races_table['long'].append(float(i['Circuit']['Location']['long']))
            except:
                races_table['long'].append(None)

            try:
                # url: wikipedia links containing the information of the races according to the competition names
                races_table['url'].append(i['url'])
            except:
                races_table['url'].append(None)
            
    races_table = pd.DataFrame(races_table)
    # rename races table columns
    races_table = races_table.rename(columns={'season':'Season','lat':'Lattitude','long':'Longitude','country':'Country','url':'Url'})

    return races_table

def weather_table():
    # get the season, country and lattitude columns from the races table to pull the weather data
    races_table = wikipedia_table()
    weather = races_table.iloc[:,[0,1,2]]

    # weather information of the formula1 competitions
    info = []

    # read wikipedia tables

    for url in races_table.Url:
        try:
            data = pd.read_html(url)[0]
            if 'Weather' in list(data.iloc[:,0]):
                n = list(data.iloc[:,0]).index('Weather')
                info.append(data.iloc[n,1])
            else:
                data = pd.read_html(url)[1]
                if 'Weather' in list(data.iloc[:,0]):
                    n = list(data.iloc[:,0]).index('Weather')
                    info.append(data.iloc[n,1])
                else:
                    data = pd.read_html(url)[2]
                    if 'Weather' in list(data.iloc[:,0]):
                        n = list(data.iloc[:,0]).index('Weather')
                        info.append(data.iloc[n,1])
                    else:
                        data = pd.read_html(url)[3]
                        if 'Weather' in list(data.iloc[:,0]):
                            n = list(data.iloc[:,0]).index('Weather')
                            info.append(data.iloc[n,1])
                        else:
                            driver = webdriver.Chrome()
                            driver.get(url)

                            # click language button
                            button = driver.find_element_by_url_text('Italiano')
                            button.click()
                            
                            # find weather in italian with selenium
                            climate = driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[1]/tbody/tr[9]/td').text
                            info.append(climate) 
                                    
        except:
            info.append('not found')

    weather['weather'] = info

    # classifying weather information as 'warm, cold, dry, wet and cloudy'
    weather_dict = {'weather_warm': ['soleggiato', 'clear', 'warm', 'hot', 'sunny', 'fine', 'mild', 'sereno'],
                'weather_cold': ['cold', 'fresh', 'chilly', 'cool'],
                'weather_dry': ['dry', 'asciutto'],
                'weather_wet': ['showers', 'wet', 'rain', 'pioggia', 'damp', 'thunderstorms', 'rainy'],
                'weather_cloudy': ['overcast', 'nuvoloso', 'clouds', 'cloudy', 'grey', 'coperto']}

    # map new data according to weather dictionary and create dataframe
    weather_data = pd.DataFrame(columns = weather_dict.keys())
    for col in weather_data:
        weather_data[col] = weather['weather'].map(lambda x: 1 if any(i in weather_dict[col] for i in x.lower().split()) else 0)
    
    weather_info = pd.concat([weather, weather_data], axis = 1)

    return weather_info


def general_races_data():
    # concat races data and weather data
    races_data = pd.concat([races_table(), weather_table()], axis=1)
    
    return races_data

def ConvertToJSON(table, database):
    convertedData = table.to_json(orient = "records")
    SaveToDatabase(convertedData, f"formula1_{database}")

ConvertToJSON(team_table(), "teams")
ConvertToJSON(races_table(), "races")
ConvertToJSON(drivers_table(), "drivers")
ConvertToJSON(general_races_data(), "formula1")
