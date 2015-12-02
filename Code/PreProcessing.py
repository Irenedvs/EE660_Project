#!/usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals

import codecs
import csv
import sys

def main():
    data = []
    filename = "/Users/irenedavis/Documents/EE660/Final_Proj/train.csv"
    with open(filename, 'rb') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)

    print row.keys()

    wilderness_area_keys = ["Wilderness_Area{}".format(i) for i in range(1,5)]
    soil_type_keys = ["Soil_Type{}".format(i) for i in range(1,41)]
    print wilderness_area_keys
    print soil_type_keys

    for row in data:
        # Convert Wilderness Area[1-4] to Wilderness Area with value 1-4
        for i, key in enumerate(wilderness_area_keys):
            if row[key] == '1':
                row['Wilderness_Area'] = i + 1
            row.pop(key, None)
        # Convert Soil Type[1-40] to Soil Type
        for i, key in enumerate(soil_type_keys):
            if row[key] == '1':
                row['Soil_Type'] = i + 1
            row.pop(key, None)
        #print row

    write_dictionary("/Users/irenedavis/Documents/EE660/Final_Proj/outputs/train-transform.csv", data)

def write_dictionary(filename, data):    
    keys = data[0].keys()

    with open(filename, 'wb') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)

if __name__ == "__main__":
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
    main()
    

