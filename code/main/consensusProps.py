# Cross Domain Fairness
# Michele Albach
# This file determines the consensus levels achieved in the property assignments in the initial survey using Shannon entropy

import csv
import numpy as np
from scipy import stats

recfile = open('../../data/MainSurveyBail.csv','r')
recdata = list(csv.reader(recfile))
recfile.close()
unemfile = open('../../data/MainSurveyUnem.csv','r')
unemdata = list(csv.reader(unemfile))
unemfile.close()
cpsfile = open('../../data/MainSurveyCPS.csv','r')
cpsdata = list(csv.reader(cpsfile))
cpsfile.close()
hosfile = open('../../data/MainSurveyHos.csv','r')
hosdata = list(csv.reader(hosfile))
hosfile.close()
loanfile = open('../../data/MainSurveyLoan.csv','r')
loandata = list(csv.reader(loanfile))
loanfile.close()
insfile = open('../../data/MainSurveyIns.csv','r')
insdata = list(csv.reader(insfile))
insfile.close()

# Creates a file that reports the consensus levels for each property assignment to each feature (after bucketing into 3 categories) as well as the average per feature
toprow = ['Domain','Feature','Reliability','Relevance','Privacy','Volitionality','Outcome','Cycle','Disparity','By Group','Avg 3 Point Consensus (1-NSE)']

def consensus(data):
    rows = []
    for i in range(int((len(data[0])-15)/9)): # For every feature
        totcon = 0
        featureIndx = 15+i*9
        row = [data[1][13],data[0][featureIndx]] # domain and feature
        for p in range(1,9):
            # Count proportion of responses
            counts = [0,0,0,0,0,0,0]
            for result in data:
                if result[0] == "Study ID":
                    continue
                if result[featureIndx+p] == "Strongly Disagree":
                    counts[0]+=1
                if result[featureIndx+p] == "Disagree":
                    counts[1]+=1
                if result[featureIndx+p] == "Somewhat Disagree":
                    counts[2]+=1
                if result[featureIndx+p] == "Neutral":
                    counts[3]+=1
                if result[featureIndx+p] == "Somewhat Agree":
                    counts[4]+=1
                if result[featureIndx+p] == "Agree":
                    counts[5]+=1
                if result[featureIndx+p] == "Strongly Agree":
                    counts[6]+=1
            normcounts = [x/float(sum(counts)) for x in counts]
            # Bucket responses
            mininormcounts = [sum(normcounts[:3])]+[normcounts[3]]+[sum(normcounts[4:])]
            # Get Shannon entropy and normalize
            nse = stats.entropy(mininormcounts)/np.log(len(mininormcounts))
            row.append(1-nse)
            totcon=totcon+(1-nse)
        # Append average per feature
        row.append(totcon/8)
        rows.append(row)
    return rows

# Do for all domains
recrows = consensus(recdata)
unemrows = consensus(unemdata)
cpsrows = consensus(cpsdata)
hosrows = consensus(hosdata)
loanrows = consensus(loandata)
insrows = consensus(insdata)


allrows = [toprow]+recrows+unemrows+cpsrows+hosrows+loanrows+insrows

confile = open("../../results/ConsensusProps.csv",'w')
write= csv.writer(confile)
write.writerows(allrows)
confile.close()
