##PyPoll Challenge##

#Import Module to create file paths across operating systems
import os

#Import Module for reading CSV files
import csv

#Provide the path for the CSV file that should be read
csvpath = os.path.join("election_data.csv")

#Read CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)

    #Skip Header
    csv_header = next(csvreader)
    
    #print(csv_header)

    #Set count_row, net_total, pre_amount and sum_change_list to 0
    count_row = 0
    candidates = 0
    #pre_amount = 0 (not needed to be set at 0, why though?)
  
    #Create Lists to be filled in the Loop
    list_of_candidates =[]
    number_of_votes = []
    poll ={}
    total_of_votes = 0
    
    #Loop through rows
    for row in csvreader:
        
        #Count the number of rows, which gives us the total number of months in the dataset and append them in the list_of_months
        total_of_votes+=1
        
        #candidates+=int(row[2])
        list_of_candidates.append(row[2])

        for x in list_of_candidates:
            if x == 

    print(total_of_votes)
    print(list_of_candidates)