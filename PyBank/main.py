import csv
import os

csvpath = os.path.join("..", "PyBank/Resources", "budget_data.csv")

months_list = []
profit_loss_list = []
change_list = []

with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvreader)
    
    for row in csvreader:
        months_list.append(str(row[0]))
        profit_loss_list.append(int(row[1]))
    
    total_months = len(months_list)
    
    total = 0
    
    for x in profit_loss_list:
        total = total + x
    
    for x in range(1,len(profit_loss_list)):
        change_list.append(profit_loss_list[x] - profit_loss_list[x-1])
        average_change = round(sum(change_list)/len(change_list),2)

    maxincrease = max(change_list)         
    max = change_list.index(maxincrease)
    maxmonth = months_list[max+1]

    maxloss = min(change_list)
    min = change_list.index(maxloss)
    minmonth = months_list[min+1]
    
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(total_months))
    print("Total: $" + str(total))
    print("Average Change: $" + str(average_change))
    print("Greatest Increase in Profits: " + str(maxmonth) + " ($" + str(maxincrease) + ")")
    print("Greatest Decrease in Profits: " + str(minmonth) + " ($" + str(maxloss) + ")")