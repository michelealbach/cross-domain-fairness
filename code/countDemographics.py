# Cross Domain Fairness
# Michele Albach
# This file counts the number of respondents from each questioned demographic group in our three largest surveys (from which we draw most of our results)

import csv

def count(domain,feats):
    # Open the files to get the data
    file = open("../data/MainSurvey"+domain+".csv",'r')
    secdata = list(csv.reader(file))
    file.close()
    file = open("../data/Accuracy"+domain+".csv",'r')
    accdata = list(csv.reader(file))
    file.close()
    file = open("../data/NoRelevance"+domain+".csv",'r')
    nordata = list(csv.reader(file))
    file.close()

    data = secdata+accdata[1:]+nordata[1:]

    # Count
    age = [0,0,0,0,0,0]
    education = [0,0,0,0,0]
    gender = [0,0,0,0]
    income = [0,0,0,0,0]
    ethnicity = [0,0,0,0,0,0]

    for i in range(1,len(data)):
        if data[i][2]=="18-29":
            age[0] += 1
        elif data[i][2]=="30-39":
            age[1] += 1
        elif data[i][2]=="40-49":
            age[2] += 1
        elif data[i][2]=="50-59":
            age[3] += 1
        elif data[i][2]=="60-69":
            age[4] += 1
        elif data[i][2]=="70 up":
            age[5] += 1
        if data[i][3]=="Less than high School":
            education[0] += 1
        elif data[i][3]=="High School":
            education[1] += 1
        elif data[i][3]=="Associate or Diploma":
            education[2] += 1
        elif data[i][3]=="Bachelor":
            education[3] += 1
        elif data[i][3]=="Graduate":
            education[4] += 1
        if data[i][4]=="Female":
            gender[0] += 1
        elif data[i][4]=="Male":
            gender[1] += 1
        elif data[i][4]=="Nonbinary":
            gender[2] += 1
        elif data[i][5]!="":
            gender[3] += 1
        if data[i][6] == "<25000":
            income[0] += 1
        elif data[i][6] == "25000-50000":
            income[1] += 1
        elif data[i][6] == "50000-75000":
            income[2] += 1
        elif data[i][6] == "75000-100000":
            income[3] += 1
        elif data[i][6] == ">100000":
            income[4] += 1
        if data[i][7] == "true":
            ethnicity[0] += 1
        if data[i][8] == "true":
            ethnicity[1] += 1
        if data[i][9] == "true":
            ethnicity[2] += 1
        if data[i][10] == "true":
            ethnicity[3] += 1
        if data[i][11] == "true":
            ethnicity[4] += 1
        if data[i][12] != "":
            ethnicity[5] += 1

    row=[domain]+age+education+gender+income+ethnicity

    return row

# Save as table
rows = [["Domain","18-29","30-39","40-49","50-59","60-69","70 up","Less than HS","High School","Associate or Diploma","Bachelor","Graduate","Female","Male","Nonbinary","Gender Other","<25000","25000-50000","50000-75000","75000-100000",">100000","Aboriginal","Asian","Black","Caucasian","Hispanic","Ethnicity Other"]]

rows.append(count("Bail",10))
rows.append(count("Unem",10))
rows.append(count("CPS",10))
rows.append(count("Hos",8))
rows.append(count("Loan",10))
rows.append(count("Ins",8))

row = ["Total"]
for col in range(1,len(rows[0])):
    row.append(rows[1][col]+rows[2][col]+rows[3][col]+rows[4][col]+rows[5][col]+rows[6][col])

rows.append(row)

file = open("../results/DemoCounts.csv",'w')
write = csv.writer(file)
write.writerows(rows)
file.close()
