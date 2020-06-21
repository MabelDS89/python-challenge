#1st import the OS module
import os

#2nd import module for reading CSV and set path for "budget_data" file
import csv
budget_datacsv = os.path.join("Resources", "budget_data.csv")
    
#Assign values to variables
date = str((budget_data[0])
profitloss = int((budget_data[1]))

#Open the "budget_data" CSV file and specify delimiter and variable that holds content
with open(budget_datacsv) as csvfile:
    csvreader = csv.reader(budget_datacsv, delimiter=",")
  
    #Skip the Header Row
    next(csvreader, None)

    #Read through each row of data skipping the header
    for row in csvreader:
        
        #Find the total # of months in "budget_data" file by using the len() function
        total_months = int(len(date))

        #Find the net total amount of "Profit/Losses" over the entire period
        net_total_profit_losses = int(sum(profitloss))

        #Print values for total_months and net_total_profit_losses
        print(f'"Total Months: " + (total_months)')
        print(f'"Total: " + (net_total_profit_losses)')