import os
import csv

#Create the space in memory and join it

budget_file_path = os.path.join(os.path.dirname(__file__),"Resources","budget_data.csv").replace("\\", "/")
print(budget_file_path)

#Creates a bookmark for the program to look to when we reference data

with open(budget_file_path, "r") as budget_memory:
    budget_read = csv.reader(budget_memory, delimiter = ',')

    total_months = 0
    net_profit_loss = 0
    change_pl = 0
    average_change_pl =0
    increase_profit = 0
    decrease_profit = 0

    print("Financial Analysis")
    print("----------------------------")

    #Total number of months
    
    for row in budget_read:
        total_months = len(list(budget_read))
        print("Total Months:", total_months)



    