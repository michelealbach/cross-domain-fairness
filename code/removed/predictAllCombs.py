# Cross Domain Fairness
# Michele Albach
# This file creates one table (using 'removed' survey data) which performs every test with one property removed and every single property test (for all domains). The resulting table indicates which properties were used in a given test by showing the weights for all used properties.

from itertools import combinations
from predictorAllDomains import *
from predictorWithinDomain import *
import csv

rows = [["Prediction","Accuracy","Error","Reliability","Privacy","Volitionality","Causes Outcome","Causes Cycle","Causes Disparity","Caused by Group"]]

props = [0,1,2,3,4,5,6]
rows.append(AllDomains(props))
for i in range(7):
    props=[0,1,2,3,4,5,6]
    props[i] = 'S'
    rows.append(AllDomains(props))
for i in range(7):
    props=['S','S','S','S','S','S','S']
    props[i]=i
    rows.append(AllDomains(props))
props = [0,1,2,3,4,5,6]
rows.append(WithinDomain("Rec",props))
for i in range(7):
    props=[0,1,2,3,4,5,6]
    props[i] = 'S'
    rows.append(WithinDomain("Rec",props))
for i in range(7):
    props=['S','S','S','S','S','S','S']
    props[i]=i
    rows.append(WithinDomain("Rec",props))
props = [0,1,2,3,4,5,6]
rows.append(WithinDomain("Unem",props))
for i in range(7):
    props=[0,1,2,3,4,5,6]
    props[i] = 'S'
    rows.append(WithinDomain("Unem",props))
for i in range(7):
    props=['S','S','S','S','S','S','S']
    props[i]=i
    rows.append(WithinDomain("Unem",props))
props = [0,1,2,3,4,5,6]
rows.append(WithinDomain("CPS",props))
for i in range(7):
    props=[0,1,2,3,4,5,6]
    props[i] = 'S'
    rows.append(WithinDomain("CPS",props))
for i in range(7):
    props=['S','S','S','S','S','S','S']
    props[i]=i
    rows.append(WithinDomain("CPS",props))
props = [0,1,2,3,4,5,6]
rows.append(WithinDomain("Hos",props))
for i in range(7):
    props=[0,1,2,3,4,5,6]
    props[i] = 'S'
    rows.append(WithinDomain("Hos",props))
for i in range(7):
    props=['S','S','S','S','S','S','S']
    props[i]=i
    rows.append(WithinDomain("Hos",props))
props = [0,1,2,3,4,5,6]
rows.append(WithinDomain("Loan",props))
for i in range(7):
    props=[0,1,2,3,4,5,6]
    props[i] = 'S'
    rows.append(WithinDomain("Loan",props))
for i in range(7):
    props=['S','S','S','S','S','S','S']
    props[i]=i
    rows.append(WithinDomain("Loan",props))
props = [0,1,2,3,4,5,6]
rows.append(WithinDomain("Ins",props))
for i in range(7):
    props=[0,1,2,3,4,5,6]
    props[i] = 'S'
    rows.append(WithinDomain("Ins",props))
for i in range(7):
    props=['S','S','S','S','S','S','S']
    props[i]=i
    rows.append(WithinDomain("Ins",props))
    
accsfile = open("../../results/RemovedCombsAccuraciesAndWeights.csv",'w')
write = csv.writer(accsfile)
write.writerows(rows)
accsfile.close()
