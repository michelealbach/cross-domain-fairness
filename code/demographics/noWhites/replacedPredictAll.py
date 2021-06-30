# Cross Domain Fairness
# Michele Albach
# This file calls for all tests using data without caucasian respondents from the survey that replaced relevance with increases accuracy

from replacedPredictorAllDomains import *
from replacedPredictorWithinDomain import *
import csv

rows = [["Prediction","Accuracy","Error","Reliability","Accuracy","Privacy","Volitionality","Causes Outcome","Causes Cycle","Causes Disparity","Caused by Group"]]
rows.append(AllDomains(range(8)))
rows.append(WithinDomain("Bail",range(8)))
rows.append(WithinDomain("Unem",range(8)))
rows.append(WithinDomain("CPS",range(8)))
rows.append(WithinDomain("Hos",range(8)))
rows.append(WithinDomain("Loan",range(8)))
rows.append(WithinDomain("Ins",range(8)))

accsfile = open("ReplacedAccuraciesAndWeightsNoWhites.csv",'w')
write = csv.writer(accsfile)
write.writerows(rows)
accsfile.close()
