#!/usr/bin/env python
# coding: utf-8

# In[9]:


#import module
import csv, os


# In[10]:


#define file path to load and output
election_csv = os.path.join("Resources", "election_data.csv")
file_output = os.path.join("analysis", "election_analysis.txt")


# In[11]:


#make list to hold data
VoterID = []
county = []
candidate = []
cand_option = {}
total_cand_vote = 0
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0


# In[12]:


#read csv and convert it into list
with open(election_csv, 'r') as f:
    csvreader = csv.reader(f, delimiter =",")
    header =next(csvreader)
    #print(header)
    for row in csvreader:
        VoterID.append(row[0])
        county.append(row[1])
        candidate_name = row[2]
        if candidate_name not in candidate:
            candidate.append(candidate_name)
            cand_option[candidate_name]=0
        cand_option[candidate_name]=cand_option[candidate_name] + 1
            


# In[13]:


#get total votes
total_votes = len(VoterID)


# In[14]:


with open(file_output, "w") as txt_file:
    result = (
         f"\n\nElction Result\n"
         f"------------------------\n"
         f"Total Votes: {total_votes}\n"
         f"------------------------\n")
    print(result, end="")
    txt_file.write(result)
    #get candidate count dictionary
    for candidate in cand_option:

        # Retrieve vote count and percentage
        votes = cand_option.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        # Determine winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        # Print each candidate's voter count and percentage (to terminal)
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

        # Save each candidate's voter count and percentage to text file
        txt_file.write(voter_output)

    # Print the winning candidate (to terminal)
    winning_cand_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winning_cand_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)

