import requests
import json
import pandas as pd
import csv

# ----------------------------------------------Asteroid image of the day display----------------------------------------------

# API and parameters
base_url="https://api.nasa.gov/planetary/apod"
api_key = ""

params={
    "api_key": api_key,
}

# Making a request
response=requests.get(base_url,params=params)

# If the answer is 'ok'
if response.status_code == 200:

    # Store the result in a json file
    result = response.json()
    
    # Print the image of the day url only
    print(f"APOD link: {result["url"]}")
else:
    print(f"Invalid resquest. Error {response.status_code}.")

# ----------------------------------------------Near Earth Object Data----------------------------------------------

# API and parameters
base_url="https://api.nasa.gov/neo/rest/v1/feed"
start_date= "2025-08-24"
end_date = "2025-08-25"

params={
    "api_key": api_key,
    "start_date": start_date,
    "end_date": end_date,
}

# Making a request
response=requests.get(base_url,params=params)

# If the answer is 'ok'
if response.status_code == 200:

    # Store the result in a json file
    result = response.json()
    data = result["near_earth_objects"]

    # Create empty list of rows
    rows=[]

    # Looping through "near_earth_objects"
    for date, neos in data.items():

        # Looping through each object
        for neo in neos:

            # Creating a dictionary of each row with necessary data
            rows.append({
                "Asteroid ID": neo["id"],
                "Asteroid Name": neo["name"],
                "Min Diameter (km)": neo["estimated_diameter"]["kilometers"]["estimated_diameter_min"],
                "Absolute Magnitude": neo["absolute_magnitude_h"],
                "Relative Velocity (km/s)": neo["close_approach_data"][0]["relative_velocity"]["kilometers_per_second"],
            })
         
else:
    print(f"Invalid resquest. Error {response.status_code}.")

# Creating a data frame with the list of rows, where columns and the key of the dictionary 'row'
df= pd.DataFrame(rows)

# Exporting the dataframe in a csv file for cleaner output
output_file = f"neo_feed_{start_date}_clean.csv"
df.to_csv(output_file, index=False)
print("Data successfully exported to",output_file)