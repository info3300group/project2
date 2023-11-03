import os
import csv
import json

root_directory = 'NYCPropertyCosts'
result_dict = {}

for borough in os.listdir(root_directory):
    borough_path = os.path.join(root_directory, borough)
    
    if os.path.isdir(borough_path):
        result_dict[borough] = {} 

        csv_files = [f for f in os.listdir(borough_path) if f.endswith('.csv')]
        
        for csv_file in csv_files:
            year = csv_file.split('_')[0]
            year_path = os.path.join(borough_path, csv_file)
            
            with open(year_path, 'r') as file:
                reader = csv.DictReader(file)
                sale_prices = [int(row['Sale Price']) for row in reader if row['Sale Price'].strip()]
                if sale_prices:
                    average_price = round(sum(sale_prices) / len(sale_prices), 2)
                    result_dict[borough][year] = average_price

with open('average_sale_prices.json', 'w') as json_file:
    json.dump(result_dict, json_file, indent=4)
