# Cross Domain Fairness
# Michele Albach
# This file calls for all tests using data without male respondents from the survey that removed relevance entirely

from removedPredictorAllDomains import *
from removedPredictorWithinDomain import *
import csv

rows = [["Prediction","Accuracy","Error","Reliability","Privacy","Volitionality","Causes Outcome","Causes Cycle","Causes Disparity","Caused by Group"]]
f=7
rows.append(AllDomains(range(7)))
rows.append(WithinDomain("Bail",range(7)))
rows.append(WithinDomain("Unem",range(7)))
rows.append(WithinDomain("CPS",range(7)))
rows.append(WithinDomain("Hos",range(7)))
rows.append(WithinDomain("Loan",range(7)))
rows.append(WithinDomain("Ins",range(7)))

accsfile = open("RemovedAccuraciesAndWeightsNoMales.csv",'w')
write = csv.writer(accsfile)
write.writerows(rows)
accsfile.close()
