# Cross Domain Fairness
# Michele Albach
# This file calls for all tests (including cross domain) using all eight properties with initial survey data to combine results (including accuracy levels, error levels, and weights) into large and small tables

from predictorAllDomains import *
from predictorWithinDomain import *
from predictorCrossDomains import *
import csv
from scipy import stats

rows = [["Prediction","Accuracy","Error","Reliability","Relevance","Privacy","Volitionality","Causes Outcome","Causes Cycle","Causes Disparity","Caused by Group"]]
domains = ["Bail","CPS","Hos","Ins","Loan","Unem"]

rows.append(AllDomains(range(8)))

for domain in domains:
    rows.append(WithinDomain(domain,range(8)))

for domain1 in domains:
    for domain2 in domains:
        if domain1==domain2:
            continue
        rows.append(CrossDomain1v1(domain1,domain2))

accsfile = open("../../results/MainAccuraciesAndWeights.csv",'w')
write = csv.writer(accsfile)
write.writerows(rows)
accsfile.close()

smallrows = [["Domain","Within","Error","Cross Trained","Error","Cross Tested","Error"]]

for i in range(len(domains)):
    row = [domains[i]]
    row.append(rows[i+2][1])
    row.append(rows[i+2][2])
    train = [rows[8+i*5][1],rows[9+i*5][1],rows[10+i*5][1],rows[11+i*5][1],rows[12+i*5][1]]
    row.append(sum(train)/len(train))
    row.append(stats.sem(train))
    test = []
    for j in range(i):
        test.append(rows[8+i-1+j*5][1])
    for j in range(i+1,6):
        k = j-i-1
        test.append(rows[8+(i+1)*5+i+k*5][1])
    row.append(sum(test)/len(test))
    row.append(stats.sem(test))
    smallrows.append(row)
smallrows.append(["All",rows[1][1],rows[1][2],"NA"])
    
file = open("../../results/Table1.csv",'w')
write = csv.writer(file)
write.writerows(smallrows)
file.close()
