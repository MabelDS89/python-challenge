#1st import the OS, CSV, and Counter modules
import os
import csv
import collections
from collections import Counter

#Set path for "election_data" file
election_data_path = os.path.join("Resources", "election_data.csv")

#Open the "election_data" CSV file and specify delimiter and variable that holds content
with open(election_data_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
  
    #Skip the Header Row
    next(csvreader)

    #Assign variables
    voterID_roster = []
    candidates_roster = []

        #Read through each row of data skipping the header
    for x in csvreader:

        #Assign a new variable for how to determine voters
        voters = (x[0])

        #Store voter values inside voterID_list
        voterID_roster.append(voters)

        #Assign a new variable for how to determine voters
        candidates = (x[2])
        
        #Store candidate values inside candidates_list
        candidates_roster.append(candidates)

    #Count per candidate
    candidate_freq = []
    candidate_names = candidates_roster

    for name in candidate_names:

        candidate_freq.append(name)

    counter_candidate_freq = Counter(candidate_freq)

    #Find the length of the voterID_list
    length_voterID_roster = len(voterID_roster)

    #Remove duplicates from the candidates_list
    candidates_dict = list(dict.fromkeys(candidates_roster))

    #Percent of Khan votes
    Khan_votes = int(counter_candidate_freq[candidates_dict[0]])
    Khan_percent = Khan_votes/length_voterID_roster

    #Percent of Correy votes
    Correy_votes = int(counter_candidate_freq[candidates_dict[1]])
    Correy_percent = Correy_votes/length_voterID_roster

    #Percent of Li votes
    Li_votes = int(counter_candidate_freq[candidates_dict[2]])
    Li_percent = Li_votes/length_voterID_roster

    #Percent of Li votes
    OTooley_votes = int(counter_candidate_freq[candidates_dict[3]])
    OTooley_percent = OTooley_votes/length_voterID_roster
    
    #Print statements
    print("Election Results")
    print("-------------------------------")
    print(f"Total Votes: {length_voterID_roster}")
    print("-------------------------------")
    print(candidates_dict[0], "{:.3%}".format(Khan_percent), counter_candidate_freq[candidates_dict[0]])
    print(candidates_dict[1], "{:.3%}".format(Correy_percent), counter_candidate_freq[candidates_dict[1]])
    print(candidates_dict[2], "{:.3%}".format(Li_percent), counter_candidate_freq[candidates_dict[2]])
    print(candidates_dict[3], "{:.3%}".format(OTooley_percent), counter_candidate_freq[candidates_dict[3]])
    print("-------------------------------")
    print(f"Winner: {candidates_dict[0]}")
    print("-------------------------------")