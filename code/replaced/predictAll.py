# Cross Domain Fairness
# Michele Albach
# This file calls for all tests (including cross domain) using all eight properties with 'replaced' survey data (that asked about accuracy instead of relevance) to combine results (including accuracy levels, error levels, and weights) into a table

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

accsfile = open("../../results/ReplacedAccuraciesAndWeights.csv",'w')
write = csv.writer(accsfile)
write.writerows(rows)
accsfile.close()
