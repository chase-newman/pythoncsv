# print("Hello World")

# name = "Chase"

# print(name)


# Python program to read CSV file line by line
# import necessary packages
import csv
  
# Open file 
with open('test.csv') as file_obj:
      
    # Create reader object by passing the file 
    # object to reader method
    reader_obj = csv.reader(file_obj)
      
    # Iterate over each row in the csv 
    # file using reader object
    for row in reader_obj:
        print(row)

name = input("What is your name?")

data = [name]
file = open('test.csv', 'w+',newline ='')
with file:    
    write = csv.writer(file)
    write.writerows(data)