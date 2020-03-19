##PyBank Challenge
#Import Module to create file paths across operating systems
import os
#Import Module for reading CSV files
import csv
#Provide the path for the CSV file that should be read
csvpath = os.path.join("budget_data.csv")
#Read CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    csv_header = next(csvreader)
    print(csv_header)

    """
    Without a second list, you can do all operations in one for loop 
    """
    count_row = 0
    sum_row = 0

    for row in csvreader:
        count_row+=1
        sum_row+=int(row[1])
        print(row)

    print(count_row)
    print(sum_row)