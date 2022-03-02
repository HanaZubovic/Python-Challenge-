import os
import csv

#Create the space in memory and join it

budget_file_path = os.path.join("Resources","budget_data.csv")

#Creates a bookmark for the program to look to when we reference data

with open(budget_file_path) as budget_memory:
    budget_read = csv.reader(budget_memory, delimiter = ',')

# Declaring Variables

    total_months = 0
    net_profit_loss = 0
    change_pl = 0
    average_change_pl =0
    increase_profit = 0
    decrease_profit = 0
    ch_total = 0
    inc = ['',0]
    dec = ['',0]

    # max_date =""
    # min_date =""

    #Total number of months
    #Net Profit & Loss over the entire period

    #variable += 1
    #         ==
    #variable = variable + 1
    past_price = 0
    data_change = []
    next(budget_read)
    for i,row in enumerate(budget_read):
        # total_months = total_months + 1
        total_months += 1
        net_profit_loss += int(row[1])
        current_price = int(row[1])
        change = current_price - past_price 
        past_price = current_price

        if i == 0:
            change = 0 

        ch_total += change

        # Greatest Increase
        if change > inc[1]:
            inc[0] = row[0]
            inc[1] = change
        
        # Greatest Decrease
        if change < dec[1]:
            dec[0] = row[0]
            dec[1] = change

    output = f'''
    ---------------------------------------------------
       Financial Analysis
    ---------------------------------------------------
    Months: {total_months}
    Total: ${net_profit_loss:,}
    Average Change: ${ch_total/(total_months-1):,.2f}
    Greatest Increase in Profit is: {inc[0]} (${inc[1]:,})
    Greatest Decrease in Profit is: {dec[0]} (${dec[1]:,})
    ---------------------------------------------------'''
    
print(output)
open('analysis/analysis.txt','w').write(output)

