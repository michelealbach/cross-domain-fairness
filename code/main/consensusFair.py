# Cross Domain Fairness
# Michele Albach
# This file determines the consensus levels achieved in the fairness judgements in the initial survey using Shannon entropy

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

# Creates a file that reports the proportion of responses for each point and the consensus after bucketing into 3 categories
toprow = ['Domain','Feature','Very Unfair','Unfair','Somewhat Unfair','Combined Unfair','Neutral','Combined Fair','Somewhat Fair','Fair','Very Fair','3 Point Consensus (1-NSE)']

def consensus(data):
    rows = []
    for i in range(int((len(data[0])-15)/9)): # For every feature
        featureIndx = 15+i*9
        # Count proportions of responses
        counts = [0,0,0,0,0,0,0]
        for result in data: # For every respondent
            if result[0] == "Study ID":
                continue
            if result[featureIndx] == "Very Unfair":
                counts[0]+=1
            if result[featureIndx] == "Unfair":
                counts[1]+=1
            if result[featureIndx] == "Somewhat Unfair":
                counts[2]+=1
            if result[featureIndx] == "Neutral":
                counts[3]+=1
            if result[featureIndx] == "Somewhat Fair":
                counts[4]+=1
            if result[featureIndx] == "Fair":
                counts[5]+=1
            if result[featureIndx] == "Very Fair":
                counts[6]+=1
        normcounts = [x/float(sum(counts)) for x in counts]
        frontofrow = [data[1][13],data[0][featureIndx]] # Domain and feature
        # Bucket responses
        mininormcounts = [sum(normcounts[:3])]+[normcounts[3]]+[sum(normcounts[4:])]
        row = frontofrow+normcounts[:3]+mininormcounts+normcounts[4:]
        # Get Shannon Entropy and normalize
        nse = stats.entropy(mininormcounts)/np.log(len(mininormcounts))
        row.append(1-nse)
        rows.append(row)
    return rows

# Do for all domains
recrows = consensus(recdata)
unemrows = consensus(unemdata)
cpsrows = consensus(cpsdata)
hosrows = consensus(hosdata)
loanrows = consensus(loandata)
insrows = consensus(insdata)


allrows = [toprow]
allrows = allrows + recrows
allrows = allrows + unemrows
allrows = allrows + cpsrows
allrows = allrows + hosrows
allrows = allrows + loanrows
allrows = allrows + insrows

confile = open("../../results/ConsensusFair.csv",'w')
write= csv.writer(confile)
write.writerows(allrows)
confile.close()
