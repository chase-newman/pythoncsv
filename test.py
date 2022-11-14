# print("Hello World")

# name = "Chase"

# print(name)


# Python program to read CSV file line by line
# import necessary packages
import csv

from csv import writer
  
# Open file 
with open('test.csv') as file_obj:
      
    # Create reader object by passing the file 
    # object to reader method
    reader_obj = csv.reader(file_obj)
      
    # Iterate over each row in the csv 
    # file using reader object
    for row in reader_obj:
        print(row)


data = [name]
file = open('test.csv', 'w+',newline ='')
with file:    
    write = csv.writer(file)
    write.writerows(data)

    
def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)