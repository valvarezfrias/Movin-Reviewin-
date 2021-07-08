import requests
import json
import pprint
import pandas as pd
import csv
import sqlalchemy
from sqlalchemy import create_engine
import os
import matplotlib
import matplotlib.pyplot as plt
import random

def main():
    cities = {
          '41620': 'Salt Lake, Utah',
          '19740': 'Denver, Colorado',
          '21340': 'El Paso, Texas',
          '38060': 'Phoenix, Arizona',
          '38300': 'Pittsburg, Pennsylvania'
          }
    occupation = {
              '151251': 'Computer Programmer',
              '291228': 'Physicians',
              '472181': 'Roofers',
              '412031': 'Retail Salespersons',
              '333021': 'Detectives and Criminal Investigators'
             }

    inputCity = displayCities(cities)
    inputCityValue = cities.get(inputCity)
    inputOcup = displayOccupation(occupation)
    inputOcupValue = occupation.get(inputOcup)
    #userDataFrame = userInfoApiRequest(inputCity, inputOcup)
    
    #API REQUEST FUNCTION######################################
    job = inputOcupValue
    dataDict = {}
    wage = 41.48
    city = inputCityValue
    for var in ["job", "wage", "city"]:
        dataDict[var] = eval(var)
    df = pd.DataFrame(dataDict, index=[0])#usersdataframe
    ##############################################################
    visualsdf = informationDataFrame()
    createDatabase(visualsdf)
    
    randomDF = randUserDataFrame(inputCityValue, inputOcupValue,visualsdf)
    final = df.append(randomDF,ignore_index=True)#usersdataframe
    barChart(final)
    
    
    
    
def displayCities(city):
  print("Key\tCity/State")
  for keys, values in city.items():
      print(keys, ":", values)
  flag = False
  while flag == False:
    key = input("Please enter a key: ")
    if key in city.keys():
      return key
      

def displayOccupation(ocup):
    print("Key\tOccupation")
    for keys, values in ocup.items():
        print(keys, ":", values)
    flag = False
    while flag == False:
      key = input("Please enter a key: ")
      if key in ocup.keys():
        return key
      
def userInfoApiRequest(inputCity, inputOcup):
    url = 'https://api.bls.gov/publicAPI/v1/timeseries/data/OEUM00'+ inputCity + '000000' + inputOcup + '03' # occupation and salary
    #R is a dictionary
    r = requests.get(url).json()
    status = r["status"]
    hourly = r["Results"]["series"][0]["data"][0]["value"]
    dataDict = {}
    for var in ["hourly", "inputCity"]:
        dataDict[var] = eval(var)
    df = pd.DataFrame(dataDict, index=[0])
    return df
    
def informationDataFrame():
    # reads csv file and turns it into a dataframe
    vdf = pd.read_csv("visual_info.csv")
    return vdf
  
def randomIndex(userInputCity, userInputOccupation, vdf):
    randomInt = random.randint(0, 24)
    flag = False
    while flag == False:
        if vdf.at[randomInt, 'city'] != userInputCity and vdf.at[randomInt, 'occupation'] == userInputOccupation:
            job = vdf.at[randomInt, 'occupation']
            wage = vdf.at[randomInt, 'value']
            city = vdf.at[randomInt, 'city']
            a_dict = {}
            for variable in ["job", "wage", "city"]:
                a_dict[variable] = eval(variable)
            return a_dict
        else:
            randomInt = random.randint(0, 24)

def randUserDataFrame(inputCityValue, inputOcupValue,visualsdf):
    arr = []
    for i in range(2):
        dictionary = randomIndex(inputCityValue, inputOcupValue, visualsdf)
        arr.append(dictionary)
    df1 = pd.DataFrame(arr[0], index=[0])
    df2 = pd.DataFrame(arr[1], index=[0])
    result = df1.append(df2,ignore_index=True)
    return result
    
def barChart(final):
    x_axis = final["city"]
    y_axis = final["wage"]
    plt.bar(x_axis, y_axis, color=['pink', 'blue', 'yellow'])
    plt.title(final.at[0,"job"])
    plt.xlabel("Cities")
    plt.ylabel("Hourly Wage")
    plt.show()


def createEngine():
    engine = create_engine('mysql://root:codio@localhost/visual')
    return engine
  
def createDatabase(vdf):
    engine = createEngine()
    vdf.to_sql('information', con=engine, if_exists='replace', index=False)

def createSQLfile():
    #creates database into sql file
    os.system("mysqldump -u root -pcodio visual > visual_info.sql")
    
    
############################
#                          #
#     Main Driver Code     #
#                          #
############################  
if __name__ == '__main__':
  main()