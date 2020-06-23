#1st import the OS and CSV modules
import os
import csv

#Set path for "election_data" file
election_data_path = os.path.join("Resources", "election_data.csv")

#Open the "election_data" CSV file and specify delimiter and variable that holds content
with open(election_data_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
  
    #Skip the Header Row
    next(csvreader)

    #Assign variables
    voters = 0
    voterID_list = []
    candidates = 0
    candidates_list = []

        #Read through each row of data skipping the header
    for x in csvreader:
        
        #Loop through the Voter ID (column 1) and store values to the voterID list
        voters = int(x[0])
        voterID_list = voterID__list.append(voters)

        #Find the length of the voterID list
        length_voterID = len(voterID_list)

        #Store values in empty candidates_list
        

    print(f"Total Votes: {length_voterID}")