'''In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)
You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:
The total number of votes cast
A complete list of candidates who received votes
The percentage of votes each candidate won
The total number of votes each candidate won
The Winner of the election based on popular vote.'''

import os
import csv

pyPoll = os.path.join("..", "Resources","election_data.csv")

#Initializing the total votes
totalVotes = 0

# Creating dictionaries where the key will be the count of votes and values will be name of the candidates
candidateVotes = {}
candidatePercentages ={}

# Initializing the Winner's vote count
Winner = ""
WinningVotes = 0

# Opening the csv file
with open(pyPoll,'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    next(csvreader)
    
    # To tally the votes
    for row in csvreader:
        
        # Add to the total vote count
        totalVotes = totalVotes + 1
        
        # To get the candidate names from each row
        candidate = row[2]
        
        # To add for the same candidate in the candidate group
        if candidate in candidateVotes:
            candidateVotes[candidate] = candidateVotes[candidate] + 1
        else:
            candidateVotes[candidate] = 1
            
# To calculate vote percentage and identify winning candidate
for uniqueCandidate, voteCount in candidateVotes.items():
    candidatePercentages[uniqueCandidate] = '{0:.3%}'.format(voteCount / totalVotes)
    if voteCount > WinningVotes:
        WinningVotes = voteCount
        Winner = uniqueCandidate
        
# print out results
output = ("\n""Election Results\n")
print("-------------------------")
print(f"Total Votes: {totalVotes}")
print("-------------------------")
for uniqueCandidate, voteCount in candidateVotes.items():
    print(f"{uniqueCandidate}: {candidatePercentages[uniqueCandidate]} ({voteCount})")
print("-------------------------")
print(f"Winner: {Winner}")
print("-------------------------")

# Printing the results as text
with open("Election_Results.txt", "w") as pyPollText:
    pyPollText.write("\n""Election Results" + "\n")
    pyPollText.write("-------------------------" + "\n")
    pyPollText.write(f"Total Votes: {totalVotes}" + "\n")
    pyPollText.write("-------------------------" + "\n")  
    for uniqueCandidate, voteCount in candidateVotes.items():
        pyPollText.write(f"{uniqueCandidate}: {candidatePercentages[uniqueCandidate]} ({voteCount})" + "\n")
    pyPollText.write("-------------------------" + "\n")
    pyPollText.write(f"Winner: {Winner}" + "\n")
    pyPollText.write("-------------------------" + "\n")


