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
    voterID_list = []
    candidates_list = []

        #Read through each row of data skipping the header
    for x in csvreader:

        #Assign a new variable for how to determine voters
        voters = (x[0])

        #Store voter values inside voterID_list
        voterID_list.append(voters)

        #Assign a new variable for how to determine voters
        candidates = (x[2])
        
        #Store candidate values inside candidates_list
        candidates_list.append(candidates)

        #Count per candidate
        

    #Find the length of the voterID_list
    length_voterID_list = len(voterID_list)

    #Remove duplicates from the candidates_list
    candidates_dict = list(dict.fromkeys(candidates_list))
    
    #Print statements
    print("Election Results")
    print("-------------------------------")
    print(f"Total Votes: {length_voterID_list}")
    print("-------------------------------")
    print(candidates_dict[0])
    print(candidates_dict[1])
    print(candidates_dict[2])
    print(candidates_dict[3])
    print("-------------------------------")
    print(f"Winner:")
    print("-------------------------------")
        


