#import dependencies
import os
import csv

#set file path
csvpath = os.path.join("..", "PyPoll/Resources", "PyPoll_Data.csv")

#define lists
voter_list = []
county_list = []
candidates_list = []
khan = []
correy = []
li = []
otooley = []

#read csvfile
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip header row
    csv_header = next(csvreader)

    #create lists
    for row in csvreader:
        voter_list.append(str(row[0]))
        county_list.append(row[1])
        candidates_list.append(row[2])

    #calculate total votes
    total_votes = len(voter_list)

    #calculate total votes/percentage of overall votes per candidate
    for x in candidates_list:
        if x == "Khan":
            khan.append(candidates_list)
            khan_votes = len(khan)
            percentkhan = round((khan_votes/total_votes)*100,3)
        elif x == "Correy":
            correy.append(candidates_list)
            correy_votes = len(correy)
            percentcorrey = round((correy_votes/total_votes)*100,3)
        elif x == "Li":
            li.append(candidates_list)
            li_votes = len(li)
            percentli = round((li_votes/total_votes)*100,3)
        else:
            otooley.append(candidates_list)
            otooley_votes = len(otooley)
            percentotooley = round((otooley_votes/total_votes)*100,3)

    #find winner
    winner = max(percentkhan,percentcorrey,percentli,percentotooley)

    if winner == percentkhan:
        winner1 = "Khan"
    elif winner == percentcorrey:
        winner1 = "Correy"
    elif winner == percentli:
        winner1 = "Li"
    elif winner == percentotooley:
        winner1 = "O'Tooley" 

    #print analysis
    print("Election Results")
    print("-----------------------")
    print("Total Votes: " + str(total_votes))
    print("-----------------------")
    print("Khan: " + str(percentkhan) + "% (" + str(khan_votes) + ")")
    print("Correy: " + str(percentcorrey) + "% (" + str(correy_votes) + ")")
    print("Li: " + str(percentli) + "% (" + str(li_votes) + ")")
    print("O'Tooley: " + str(percentotooley) + "% (" + str(otooley_votes) + ")")
    print("-----------------------")
    print("Winner: " + winner1)
    print("-----------------------")

log = open("PyPollAnalysis.txt", "w")
print("PyPoll Analysis", file = log)