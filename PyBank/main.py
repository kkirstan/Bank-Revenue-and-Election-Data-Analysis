#import dependencies
import csv
import os

#set file path
csvpath = os.path.join("..", "PyBank/Resources", "budget_data.csv")

#define lists
months_list = []
profit_loss_list = []
change_list = []

#read csvfile
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #skip header row
    csv_header = next(csvreader)
    
    #create lists
    for row in csvreader:
        months_list.append(str(row[0]))
        profit_loss_list.append(int(row[1]))
    
    #calculate total months
    total_months = len(months_list)
    
    total = 0
    
    #calculate total revenue
    for x in profit_loss_list:
        total = total + x
    
    #calculate average change in revenue from month to month
    for x in range(1,len(profit_loss_list)):
        change_list.append(profit_loss_list[x] - profit_loss_list[x-1])
        average_change = round(sum(change_list)/len(change_list),2)

    #calculate the month with the greatest increase in revenue
    maxincrease = max(change_list)         
    max = change_list.index(maxincrease)
    maxmonth = months_list[max+1]

    #calculate the month with the greatest loss in revenue
    maxloss = min(change_list)
    min = change_list.index(maxloss)
    minmonth = months_list[min+1]
    
    #print financial analysis
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(total_months))
    print("Total: $" + str(total))
    print("Average Change: $" + str(average_change))
    print("Greatest Increase in Profits: " + str(maxmonth) + " ($" + str(maxincrease) + ")")
    print("Greatest Decrease in Profits: " + str(minmonth) + " ($" + str(maxloss) + ")")