#Lab 5 ---------------------------------------
# Mashed potatos, applesauce
# buttery.... biscuits!
#---------------------------------------------

#A lot of this was stolen from a previous Scripting assignment I did lol

import csv
import json
#import sys
#import os
import requests


#This function is just meant to get the country. 
#I had this originally in the parse function, but moved it cause its easier
#Took longer cause I thought I needed an API key.


def fetch_country(ip_address):
    try:
        response = requests.get(f"http://ipinfo.io/{ip_address}/json")      #To get the IP, IPinfo has an API that we can use. Provide the forwarded IP and get the json data
        data = response.json()                                                  #Save the content from the API to a json file
        return data.get("country")                                              #With the saved json file, get the 'country' field of the contents
        #print("Obtained country!")                                                    #Just some debugging stuff
    
    except Exception as error:          #If an error happens, print the IP address being processed and the type of exception
        print(f"Couldn't get the country for the IP {ip_address}: {error}")



#This parses the vernlog csv to json, as well as convert the data into one variable and print it to the screen


def parsin(csv_file):
    data = []

    # Open the CSV file.
    with open(csv_file, "r") as file:
        reader = csv.DictReader(file)           #Read it with the DictReader function.

        # Get the csv contents so we can add another field.
        for row in reader:
            parsed_row = {
                "clientaddr": row["clientaddr"],
                "destaddr": row["destaddr"],
                "firewall": row["firewall"],
                "port": row["port"],
                "proto": row["proto"],
                "action": row["action"]
            }

            # Add country field based on clientaddr
            country = fetch_country(row["clientaddr"])     #To get the country based on the IP, go to the function using the clientaddr as the IP Address to search
            if country:
                parsed_row["country"] = country             #Afterwards, just parse the country data into the soon to be created json file

            data.append(parsed_row)                         #Append it to the end

    # Convert the list of dictionaries to a single variable string
    json_data = json.dumps(data, indent=4)
    return json_data



if __name__ == "__main__":

    csv_file = input("Enter the name of the csv file to parse> ")       #The user can enter the name of the file they wish to parse.
                                                                        #If said file isn't in the working directory, an absolute path  must be specified, duh.
    try:
        # Parse the CSV file and convert it to JSON
        json_data = parsin(csv_file)

        # Print the JSON data
        print(json_data)

    except FileNotFoundError:
        print("File not found.\n")
        print("Please provide an absolute path to the CSV file if needed.")