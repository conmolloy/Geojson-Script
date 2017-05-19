import csv
import os

#asks user the name of file
userFile = raw_input('Enter the name of the csv file: ')

#redas in the data of file
f = open(userFile)
csv_f = csv.reader(f)
next(csv_f, None)  # skip the headers

#reads it in again this time to count the rows in the file
with open(userFile,"r") as l:
    reader = csv.reader(l,delimiter = ",")
    data = list(reader)
    tot_row_count = len(data)

#opening text of the geojson
test = "{ \n\t\"type\": \"FeatureCollection\",\n\t\"features\": [\n\t"
cords_list = []



row_count = 0

#iterates through all the rows of the file
for row in csv_f:
    #increments what row currently on 
    row_count = row_count + 1
    #the latitude data is stored on column 4 (5-1 = 4 =column F)
    latitude = row[5]
    longitude = row[6]
    store_name = row[1]
    address = row[2]
    town = row[3]  
    no_of_machine = row[4]
    machine_type = row[0]
    #etc etc serial_number stored on 6 (5-1 = 6 = column H)
    serial_number = row[7]
    macine_no_str = ""

    #if no of machine = 1 do nothing
    if no_of_machine == "1":
        macine_no_str = ""
    #if it is 2 put a 2 on the marker styling
    if no_of_machine == "2":
        macine_no_str = "\"marker-symbol\": \"2\",\n\t\t\t"
    #if it is 3 put a 3 on the marker styling
    if no_of_machine == "3":
        macine_no_str = "\"marker-symbol\": \"3\",\n\t\t\t"
    #if the machine type is a vending machine colour it blue
    if machine_type == "Vending":
        macine_no_str = macine_no_str +"\"marker-color\": \"#5ab4ac\",\n\t\t\t"
    #else colour it orange 
    else:
        macine_no_str = macine_no_str + "\"marker-color\": \"#d8b365\",\n\t\t\t"

    #if the row is not the last rown continue as normal
    if (row_count < tot_row_count - 1 ):
        cords_list.append("\t\t{\n\t\t\"type\": \"Feature\",\n\t\t\"geometry\": {\n\t\t\t\"type\": \"Point\",\n\t\t\t\"coordinates\": [\n\t\t\t"+str(longitude)+",\n\t\t\t"+str(latitude)+"\n\t\t\t]\n\t\t},\n\t\t\"properties\": {\n\t\t\t\"store-name\": \""+str(store_name)+"\",\n\t\t\t\"marker-size\": \"small\",\n\t\t\t"+macine_no_str+"\"address\": \""+str(address)+"\",\n\t\t\t\"machineType\": \""+str(machine_type)+"\",\n\t\t\t\"serialNo\": \""+ str(serial_number)+"\",\n\t\t\t\"city\": \""+str(town)+"\"\n\t\t}\n\t\t},\n")
    #if the row is the last row dont put a comma at the end
    else:
        cords_list.append("\t\t{\n\t\t\"type\": \"Feature\",\n\t\t\"geometry\": {\n\t\t\t\"type\": \"Point\",\n\t\t\t\"coordinates\": [\n\t\t\t"+str(longitude)+",\n\t\t\t"+str(latitude)+"\n\t\t\t]\n\t\t},\n\t\t\"properties\": {\n\t\t\t\"store-name\": \""+str(store_name)+"\",\n\t\t\t\"marker-size\": \"small\",\n\t\t\t"+macine_no_str+"\"address\": \""+str(address)+"\",\n\t\t\t\"machineType\": \""+str(machine_type)+"\",\n\t\t\t\"serialNo\": \""+ str(serial_number)+"\",\n\t\t\t\"city\": \""+str(town)+"\"\n\t\t}\n\t\t}\n")


#output geojson
#deletes any geojson file first before recreating

try:
    os.remove("geojson.geojson")
except OSError:
    pass
with open("geojson.geojson", "a") as outputFile:
    outputFile.write(test) 
    for line in cords_list:       
        outputFile.write(line)
    outputFile.write("\t]\n}")




