#1st import the OS and CSV modules
import os
import csv

#Set path for "budget_data" file
budget_data_path = os.path.join("Resources", "budget_data.csv")

#Open the "budget_data" CSV file and specify delimiter and variable that holds content
with open(budget_data_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
  
    #Skip the Header Row
    next(csvreader)

    #Assign variables
    total_months = 0
    net_total = 0
    previous = 0
    change = 0
    difference_list = []

    #Read through each row of data skipping the header
    for x in csvreader:
        
        #Find the total # of months in dataset
        total_months = total_months + 1

        #Find the net total amount of "Profit/Losses" over the entire period
        net_total = net_total + int(x[1])

        #Find the difference between rows in colum 2 and store values to the difference list
        change = int(x[1]) - previous
        previous = int(x[1])
        difference_list.append(change)
    
        #Calculate the # of differences from month to month
        length = len(difference_list) - 1

    #Calculate the average change in profit/loss
    average = round((sum(difference_list[1:])/length),2)

    #Calculate the greatest increase and decrease in profits
    maxincrease = int(max(difference_list))
    minincrease = int(min(difference_list))

    #Print values for total_months and net_total_profit_losses
    print("Financial Analysis")
    print("------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_total}")
    print(f"Average Change: ${average}")
    print(f"Greatest Increase in Profits: ${maxincrease}")
    print(f"Greatest Decrease in Profits: ${minincrease}")