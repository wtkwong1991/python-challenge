import os
import csv

print("Election Results")
print("----------------------------")


# Variable for finding total number of votes 
total = 0

# Variables for finding total number of votes for each candidate
khan_votes = 0
correy_votes = 0
li_votes = 0
tooley_votes = 0

# Variables for finding percent of each candidate's number of won votes 
khan_percent = 0
correy_percent = 0
li_percent = 0
tooley_percent = 0

# Variable for finding candidate with the most number of votes 
winner = 0


# Finding the total number of votes from csv file 
pollpath = os.path.join("election_data.csv")
with open(pollpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    header = next(csvreader)
    for row in csvreader:
        total += 1
print("Total Votes: " + str(int(total)))
print("----------------------------")


# Finding Khan's percentage of won votes and total number of won votes 
with open(pollpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    header = next(csvreader)
    for row in csvreader:     
       if(row[2] == "Khan"):
        khan_votes += 1
khan_percent = round(((float(khan_votes)/float(total))*100), 3)
print("Khan: " + str(khan_percent) + "% (" + str(khan_votes) + ")")


# Finding Correy's percentage of won votes and total number of won votes 
with open(pollpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    header = next(csvreader)
    for row in csvreader:          
       if(row[2] == "Correy"):
        correy_votes += 1
correy_percent = round(((float(correy_votes)/float(total))*100), 3)
print("Correy: " + str(correy_percent) + "% (" + str(correy_votes) + ")")


# Finding Li's percentage of won votes and total number of won votes 
with open(pollpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    header = next(csvreader)
    for row in csvreader:         
       if(row[2] == "Li"):
        li_votes += 1    
li_percent = round(((float(li_votes)/float(total))*100), 3)
print("Li: " + str(li_percent) + "% (" + str(li_votes) + ")")


# Finding O'Tooley's percentage of won votes and total number of won votes 
with open(pollpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    header = next(csvreader)
    for row in csvreader: 
       if(row[2] == "O'Tooley"):
        tooley_votes += 1  
tooley_percent = round(((float(tooley_votes)/float(total))*100), 3)
print("O'Tooley: " + str(tooley_percent) + "% (" + str(tooley_votes) + ")")
print("----------------------------")



# Finding which candidate has the most winning number of votes 
if(khan_votes > correy_votes and khan_votes > li_votes and khan_votes > tooley_votes):
    print("Winner: Khan")
elif(correy_votes > khan_votes and correy_votes > li_votes and correy_votes > tooley_votes):
    print("Winner: Correy")
elif(li_votes > khan_votes and li_votes > correy_votes and li_votes > tooley_votes):
    print("Winner: Li")
elif(tooley_votes > khan_votes and tooley_votes > correy_votes and tooley_votes > li_votes):
    print("Winner: O'Tooley")

print("----------------------------")




# Exporting a text file with the results
text_path = os.path.join("pypoll.txt")
with open(text_path, "w") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow(["Total Votes: " + str(int(total))])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow(["Khan: " + str(khan_percent) + "% (" + str(khan_votes) + ")"])
    csvwriter.writerow(["Correy: " + str(correy_percent) + "% (" + str(correy_votes) + ")"])
    csvwriter.writerow(["Li: " + str(li_percent) + "% (" + str(li_votes) + ")"])
    csvwriter.writerow(["O'Tooley: " + str(tooley_percent) + "% (" + str(tooley_votes) + ")"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow(["Winner: Khan"])
    csvwriter.writerow(["----------------------------"])