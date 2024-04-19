import os
import csv

inputfile =os.path.join("election_data.csv")

outputfile = os.path.join("AnalysisPypoll.txt")

totalVotes = 0
candidates = []
candidateVotes = {}
winningCount =0
winningCandidate = ""
with open(inputfile) as surveyData:
    csvreader = csv.reader(surveyData)
    header = next(csvreader)
    for row in csvreader:
        totalVotes += 1
        candidateName=row[2]
        
        if candidateName not in candidates:
            candidates.append(candidateName)
            candidateVotes[candidateName] = 0
        else:
            candidateVotes[candidateName] +=1


voteroutput=""
for candidates in candidateVotes:
    votes=candidateVotes.get(candidates)
    votePct =(float(votes)/float(totalVotes))*100.00
    voteroutput += f"\t{candidates}:{votePct:.2f}% ({votes}) \n"
                     
    if votes> winningCount:
        winningCount =votes
        winningCandidate = candidates

winningCandidateOutput = f"Winner: {winningCandidate }\n-------------------------------------"

output = (
    
    f"\n"
    f"Election Results \n"
    f"\n"
    f"--------------------------------------\n"
    f"\n"
    f"\tTotal Votes: {totalVotes:,}\n"
    f"\n"
    f"--------------------------------------\n"
    f"\n"
    f"{voteroutput}\n"
    f"\n"
    f"--------------------------------------\n"
    f"\n"
    f"{winningCandidateOutput}"
    f"\n"
)

print(output)
with open(outputfile, "w") as textfile:
    textfile.write(output)









