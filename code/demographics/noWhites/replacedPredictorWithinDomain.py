# Cross Domain Fairness
# Michele Albach
# This file performs 1000 50/50 train test splits using data without caucasian survey respondents from a particular domain from the survey that replaced relevance with increases accuracy

import csv
import numpy as np
from sklearn import linear_model
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_auc_score
from scipy import stats
import statsmodels.api as sm

def load(domain,props):
    file = open("../modifiedData/Replaced"+domain+"NoWhites.csv",'r')
    data = list(csv.reader(file))
    file.close()

    X = []
    Y = []
    for i in range(1,len(data)): # For every respondent
        for k in range(int((len(data[0])-15)/9)): # For every feature
            skip=False
            # append a 1 to Y if rated fair or a 0 if rated unfair
            if data[i][15+k*9] == "Very Fair":
                Y.append(1)
            elif data[i][15+k*9] == "Fair":
                Y.append(1)
            elif data[i][15+k*9] == "Somewhat Fair":
                Y.append(1)
            elif data[i][15+k*9] == "Somewhat Unfair":
                Y.append(0)
            elif data[i][15+k*9] == "Unfair":
                Y.append(0)
            elif data[i][15+k*9] == "Very Unfair":
                Y.append(0)
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
                if data[i][16+k*9+j] == "Strongly Disagree":
                    x.append(-3)
                elif data[i][16+k*9+j] == "Disagree":
                    x.append(-2)
                elif data[i][16+k*9+j] == "Somewhat Disagree":
                    x.append(-1)
                elif data[i][16+k*9+j] == "Somewhat Agree":
                    x.append(1)
                elif data[i][16+k*9+j] == "Agree":
                    x.append(2)
                elif data[i][16+k*9+j] == "Strongly Agree":
                    x.append(3)
                else: # rated neutral or question skipped
                    x.append(0)
            if skip==False:
                X.append(x)
    X = np.asarray(X)
    Y = np.asarray(Y)
    return(X,Y)

def trainandpredict(X,Y):
    # Divide the data into 50% test, 50% train
    num_test = int((len(Y)/2)//1)
    num_train = len(Y)-num_test
    zeros = np.zeros(num_test)
    ones = np.ones(num_train)
    rand = np.concatenate([zeros,ones])
    np.random.shuffle(rand)

    Y_train = np.zeros(num_train)
    Y_test = np.zeros(num_test)
    X_train = np.zeros((num_train,X.shape[1]))
    X_test = np.zeros((num_test,X.shape[1]))
    train_indx = 0
    test_indx = 0

    for i in range(len(Y)):
        if rand[i] == 1:
            Y_train[train_indx] = Y[i]
            X_train[train_indx] = X[i]
            train_indx+=1
        else:
            Y_test[test_indx] = Y[i]
            X_test[test_indx] = X[i]
            test_indx+=1

    model = linear_model.LogisticRegression()
    model.fit(X_train,Y_train)

    Y_pred = model.predict(X_test)

    # Repeat with all data in train to get coefficients
    model_w = linear_model.LogisticRegression()
    model_w.fit(X,Y)

    return accuracy_score(Y_test,Y_pred),roc_auc_score(Y_test,Y_pred), model_w.coef_[0]

def WithinDomain(domain,props):
    # 'domain' should be 'rec', 'unem', 'cps', 'hos', 'loan', or 'ins'
    # 'props' should be a list of the integers 0..7 with any property that should be skipped as an 'S' instead
    [X,Y] = load(domain,props)
    accs = []
    # Complete 1000 train/test splits
    for test in range(1000):
        [acc,auc,weights] = trainandpredict(X,Y)
        accs.append(acc)
    mean=np.mean(accs) # Accuracy mean
    error = stats.sem(accs) # Standard Error
    row = ["Within "+domain]
    row.append(mean)
    row.append(error)
    i=0
    # Append a blank for skipped properties for the sake of the table
    for p in props:
        if p=='S':
            row.append("")
        else:
            row.append(weights[i])
            i=i+1
    return row

#print(WithinDomain("Ins",[0,1,2,3,4,5,6,7]))
