# Cross Domain Fairness
# Michele Albach
# This file performs one test by training on the data from one domain and testing on the remaining five (from the second survey)

import csv
import numpy as np
from sklearn import linear_model
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_auc_score

def load(exclude,props):
    # 'exclude' indicates the single domain to train on
    file = open("../data/SecondSurveyBail.csv",'r')
    recdata = list(csv.reader(file))
    file.close()
    file = open("../data/SecondSurveyUnem.csv",'r')
    unemdata = list(csv.reader(file))
    file.close()
    file = open("../data/SecondSurveyCPS.csv",'r')
    cpsdata = list(csv.reader(file))
    file.close()
    file = open("../data/SecondSurveyHos.csv",'r')
    hosdata = list(csv.reader(file))
    file.close()
    file = open("../data/SecondSurveyLoan.csv",'r')
    loandata = list(csv.reader(file))
    file.close()
    file = open("../data/SecondSurveyIns.csv",'r')
    insdata = list(csv.reader(file))
    file.close()

    # Divide train and test data
    if exclude == "Bail":
        testdata = unemdata[1:]+cpsdata[1:]+hosdata[1:]+loandata[1:]+insdata[1:]
        traindata = recdata[1:]
    if exclude == "Unem":
        testdata = recdata[1:]+cpsdata[1:]+hosdata[1:]+loandata[1:]+insdata[1:]
        traindata = unemdata[1:]
    if exclude == "CPS":
        testdata = unemdata[1:]+recdata[1:]+hosdata[1:]+loandata[1:]+insdata[1:]
        traindata = cpsdata[1:]
    if exclude == "Hos":
        testdata = unemdata[1:]+cpsdata[1:]+recdata[1:]+loandata[1:]+insdata[1:]
        traindata = hosdata[1:]
    if exclude == "Loan":
        testdata = unemdata[1:]+cpsdata[1:]+hosdata[1:]+recdata[1:]+insdata[1:]
        traindata = loandata[1:]
    if exclude == "Ins":
        testdata = unemdata[1:]+cpsdata[1:]+hosdata[1:]+loandata[1:]+recdata[1:]
        traindata = insdata[1:]

    X_train = []
    Y_train = []
    X_test = []
    Y_test = []
    # Training data:
    for i in range(len(traindata)): # For every respondent
        for k in range(int((len(traindata[0])-15)/9)): # For every feature
            try:
                ignore =traindata[i][15+k*9]
            except:
                continue
            skip=False
            # append a 1 to Y if rated fair or a 0 if rated unfair
            if traindata[i][15+k*9] == "Very Fair":
                Y_train.append(1)
            elif traindata[i][15+k*9] == "Fair":
                Y_train.append(1)
            elif traindata[i][15+k*9] == "Somewhat Fair":
                Y_train.append(1)
            elif traindata[i][15+k*9] == "Somewhat Unfair":
                Y_train.append(0)
            elif traindata[i][15+k*9] == "Unfair":
                Y_train.append(0)
            elif traindata[i][15+k*9] == "Very Unfair":
                Y_train.append(0)
            else: # rated as neutral or question skipped
                skip=True
            x = []
            for j in props: # For every property
                if j=='S':
                    # This property is skipped for this test
                    continue
                if skip==True:
                    break
                # Append a -3..3 for Strongly Disagree..Strongly Agree
                if traindata[i][16+k*9+j] == "Strongly Disagree":
                    x.append(-3)
                elif traindata[i][16+k*9+j] == "Disagree":
                    x.append(-2)
                elif traindata[i][16+k*9+j] == "Somewhat Disagree":
                    x.append(-1)
                elif traindata[i][16+k*9+j] == "Somewhat Agree":
                    x.append(1)
                elif traindata[i][16+k*9+j] == "Agree":
                    x.append(2)
                elif traindata[i][16+k*9+j] == "Strongly Agree":
                    x.append(3)
                else: # rated neutral of skipped
                    x.append(0)
            if skip==False:
                X_train.append(x)
    # Repeat for testing data:
    for i in range(len(testdata)):
        for k in range(int((len(testdata[0])-15)/9)):
            try:
                ignore = testdata[i][15+k*9]
            except:
                continue
            skip=False
            if testdata[i][15+k*9] == "Very Fair":
                Y_test.append(1)
            elif testdata[i][15+k*9] == "Fair":
                Y_test.append(1)
            elif testdata[i][15+k*9] == "Somewhat Fair":
                Y_test.append(1)
            elif testdata[i][15+k*9] == "Somewhat Unfair":
                Y_test.append(0)
            elif testdata[i][15+k*9] == "Unfair":
                Y_test.append(0)
            elif testdata[i][15+k*9] == "Very Unfair":
                Y_test.append(0)
            else:
                skip=True
            x = []
            for j in props:
                if j=='S':
                    continue
                if skip==True:
                    break
                if testdata[i][16+k*9+j] == "Strongly Disagree":
                    x.append(-3)
                elif testdata[i][16+k*9+j] == "Disagree":
                    x.append(-2)
                elif testdata[i][16+k*9+j] == "Somewhat Disagree":
                    x.append(-1)
                elif testdata[i][16+k*9+j] == "Somewhat Agree":
                    x.append(1)
                elif testdata[i][16+k*9+j] == "Agree":
                    x.append(2)
                elif testdata[i][16+k*9+j] == "Strongly Agree":
                    x.append(3)
                else:
                    x.append(0)
            if skip==False:
                X_test.append(x)
    X_train = np.asarray(X_train)
    Y_train = np.asarray(Y_train)
    X_test = np.asarray(X_test)
    Y_test = np.asarray(Y_test)
    return(X_train,Y_train,X_test,Y_test)

def trainandpredict(X_train,Y_train,X_test,Y_test):
    model = linear_model.LogisticRegression()
    model.fit(X_train,Y_train)

    Y_pred = model.predict(X_test)

    return accuracy_score(Y_test,Y_pred),roc_auc_score(Y_test,Y_pred),model.coef_[0]

def CrossDomain1v5(train_domain,props):
    # 'train_domain' should be 'Bail', 'Unem', 'CPS', 'Hos', 'Loan', or 'Ins'
    # 'props' should be a list of the integers 0..7 with any property that should be skipped as an 'S' instead    
    [X_train,Y_train,X_test,Y_test] = load(train_domain,props)
    [acc,auc,weights]=trainandpredict(X_train,Y_train,X_test,Y_test)
    row = ["Cross Train "+train_domain]
    row.append(acc)
    row.append("NA") # No error since only 1 test done
    i=0
    # Append a blank for skipped properties for the sake of the table
    for p in props:
        if p=='S':
            row.append("")
        else:
            row.append(weights[i])
            i=i+1
    return(row)

print(CrossDomain1v5("Bail",[0,1,2,3,4,5,6,7]))
