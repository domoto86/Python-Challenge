import csv

total_months = 0
pl_total = 0
previous_month = 0
profit_changes = []
great_inc = ["", 0]
great_dec = ["", 999999999]

# Read CSV file
with open('Resources/budget_data.csv') as csvfile:
    file = csv.reader(csvfile, delimiter=',')
    
    # Skips the first Row
    next(file)
    
    # Find the total for Profit/loss and finds total of months
    for row in file:

        total_months = total_months + 1

        pl_total = pl_total + int(row[1])

        this_month = int(row[1])
    
    # Evaluates if the first row is greater than one. This helps to create the logic for previous month.
        if total_months > 1:
            profit_change = this_month - previous_month
            profit_changes.append(profit_change)

            if profit_change > great_inc[1]:
                great_inc[0] = row[0]
                great_inc[1] = profit_change

            if profit_change < great_dec[1]:
                great_dec[0] = row[0]
                great_dec[1] = profit_change

        previous_month = this_month

# Finds the average of profit changes
average_change = sum(profit_changes) / len(profit_changes)

print("PyBasnk Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${pl_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {great_inc[0]} (${great_inc[1]})")
print(f"Greatest Decrease in Profits: {great_dec[0]} (${great_dec[1]})")

with open("Analysis/pybank_results.txt", "w") as text_file:
    text_file.write("Financial Analysis\n")
    text_file.write("----------------------------\n")
    text_file.write(f"Total Months: {total_months}\n")
    text_file.write(f"Total: ${pl_total}\n")
    text_file.write(f"Average Change: ${average_change:.2f}\n")
    text_file.write(f"Greatest Increase in Profits: {great_inc[0]} (${great_inc[1]})\n")
    text_file.write(f"Greatest Decrease in Profits: {great_dec[0]} (${great_dec[1]})\n")