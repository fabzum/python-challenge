##PyBank Challenge##

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
    #print(csv_header)

    #Set count_row, net_total, pre_amount and sum_change_list to 0
    count_row = 0
    net_total = 0
    #pre_amount = 0 (not needed to be set at 0, why though?)
  
    #Create Lists to be filled in the Loop
    list_of_months =[]
    list_of_profits =[]
    change_list =[]
    
    
    #Loop through rows
    for row in csvreader:
        #Count the number of rows, which gives us the total number of months in the dataset and append them in the list_of_months
        count_row+=1
        list_of_months.append(row[0])

        #Count the net total amount, by summing up all the Profit and Losses and append them to the other list_of_profits
        net_total+=int(row[1])
        list_of_profits.append(row[1])

        #Find out the changes between the Profit and Losses and put the changes in the new change_list
        if count_row == 1:
            pre_amount = float(row[1])
        elif count_row > 1:
            change = float(row[1]) - pre_amount
            change_list.append(change)
            pre_amount = float(row[1])
     
        
    
    #Calculate the avarage of the change list by summing up the values of the list and divide it by it's length
    avergage_change_list=sum(change_list)/len(change_list)
    
    #Find out the greates increase and decrease in the change_list
    greatest_increase=max(change_list)
    greatest_decrease=min(change_list)

    #Find out the index number of the greatest increase and the greatest decrease
    greatest_increase_index=change_list.index(greatest_increase)
    greatest_decrease_index=change_list.index(greatest_decrease)
    
    #To find out the matching months for the greatest increase and decrease, we have to add 1 to the greatest increase and decrease index,
    #since the length of the list_of_months is + 1 than the list of the change_list. 
    greatest_increase_month=list_of_months[int(greatest_increase_index) + 1]
    greatest_decrease_month=list_of_months[int(greatest_decrease_index) + 1]

    #Printing out of the Results
    print(count_row)
    print(net_total)
    print(avergage_change_list)
    print(str(greatest_increase_month) + " with an increase of " + str(round(greatest_increase)))    
    print(str(greatest_decrease_month) + " with a decrease of " + str(round(greatest_decrease)))
    
#Create the output path for the text file (Textfile has been created via touch output.txt command in terminal)
output_path = os.path.join("output.txt")
with open(output_path, "w") as writefile:
    #Write down the solutions in the textfile
    writefile.writelines("Financial Analysis\n")
    writefile.writelines("------------------" + "\n")
    writefile.writelines("Total Months:" + str(count_row) + "\n")
    writefile.writelines("Total: $" + str(net_total) + "\n")
    writefile.writelines("Average Change: $" + str(round(avergage_change_list,2)) + "\n")
    writefile.writelines("Greatest Increase in Profits:" + str(greatest_increase_month) + "(" + "$" + str(round(greatest_increase)) + ")" + "\n")
    writefile.writelines("Greatest Decrease in Profits:" + str(greatest_decrease_month) + "(" + "$" + str(round(greatest_decrease)) + ")" + "\n")
    
     
     
  

