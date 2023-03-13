import csv

total_votes = 0
value_counts = {}

# Read CSV file
with open('Resources/election_data.csv') as csvfile:
    file = csv.reader(csvfile, delimiter=',')
    
    # Skip header row
    next(file)
    
    for row in file:
        #Adding total counts and grabbing candidate value from Candidate Column
        total_votes = total_votes + 1
        value = row[2]
        
        #Adding unique candidates to dictionary
        if value not in value_counts:
            value_counts[value] = 1
        else:
            value_counts[value] = value_counts[value] + 1

#Printing Results
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {total_votes}")
print(f"-------------------------")

#Printing Name, Percentage and total votes for each candidate
for value, count in value_counts.items():
    percentage = round(count / total_votes * 100,3)
    print(f"{value}: {percentage}% ({(count)})")

#Printing Winner
print(f"-------------------------")
#Below line of code found it online to grab the max
winner = max(value_counts, key=value_counts.get)

print(f"Winner: {winner}")
print(f"-------------------------")

#Creating .txt with the Results
with open("Analysis/PyPoll_results.txt", "w") as txt_file:
    txt_file.write(f"Election Results\n")
    txt_file.write(f"-------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write(f"-------------------------\n")

    for value, count in value_counts.items():
        percentage = round(count / total_votes * 100,3)
        txt_file.write(f"{value}: {percentage}% ({(count)})\n")

    txt_file.write(f"-------------------------\n")
    txt_file.write(f"Winner: {winner}\n")
    txt_file.write(f"-------------------------")