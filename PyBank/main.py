
#The changes in "Profit/Losses" over the entire period, and then the average of those changes

# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

#creating a list here:
month = []
change_list = []
total_profit_loss = 0
counter = 0
#Budget Data File located here:
csv_path = ("Resources/budget_data.csv")
with open(csv_path) as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

      # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
    # Read each row of data after the header
    for row in csvreader:
        month.append(row[0])
        #print(row)
        profit_loss = int(row[1])
        #this is maintaining the total profit loss for the second question
        total_profit_loss +=int(row[1])
        if counter>0:
            change = profit_loss - previous_row
            change_list.append(change)
        previous_row = profit_loss
        counter+=1
    
#print(len(month))
#print(total_profit_loss)
avg_change = round(sum(change_list)/len(change_list),2)
#print(avg_change)

max_increase = max(change_list)
max_decrease = min(change_list)
max_index = change_list.index(max_increase)
min_index = change_list.index(max_decrease)
max_month = month[max_index+1]
min_month = month[min_index+1]

output_text = (
f'Financial Analysis\n'
f'----------------------------\n'
f'Total Months: {len(month)}\n'
f'Total: ${total_profit_loss}\n'
f'Average Change: ${avg_change}\n'
f'Greatest Increase in Profits: {max_month} (${max_increase})\n'
f'Greatest Decrease in Profits: {min_month} (${max_decrease})'
)

print(output_text)

text_path = ("analysis/budget_analysis.txt")
with open(text_path,"w") as txtfile:
    txtfile.write(output_text)
