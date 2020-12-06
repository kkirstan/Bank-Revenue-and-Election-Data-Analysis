import os
import csv

csvpath = os.path.join("..", "PyPoll/Resources", "PyPoll_Data.csv")

voter_list = []

with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        voter_list.append(str(row[0]))

    total_votes = len(voter_list)

    print("Election Results")
    print("-----------------------")
    print("Total Votes: " + str(total_votes))
    print("-----------------------")
    
