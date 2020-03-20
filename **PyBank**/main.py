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

    #Skip Header
    csv_header = next(csvreader)
    print(csv_header)

    #Set count_row and sum_month to 0
    count_row = 0
    net_total = 0
    pre_amount = 0
    sum_change_list = 0

    list_of_months =[]
    list_of_profits =[]
    change_list =[]
    
    
    #Loop through rows
    for row in csvreader:
        count_row+=1
        list_of_months.append(row[0])

        net_total+=int(row[1])
        list_of_profits.append(row[1])

        if count_row == 1:
            pre_amount = int(row[1])
        elif count_row > 1:
            change = int(row[1]) - pre_amount
            change_list.append(change)
            pre_amount = int(row[1])
     
        
    
    
    avergage_change_list=sum(change_list)/len(change_list)
    greatest_increase=max(change_list)
    greatest_decrease=min(change_list)
    greatest_increase_index=change_list.index(greatest_increase)
    greatest_decrease_index=change_list.index(greatest_decrease)
    
    greatest_increase_month=list_of_months[int(greatest_increase_index) + 1]
    greatest_decrease_month=list_of_months[int(greatest_decrease_index) + 1]

    print(count_row)
    print(net_total)
    print(avergage_change_list)
    print(str(greatest_increase) + str(greatest_increase_month))    
    print(str(greatest_decrease) + str(greatest_decrease_month)) 
    
    
output_path = os.path.join("output.txt")
with open(output_path, "w") as writefile:

    writefile.writelines("Financial Analysis\n")
    writefile.writelines("------------------" + "\n")
    writefile.writelines("Total Months:" + str(count_row) + "\n")
    writefile.writelines("Total: $" + str(net_total) + "\n")
    writefile.writelines("Average Change: $" + str(round(avergage_change_list)) + "\n")
    writefile.writelines("Greatest Increase in Profits:" + str(greatest_increase_month) + "(" + "$" + str(greatest_increase) + ")" + "\n")
    writefile.writelines("Greatest Decrease in Profits:" + str(greatest_decrease_month) + "(" + "$" + str(greatest_decrease) + ")" + "\n")
    
     
     
  

