import os
import csv

csvpath = os.path.join("..", "PyBank", "budget_data.csv")

months_list = []
profit_loss_list = []

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
    
    
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(total_months))
    print("Total: $" + str(total))
    
    
    
   
    
     
    