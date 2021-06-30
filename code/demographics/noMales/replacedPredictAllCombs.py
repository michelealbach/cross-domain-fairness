# Cross Domain Fairness
# Michele Albach
# This file creates two tables (both using data without male survey respondents from the survey that replaced relevance with increases accuracy). The first performs every test with one property removed and every single property test (for all domains), and the second performs tests using only relevance as a predictive property and then performs all possible combinations of properties excluding relevance to show that they all perform worse. This is repeated for all individual domains. The resulting table indicates which properties were used in a given test by showing the weights for all used properties.

from itertools import combinations
from replacedPredictorAllDomains import *
from replacedPredictorWithinDomain import *
import csv


rows = [["Prediction","Accuracy","Error","Reliability","Accuracy","Privacy","Volitionality","Causes Outcome","Causes Cycle","Causes Disparity","Caused by Group"]]
rows2 = [["Prediction","Accuracy","Error","Reliability","Accuracy","Privacy","Volitionality","Causes Outcome","Causes Cycle","Causes Disparity","Caused by Group"]]


props = [0,1,2,3,4,5,6,7]
rows.append(AllDomains(props))
for i in range(8):
    props=[0,1,2,3,4,5,6,7]
    props[i] = 'S'
    rows.append(AllDomains(props))
for i in range(8):
    props=['S','S','S','S','S','S','S','S']
    props[i] = i
    rows.append(AllDomains(props))
    if i==1:
        rows2.append(AllDomains(props))
excacc = [0,2,3,4,5,6,7]
for l in [1,2,3,4,5,6]:
    combs = combinations(excacc,l)
    for comb in combs:
        props = [0,'S',2,3,4,5,6,7]
        for c in comb:
            props[c]='S'
        rows2.append(AllDomains(props))

props = [0,1,2,3,4,5,6,7]
rows.append(WithinDomain("Bail",props))
for i in range(8):
    props=[0,1,2,3,4,5,6,7]
    props[i] = 'S'
    rows.append(WithinDomain("Bail",props))
for i in range(8):
    props=['S','S','S','S','S','S','S','S']
    props[i] = i
    rows.append(WithinDomain("Bail",props))
    if i==1:
        rows2.append(WithinDomain("Bail",props))
excacc = [0,2,3,4,5,6,7]
for l in [1,2,3,4,5,6]:
    combs = combinations(excacc,l)
    for comb in combs:
        props = [0,'S',2,3,4,5,6,7]
        for c in comb:
            props[c]='S'
        rows2.append(WithinDomain("Bail",props))

props = [0,1,2,3,4,5,6,7]
rows.append(WithinDomain("Unem",props))
for i in range(8):
    props=[0,1,2,3,4,5,6,7]
    props[i] = 'S'
    rows.append(WithinDomain("Unem",props))
for i in range(8):
    props=['S','S','S','S','S','S','S','S']
    props[i] = i
    rows.append(WithinDomain("Unem",props))
    if i==1:
        rows2.append(WithinDomain("Unem",props))
excacc = [0,2,3,4,5,6,7]
props = [0,'S',2,3,4,5,6,7]
for l in [1,2,3,4,5,6]:
    combs = combinations(excacc,l)
    for comb in combs:
        props = [0,'S',2,3,4,5,6,7]
        for c in comb:
            props[c]='S'
        rows2.append(WithinDomain("Unem",props))

props = [0,1,2,3,4,5,6,7]
rows.append(WithinDomain("CPS",props))
for i in range(8):
    props=[0,1,2,3,4,5,6,7]
    props[i] = 'S'
    rows.append(WithinDomain("CPS",props))
for i in range(8):
    props=['S','S','S','S','S','S','S','S']
    props[i] = i
    rows.append(WithinDomain("CPS",props))
    if i==1:
        rows2.append(WithinDomain("CPS",props))        
excacc = [0,2,3,4,5,6,7]
props = [0,'S',2,3,4,5,6,7]
for l in [1,2,3,4,5,6]:
    combs = combinations(excacc,l)
    for comb in combs:
        props = [0,'S',2,3,4,5,6,7]
        for c in comb:
            props[c]='S'
        rows2.append(WithinDomain("CPS",props))

props = [0,1,2,3,4,5,6,7]
rows.append(WithinDomain("Hos",props))
for i in range(8):
    props=[0,1,2,3,4,5,6,7]
    props[i] = 'S'
    rows.append(WithinDomain("Hos",props))
for i in range(8):
    props=['S','S','S','S','S','S','S','S']
    props[i] = i
    rows.append(WithinDomain("Hos",props))
    if i==1:
        rows2.append(WithinDomain("Hos",props))        
excacc = [0,2,3,4,5,6,7]
props = [0,'S',2,3,4,5,6,7]
for l in [1,2,3,4,5,6]:
    combs = combinations(excacc,l)
    for comb in combs:
        props = [0,'S',2,3,4,5,6,7]
        for c in comb:
            props[c]='S'
        rows2.append(WithinDomain("Hos",props))

props = [0,1,2,3,4,5,6,7]
rows.append(WithinDomain("Loan",props))
for i in range(8):
    props=[0,1,2,3,4,5,6,7]
    props[i] = 'S'
    rows.append(WithinDomain("Loan",props))
for i in range(8):
    props=['S','S','S','S','S','S','S','S']
    props[i] = i
    rows.append(WithinDomain("Loan",props))
    if i==1:
        rows2.append(WithinDomain("Loan",props))
excacc = [0,2,3,4,5,6,7]
props = [0,'S',2,3,4,5,6,7]
for l in [1,2,3,4,5,6]:
    combs = combinations(excacc,l)
    for comb in combs:
        props = [0,'S',2,3,4,5,6,7]
        for c in comb:
            props[c]='S'
        rows2.append(WithinDomain("Loan",props))

props = [0,1,2,3,4,5,6,7]
rows.append(WithinDomain("Ins",props))
for i in range(8):
    props=[0,1,2,3,4,5,6,7]
    props[i] = 'S'
    rows.append(WithinDomain("Ins",props))
for i in range(8):
    props=['S','S','S','S','S','S','S','S']
    props[i] = i
    rows.append(WithinDomain("Ins",props))
    if i==1:
        rows2.append(WithinDomain("Ins",props))
excacc = [0,2,3,4,5,6,7]
props = [0,'S',2,3,4,5,6,7]
for l in [1,2,3,4,5,6]:
    combs = combinations(excacc,l)
    for comb in combs:
        props = [0,'S',2,3,4,5,6,7]
        for c in comb:
            props[c]='S'
        rows2.append(WithinDomain("Ins",props))
    
accsfile = open("ReplacedCombsAccuraciesAndWeightsNoMales.csv",'w')
write = csv.writer(accsfile)
write.writerows(rows)
accsfile.close()
accsfile = open("ReplacedAllCombsWOAccuraciesAndWeightsNoMales.csv",'w')
write = csv.writer(accsfile)
write.writerows(rows2)
accsfile.close()
