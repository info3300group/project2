import os
import csv
import json

root_directory = os.path.join('.', 'NYCPropertyCosts')
result_dict = {}

borough_mapping = {
    "StatenIsland": "Staten Island"
}

for borough in os.listdir(root_directory):
    borough_path = os.path.join(root_directory, borough)

    if os.path.isdir(borough_path):
        formatted_borough = borough_mapping.get(borough, ' '.join(borough.split()))
        result_dict[formatted_borough] = {}

        csv_files = [f for f in os.listdir(borough_path) if f.endswith('.csv')]

        for csv_file in csv_files:
            year = csv_file.split('_')[0]
            year_path = os.path.join(borough_path, csv_file)

            with open(year_path, 'r') as file:
                reader = csv.DictReader(file)
                sale_prices = [int(row['Sale Price']) for row in reader if row['Sale Price'].strip() and int(row['Sale Price']) != 0 and row.get('Zip Code', '').strip()]
                
                if sale_prices:
                    average_price = "{:.2f}".format(round(sum(sale_prices) / len(sale_prices), 2))
                    result_dict[formatted_borough][year] = average_price

result_dict = dict(sorted(result_dict.items()))

with open('average_sale_prices.json', 'w') as json_file:
    json.dump(result_dict, json_file, indent=4)
