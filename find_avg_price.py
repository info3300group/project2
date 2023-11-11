import os
import pandas as pd
import json

root_directory = 'NYCPropertyCosts'
boroughs = ['Bronx', 'Brooklyn', 'Manhattan', 'Queens', 'StatenIsland']
years = list(range(2010, 2018))

average_prices_dict = {}

for borough in boroughs:
    average_prices_dict[borough] = {}
    for year in years:
        file_path = os.path.join(root_directory, borough, f'{year}_{borough}.csv')

        if os.path.exists(file_path):
 
            df = pd.read_csv(file_path)
            zip_code_column_name = 'Zip Code' 

            df = df[df['Sale Price'] != 0]

        
            grouped_data = df[df['Zip Code'] != 0].groupby('Zip Code')['Sale Price'].mean().reset_index().round(2)


            average_prices_dict[borough][str(year)] = grouped_data.to_dict(orient='records')

with open('average_prices_by_zip.json', 'w') as json_file:
    json.dump(average_prices_dict, json_file, indent=2)

print('avg prices by zip code saved to avg_prices_by_zip.json')
