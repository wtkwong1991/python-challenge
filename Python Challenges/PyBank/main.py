import os
import csv

print("Financial Analysis")
print("----------------------------")

# Variables for finding total numbers of months and profits/losses in the dataset
months = 0
total = 0

# Variables for finding average of changes in profit/losses over entire period
avg_total = 0
diff1 = 0
diff2 = 0

# Variables for finding the greatest increase in profits and greatest decrease in losses over entire period
inc_date = ""
dec_date = ""
greatest_inc = 0
greatest_dec = 0
diff3 = 0
diff4 = 0
list1 = []
list2 = []
list3 = []
list4 = []


bankpath = os.path.join("budget_data.csv")

# Finding total numbers of months and profits/losses over the entire period
with open(bankpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        months +=1
        total += int(row[1])
print("Total Months: " + str(months))
print("Total: $" + str(total))


# Finding average of the changes in profits/losses over the entire period
months2 = 0
months3 = 0
with open(bankpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        if (months2 == 0):
           diff1 = float(row[1])
           break

with open(bankpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        months3 +=1
        if (months3 == months):
           diff2 = float(row[1])
           break
       
avg_total = diff2 - diff1
print("Average Change: $" + str(round(float(avg_total/(months-1)), 2)))




# Finding the date and amount with greatest increase in profits over the entire period
# Finding the date and amount with greatest decrease in losses over the entire period

# Making a list with the profits/losses amounts from the csv file
with open(bankpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        list1.append(row[1])

# Making a list with the dates from the csv file
with open(bankpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        list2.append(row[0])
 
# Making a list with yearly differences to find greatest increase in profits and greatest decrease in losses over entire period
i = 1
while(i < len(list1)):
    diff3 = int(list1[i])-int(list1[i-1])
    list3.append(diff3)
    i += 1
greatest_inc = max(list3)
greatest_dec = min(list3)


# Finding the dates with the greatest increase in profits and greatest decrease in losses over the entire period
j = 1
while(j < len(list3)):
    if(int(list3[j]) == int(greatest_inc)):
      inc_date = str(list2[j+1])
      break 
    j += 1

k = 1
while(k < len(list3)):
    if(int(list3[k]) == int(greatest_dec)):
      dec_date = str(list2[k+1])
      break 
    k += 1

print("Greatest Increase in Profits: " + str(inc_date) + " ($" + str(greatest_inc) + ")")
print("Greatest Decrease in Profits: " + str(dec_date) + " ($" + str(greatest_dec) + ")")




# Exporting a text file with the results
text_path = os.path.join("pybank.txt")
with open(text_path, "w") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow(["Total Months: " + str(months)])
    csvwriter.writerow(["Total: $" + str(total)])
    csvwriter.writerow(["Average Change: $" + str(round(float(avg_total/(months-1)), 2))])
    csvwriter.writerow(["Greatest Increase in Profits: " + str(inc_date) + " ($" + str(greatest_inc) + ")"])
    csvwriter.writerow(["Greatest Decrease in Profits: " + str(dec_date) + " ($" + str(greatest_dec) + ")"])