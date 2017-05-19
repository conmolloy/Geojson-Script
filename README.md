This script was made using Python 2.7 to convert CSV files to Geojson files.

It is used to convert database location information downloaded as .csv files to Geojson files, so that they can be used in web application maps.
The script works by collecting the data like address, latitude and longitude from the different columns in a csv and then converts that data in to a json file which can be used to create a map.

The code is commented so if you want to change the columns just change the column number in the script.

In the example folder there is an example CSV file and the output that the script produces geojson.geojson and an example web application it can be used for

I also included an exe version of the script that unfortunatly can be edited and needs to be re compliled if you edit the script.

There is a Step action guide for more help.

External library used are the OS library and the CSV library. https://docs.python.org/2/library/csv.html make sure these are installed before running they python version of the script.

Enjoy!