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


  
    #Create Lists and a Dictionnary to be filled in the Loop
    list_of_candidates =[]
    final_list_of_candidates = []
    number_of_votes = []
    poll ={}
    percentage_of_vote = []
    winner = []
    #Put number of votes to zero
    total_of_votes = 0
    
    #Loop through rows in CSV
    for row in csvreader:
        
        #Count the number of rows, which gives us the total number of votes in the dataset
        total_of_votes+=1
        
        #Create a Full list with Candidates (includes dublicates)
        list_of_candidates.append(row[2])

        #Defines the candidates in row[2] as keys to the dictionary  
        if row [2] in poll.keys():
            poll[row[2]] = poll[row[2]]+1

        else:
            poll[row[2]] = 1
    
    #Returns two lists, once for the key (candidates) and one for its value (the number of votes)
    for key, value in poll.items():
        final_list_of_candidates.append(key)
        number_of_votes.append(value)
    
    #Calculates the percentage and appends it to the percentage_of_vote_list
    for vote in number_of_votes:
        percentage_of_vote.append(round(vote/total_of_votes*100, 3)) #Why does it not round to 3 decimal points?
    
    #Zipps the previous derived 3 lists into one (summary_data)
    summary_data = list(zip(final_list_of_candidates, percentage_of_vote, number_of_votes))

    #Loops through summary list and finds out the highest number and adds the name beloning to this number to the winner list
    for candidate in summary_data:
        if max(number_of_votes) == candidate[2]:
            winner.append(candidate[0])

    #Printing out the Results
    #-----------------------------
    #print(list_of_candidates)
    print(total_of_votes)
    #print(number_of_votes)
    #print(final_list_of_candidates)
    #print(percentage_of_vote)
    print(summary_data)
    print(winner)


#Create the output path for the text file (Textfile has been created via touch output.txt command in terminal)
output_path = os.path.join("output.txt")
with open(output_path, "w") as writefile:
    #Write down the solutions in the textfile
    writefile.writelines("Election Results\n")
    writefile.writelines("------------------" + "\n")
    writefile.writelines("Total Votes:" + str(total_of_votes) + "\n")
    writefile.writelines("------------------" + "\n")
    for i in range(len(final_list_of_candidates)):
        writefile.writelines(f"{final_list_of_candidates[i]}: {percentage_of_vote[i]}% ({number_of_votes[i]})\n")
    writefile.writelines("------------------" + "\n")
    writefile.writelines(f"Winner: {final_list_of_candidates[0]}\n")



