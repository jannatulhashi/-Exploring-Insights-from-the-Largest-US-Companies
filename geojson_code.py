<<<<<<< HEAD
import csv
import json

from collections import OrderedDict

li = []
with open('Resources/company_data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for lat, long, Company, Revenue_2021, Revenue_per_change_2021, Profits_in_millions_2021, Market_value_2021, Employees_2021, Revenue_2022, Revenue_per_change_2022, Profits_in_millions_2022, Market_value_2022, Employees_2022, Sector, City, State, Ceo_woman in reader:
        d = OrderedDict()
        d['type'] = 'Feature'
        d['geometry'] = {
            'type': 'Point',
            'coordinates': [(lat), (long)],
        }
#went through all the columns in the csv file and added here
                            
        d['properties'] = {
            'Company': Company,
            'Revenue_2021': Revenue_2021,
            'Revenue_%_change_2021': Revenue_per_change_2021,
            'Profits_in_millions_2021': Profits_in_millions_2021,
            'Market_value_2021':Market_value_2021,
            'Employees_2021':Employees_2021,
            'Revenue_2022': Revenue_2022, 
            'Revenue_%_change_2022': Revenue_per_change_2022,
            'Profits_in_millions_2022': Profits_in_millions_2022,
            'Market_value_2022':Market_value_2022,
            'Employees_2022':Employees_2022,
            'Sector':Sector,
            'City': City,
            'State': State,
            'Ceo_woman':Ceo_woman

        }
        li.append(d)

d = OrderedDict()
d['type'] = 'FeatureCollection'
d['features'] = li
with open('GeoObs.json', 'w') as f:
    f.write(json.dumps(d, sort_keys=False, indent=4))
=======
import csv
import json

from collections import OrderedDict

li = []
with open('company_data_and_location_to_geojson.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',') 
    
    #skips the header row
    next(reader)

    for lat, long, Company, Revenue_2021, Revenue_per_change_2021, Profits_in_millions_2021, Market_value_2021, Employees_2021, Revenue_2022, Revenue_per_change_2022, Profits_in_millions_2022, Market_value_2022, Employees_2022, Sector, City, State, Ceo_woman in reader:
        d = OrderedDict()
        d['type'] = 'Feature'
        d['geometry'] = {
            'type': 'Point',
            'coordinates': [(lat), (long)],
        }
#went through all the columns in the csv file and added here
                            
        d['properties'] = {
            'Company': Company,
            'Revenue_2021': Revenue_2021,
            'Revenue_%_change_2021': Revenue_per_change_2021,
            'Profits_in_millions_2021': Profits_in_millions_2021,
            'Market_value_2021':Market_value_2021,
            'Employees_2021':Employees_2021,
            'Revenue_2022': Revenue_2022, 
            'Revenue_%_change_2022': Revenue_per_change_2022,
            'Profits_in_millions_2022': Profits_in_millions_2022,
            'Market_value_2022':Market_value_2022,
            'Employees_2022':Employees_2022,
            'Sector':Sector,
            'City': City,
            'State': State,
            'Ceo_woman':Ceo_woman

        }
        li.append(d)

d = OrderedDict()
d['type'] = 'FeatureCollection'
d['features'] = li
with open('GeoObs.json', 'w') as f:
    f.write(json.dumps(d, sort_keys=False, indent=4))
>>>>>>> e4e3da799cb780104235441de82c80bf291fb918