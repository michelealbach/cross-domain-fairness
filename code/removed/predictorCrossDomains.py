# Cross Domain Fairness
# Michele Albach
# This file performs one test on data from our 'removed' survey (that removed relevance as a property) by training in one domain and testing in another

import csv
import numpy as np
from sklearn import linear_model
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_auc_score

def load(train,test):
    # Open the training data
    file = open("../../data/NoRelevance"+train+".csv",'r')
    traindata = list(csv.reader(file))
    file.close()
    # Open the testing data
    file = open("../../data/NoRelevance"+test+".csv",'r')
    testdata = list(csv.reader(file))
    file.close()

    X_train = []
    Y_train = []
    X_test = []
    Y_test = []

    f = 7 # Number of properties
    f = f+1
    for i in range(len(traindata)): # For every respondent in training data
        for k in range(int((len(traindata[0])-15)/f)): # For every feature
            try:
                ignore =traindata[i][15+k*f]
            except:
                continue
            skip=False
            # append a 1 to Y if rated fair or a 0 if rated unfair
            if traindata[i][15+k*f] == "Very Fair":
                Y_train.append(1)
            elif traindata[i][15+k*f] == "Fair":
                Y_train.append(1)
            elif traindata[i][15+k*f] == "Somewhat Fair":
                Y_train.append(1)
            elif traindata[i][15+k*f] == "Somewhat Unfair":
                Y_train.append(0)
            elif traindata[i][15+k*f] == "Unfair":
                Y_train.append(0)
            elif traindata[i][15+k*f] == "Very Unfair":
                Y_train.append(0)
            else: # rated as neutral or question skipped
                skip=True
            x = []
            for j in range(7): # For every property
                if skip==True:
                    break
                # Append a -3..3 for Strongly Disagree..Strongly Agree
                if traindata[i][16+k*f+j] == "Strongly Disagree":
                    x.append(-3)
                elif traindata[i][16+k*f+j] == "Disagree":
                    x.append(-2)
                elif traindata[i][16+k*f+j] == "Somewhat Disagree":
                    x.append(-1)
                elif traindata[i][16+k*f+j] == "Somewhat Agree":
                    x.append(1)
                elif traindata[i][16+k*f+j] == "Agree":
                    x.append(2)
                elif traindata[i][16+k*f+j] == "Strongly Agree":
                    x.append(3)
                else: # rated as neutral or question skipped
                    x.append(0)
            if skip==False:
                X_train.append(x)

    # Repeat all for test data
    for i in range(len(testdata)):
        for k in range(int((len(testdata[0])-15)/f)): # For every feature
            try:
                ignore = testdata[i][15+k*f]
            except:
                continue
            skip=False
            if testdata[i][15+k*f] == "Very Fair":
                Y_test.append(1)
            elif testdata[i][15+k*f] == "Fair":
                Y_test.append(1)
            elif testdata[i][15+k*f] == "Somewhat Fair":
                Y_test.append(1)
            elif testdata[i][15+k*f] == "Somewhat Unfair":
                Y_test.append(0)
            elif testdata[i][15+k*f] == "Unfair":
                Y_test.append(0)
            elif testdata[i][15+k*f] == "Very Unfair":
                Y_test.append(0)
            else:
                skip=True
            x = []
            for j in range(7): # For every property
                if skip==True:
                    break
                if testdata[i][16+k*f+j] == "Strongly Disagree":
                    x.append(-3)
                elif testdata[i][16+k*f+j] == "Disagree":
                    x.append(-2)
                elif testdata[i][16+k*f+j] == "Somewhat Disagree":
                    x.append(-1)
                elif testdata[i][16+k*f+j] == "Somewhat Agree":
                    x.append(1)
                elif testdata[i][16+k*f+j] == "Agree":
                    x.append(2)
                elif testdata[i][16+k*f+j] == "Strongly Agree":
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
    # Train on train data
    model.fit(X_train,Y_train)
    # Test on test data
    Y_pred = model.predict(X_test)

    return accuracy_score(Y_test,Y_pred),roc_auc_score(Y_test,Y_pred)

def CrossDomain1v1(train_domain,test_domain):
    [X_train,Y_train,X_test,Y_test] = load(train_domain,test_domain)
    [acc,auc]=trainandpredict(X_train,Y_train,X_test,Y_test)
    row = ["Cross "+train_domain+" v "+test_domain]
    row.append(acc)
    row.append("NA")
    return(row)

#print(CrossDomain1v1("Bail","Loan"))
