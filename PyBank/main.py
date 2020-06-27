#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import module
import csv, os


# In[2]:


#define file path
budget_csv = os.path.join("Resources", "budget_data.csv")
#define file path to output
file_output = os.path.join("analysis", "budget_analysis.txt")


# In[3]:


#make lists to store data
date = []
pro_loss = []
change = []
total = 0


# In[4]:


#open CSV file and read data
with open(budget_csv, encoding = "utf-8") as f:
    csvreader = csv.reader(f, delimiter = ",")
    #read header
    fheader = next(csvreader)
    #print(f"csv header is: {fheader}")
    #read through data and append to the list
    for row in csvreader:
        date.append(row[0])
        pro_loss.append(int(row[1]))
    #calculate the totol number of months included in the dataset
    total_months = len(date)
     # The net total amount of "Profit/Losses" over the entire period
    for x in pro_loss:
        total = x + total
    for i in range(1, len(pro_loss)):
        #total = total +int(pro_loss[x])
        change.append(int(pro_loss[i]) - int(pro_loss[i-1]))

    #The average of the changes in "Profit/Losses" over the entire period
    ave_change = round(sum(change) / (total_months-1), 2)

    #The greatest increase in profits over the entire period
    greatest_inc=max(change)
    #The greatest decrease in losses over the entire period
    greatest_dec=min(change)
    #Find the month of the greatest change
    for i in range(0, len(change)):
        if change[i] == greatest_inc:
            date1=date[i+1]
        elif change[i] == greatest_dec:
            date2=date[i+1]


# In[5]:


#print analysis result
# print("Financial Analyis")
# print("-----------------------------")
# print(f"Total Months: {total_months}")
# print(f"Total: $ {total}")
# print(f"Average Change: {ave_change}")
# print(f"Greatest Increase in Profits: {date1} ({greatest_inc})")
# print(f"Greatest Decrease in Profits: {date2} ({greatest_dec})")    


# In[6]:


#generate output summary
output=(
    f"\nFinancial Analyis\n"
    f"-----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: $ {total}\n"
    f"Average Change: {ave_change}\n"
    f"Greatest Increase in Profits: {date1} ({greatest_inc})\n"
    f"Greatest Decrease in Profits: {date2} ({greatest_dec})\n")  

#print the output to the terminal
print(output)


# In[7]:


#export the output to termianl
with open(file_output, "w") as text_file:
    text_file.write(output)


# In[ ]:




