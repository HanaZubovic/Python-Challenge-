import os
import csv

#Create the space in memory and join it

budget_file_path = os.path.join("Resources","budget_data.csv").replace("\\", "/")
print(budget_file_path)

#Creates a bookmark for the program to look to when we reference data

with open(budget_file_path, "r") as budget_memory:
    budget_read = csv.reader(budget_memory, delimiter = ',')

# Declaring Variables

    total_months = 0
    net_profit_loss = 0
    change_pl = 0
    average_change_pl =0
    increase_profit = 0
    decrease_profit = 0
    max_date =""
    min_date =""

    #Total number of months
    #Net Profit & Loss over the entire period

    #variable += 1
    #         ==
    #variable = variable + 1
    past_price = 0
    data_change = []
    next(budget_read)
    for row in budget_read:
        total_months += 1
        net_profit_loss += int(row[1])
         
        current_price = int(row[1])
        change = current_price - past_price 
        past_price = current_price
        data_change.append(change)

    #Greatest Increase and Decrease in profits over the enitre period
        max_d = max(data_change)
        min_d = min(data_change)
        if (change == max_d):
            max_date = row[0]
        if (change == min_d):
            min_date = row[0]
    data_change.pop(0)
    average = round(sum(data_change) / len(data_change), 2)
 
    print("----------------------------------------------------")
    print ("Financial Analysis")
    print("----------------------------------------------------")
    print("Months:", total_months)
    print(f'Total: ${net_profit_loss}')
    print(f'Average Change: ${average}')
    print(f'Greatest Increase in Profit is: {max_date} ${max_d}')
    print(f'Greatest Decrease in Profit is: {min_date} ${min_d}')
    print("----------------------------------------------------")
    
export_path = os.path.join("analysis", "analysis.txt").replace("\\", "/")
with open(export_path, "w") as export_mem:
    export_writer = csv.writer(export_mem)
    export_writer.writerow(["Financial Analysis"])
    export_writer.writerow(["----------------------------------------------------"])
    export_writer.writerow([f"Months:, {total_months}"])
    export_writer.writerow([f'Total: ${net_profit_loss}'])
    export_writer.writerow([f'Average Change: ${average}'])
    export_writer.writerow([f'Greatest Increase in Profit is: {max_date} ${max_d}'])
    export_writer.writerow([f'Greatest Decrease in Profit is: {min_date} ${min_d}'])
