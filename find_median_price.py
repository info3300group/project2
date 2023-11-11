import os
import pandas as pd
import json

root_directory = 'NYCPropertyCosts'
boroughs = ['Bronx', 'Brooklyn', 'Manhattan', 'Queens', 'StatenIsland']
years = list(range(2010, 2018))

median_prices_dict = {}

for borough in boroughs:
    median_prices_dict[borough] = {}
    for year in years:
        file_path = os.path.join(root_directory, borough, f'{year}_{borough}.csv')

        if os.path.exists(file_path):
            df = pd.read_csv(file_path)

            df = df[df['Sale Price'] != 0]

            grouped_data = df[df['Zip Code'] != 0].groupby('Zip Code')['Sale Price'].median().reset_index()
            median_prices_dict[borough][str(year)] = grouped_data.to_dict(orient='records')

# Save the dictionary to a JSON file
with open('median_prices_by_zip.json', 'w') as json_file:
    json.dump(median_prices_dict, json_file, indent=2)

print('median prices by zip code saved to median_prices_by_zip.json')
