'''In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called budget_data.csv. The dataset is composed of two columns: Date and Profit/Losses. 
Your task is to create a Python script that analyzes the records to calculate each of the following:
The total number of months included in the dataset
The net total amount of "Profit/Losses" over the entire period
The average of the changes in "Profit/Losses" over the entire period
The greatest increase in profits (date and amount) over the entire period
The greatest decrease in losses (date and amount) over the entire period '''

import os
import csv

pyBank = os.path.join("..", "Resources","budget_data.csv")

with open(pyBank, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)
    
    # Create empty list to add the csv values 
    totalmonth = []
    totalProfit = []
    profitChange = []
    
    # for creating a loop to go through the values and add them to the empty list
    for row in csvreader:
        totalmonth.append(row[0])
        totalProfit.append(int(row[1]))
        
    for i in range(len(totalProfit)-1):
        profitChange.append(totalProfit[i + 1] - totalProfit[i])
    
# to evaluate the max and min from the list made
increasedAmount = max(profitChange)
decreasedAmount = min(profitChange)
    
# for finding the increased month and decreased month
monthIncrease = profitChange.index(max(profitChange)) + 1
monthDecrease = profitChange.index(min(profitChange)) + 1

# To summarize the analysis
output = (f"\nFinancial Analysis\n"
          f"---------------------------\n"
          f"Total Months: {len(totalmonth)}\n"
          f"Total: ${sum(totalProfit)}\n"
          f"Average Change: {round(sum(profitChange)/len(profitChange),2)}\n"
          f"Greatest Increase in Profit: {totalmonth[monthIncrease]} (${(str(increasedAmount))})\n"
          f"Greatest Decreaes in Profit: {totalmonth[monthDecrease]} (${(str(decreasedAmount))})\n")

# To print the output
print(output)    

# Open the file using "write" mode. Specify the variable to hold the contents
with open("Financial_analysis.txt", "w") as pyBankText:
    pyBankText.write(output)
    
    
    
     
     
    

    
    
    
    
