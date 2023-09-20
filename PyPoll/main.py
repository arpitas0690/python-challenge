#Author: Arpita Sharma
#Date: 9/10/2023
#Purpose: Using given set of poll data called election_data.csv. The dataset is composed of three columns: 
        #“Voter ID”, “County”, and “Candidate”. Your task is to create a Python script that analyzes the votes


#============================================================================================ .

# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

#creating list here
votes = {}
unique_candidate = []
counter = 0

#Election Data File located here:
csv_path = os.path.join('.','Resources', 'election_data.csv')
with open(csv_path) as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
      csvreader = csv.reader(csvfile, delimiter=',')

      #print(csvreader)
    
      #creating header
      csv_header = next(csvreader)
      #print(f"CSV Header: {csv_header}")

      
    
        # Read each row of data after the header
      for row in csvreader:
          counter = counter+1
          candidate_name =row[2]
          if candidate_name not in unique_candidate:
            unique_candidate.append(candidate_name)
            votes[candidate_name] = 0
          votes[candidate_name] +=1
            

      #The total numer of votes: 
      print(counter)

      #The list of unique candidates
      print(unique_candidate)

      #The list of votes for each candidate:
      print(votes[candidate_name])


# getting percentage of votes for each candidate
percentages = {key: round(val / counter *100,3) for key,val in votes.items()}

print(votes)

winning_candidate = max(votes, key=votes.get)
print(winning_candidate)

#creating variables for individual candidate votes
Stockham_votes = (votes['Charles Casper Stockham'])
DeGette_votes = (votes['Diana DeGette'])
Doane_votes = (votes['Raymon Anthony Doane'])

#creating variables for individual candidate vote percentages
Stockham_vote_percent = (percentages['Charles Casper Stockham'])
DeGette_vote_percent = (percentages['Diana DeGette'])
Doane_vote_percent = (percentages['Raymon Anthony Doane'])



'********************************************************************************'
#outputting analysis here
output_text = (
f'Election Results\n'
f'----------------------------\n'
f'Total Votes: {counter}\n'
f'----------------------------\n'
f'{unique_candidate[0]}: {Stockham_vote_percent}% ({Stockham_votes})\n'
f'{unique_candidate[1]}: {DeGette_vote_percent}% ({DeGette_votes})\n'
f'{unique_candidate[2]}: {Doane_vote_percent}% ({Doane_votes})\n'
f'----------------------------\n'
f'Winner:{winning_candidate}\n'
f'----------------------------\n')

print(output_text)

text_path = ("analysis/election_analysis.txt")
with open(text_path,"w") as txtfile:
    txtfile.write(output_text)

#============================================================================================ .