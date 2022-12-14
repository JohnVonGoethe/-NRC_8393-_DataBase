import glob 
import pandas as pd 
import xml.etree.ElementTree as ET 
from datetime import datetime
import requests
from zipfile import ZipFile


def get_data():
    # Define the remote file to retrieve
    remote_url = 'http://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Lab%20-%20Extract%20Transform%20Load/data/datasource.zip'
    # Define the local filename to save data
    local_file = 'datasource.zip'
    # Make http request for remote file data
    data = requests.get(remote_url)
    # Save file data to local copy
    with open(local_file, 'wb') as f:
        f.write(data.content)
    with ZipFile(local_file, 'r') as zipObj:
        # Extract all the contents of zip file in different directory
        zipObj.extractall('dealership_data')

def extract_from_csv(file_to_process): 
    dataframe = pd.read_csv(file_to_process) 
    return dataframe

def extract_from_json(file_to_process):
    dataframe = pd.read_json(file_to_process, lines=True)
    return dataframe

def extract_from_xml(file_to_process):
    dataframe = pd.DataFrame(columns=['car_model','year_of_manufacture','price', 'fuel'])
    tree = ET.parse(file_to_process) 
    root = tree.getroot() 
    for person in root: 
        car_model = person.find("car_model").text 
        year_of_manufacture = int(person.find("year_of_manufacture").text)
        price = float(person.find("price").text) 
        fuel = person.find("fuel").text 
        dataframe = dataframe.append({"car_model":car_model, "year_of_manufacture":year_of_manufacture, "price":price, "fuel":fuel}, ignore_index=True) 
    return dataframe
    
def extract():
    extracted_data = pd.DataFrame(columns=['car_model','year_of_manufacture','price', 'fuel']) 
    #for csv files
    for csvfile in glob.glob("dealership_data/*.csv"):
        extracted_data = extracted_data.append(extract_from_csv(csvfile), ignore_index=True)
    #for json files
    for jsonfile in glob.glob("dealership_data/*.json"):
        extracted_data = extracted_data.append(extract_from_json(jsonfile), ignore_index=True)
    #for xml files
    for xmlfile in glob.glob("dealership_data/*.xml"):
        extracted_data = extracted_data.append(extract_from_xml(xmlfile), ignore_index=True)
    return extracted_data
   
def transform(data):
    data['price'] = round(data.price, 2)
    return data

def load(targetfile, data_to_load):
    data_to_load.to_csv(targetfile)

def log(logfile, message):
    timestamp_format = '%H:%M:%S-%h-%d-%Y'
    #Hour-Minute-Second-MonthName-Day-Year
    now = datetime.now() # get current timestamp
    timestamp = now.strftime(timestamp_format)
    with open(logfile,"a") as f: 
        f.write('[' + timestamp + ']: ' + message + '\n')
        print(message)


if __name__ == '__main__':

    logfile    = "dealership_logfile.txt"            # all event logs will be stored
    targetfile = "dealership_transformed_data.csv"   # transformed data is stored

    log(logfile, "Download Used Car Data")
    get_data()
    
    log(logfile, "ETL Job Started")

    log(logfile, "Extract phase Started")
    extracted_data = extract() 
    log(logfile, "Extract phase Ended")

    log(logfile, "Transform phase Started")
    transformed_data = transform(extracted_data)
    log(logfile, "Transform phase Ended")

    log(logfile, "Load phase Started")
    load(targetfile, transformed_data)
    log(logfile, "Load phase Ended")

    log(logfile, "ETL Job Started")