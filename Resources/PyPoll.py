#The data we need to retireve
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote

import csv
import os

#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or an indirect path to the file
file_to_save = os.path.join("Analysis", "election_analysis.txt")

#Initialize a total vote counter.
total_votes = 0

#Declare a new list for candidates
candidate_options = []

#Declare empty dictionary for votes per candidate
candidate_votes  ={}

#Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file.
with open(file_to_load) as election_data:
    #To do: perform analysis

    #Read the file object with the reader function
    file_reader = csv.reader(election_data)

    #PRint the header row
    headers = next(file_reader)

    #Print each row in the CSV File
    for row in file_reader:
        #print(row)
        #Add to the total vote count:
        total_votes += 1
        #Print total votes
        #print(total_votes) 

        #Print candidate name from each row
        candidate_name = row[2] 

        # Add candidate name to candidate options list. If the candidate name does not match any existing name
        if candidate_name not in candidate_options:
            #Add name to options list
            candidate_options.append(candidate_name)

            #BEgin tracking a candidate's votes
            candidate_votes[candidate_name] = 0

        #Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1

        #Determine the percentage of votes for each candidate
        #Iterate through the candidate list
    for candidate_name in candidate_votes:
        #Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]

        #Calculate percentage of votes
        vote_percentage = (float(votes) / float(total_votes)) * 100

        print(f"{candidate_name}: {vote_percentage: .1f}% ({votes:,})\n")

        #Determine winning vote count and candidate
        #Determine if the votes is greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

        #Print the candidate name and percentage of votes
        #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote")
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)


    #Print candidate names
    print(candidate_options)

    #Print candidate votes dictionary
    print(candidate_votes)


# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Counties in the Election\n-------\nArapahoe\nDenver\nJefferson")
