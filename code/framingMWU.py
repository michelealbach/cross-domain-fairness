# Cross Domain Fairness
# Michele Albach
# This file performs a Mann-Whitney U test to compare results between the survey that explicitly mentioned a "machine learning computer program" and that didn't

from scipy import stats
import csv

fileV1 = open('../data/FramingSurveyNotMentioned.csv', 'r')
fileV2 = open('../data/FramingSurveyMentioned.csv', 'r')
dataV1 = csv.reader(fileV1)
dataV2 = csv.reader(fileV2)
resultsV1 = list(dataV1)
resultsV2 = list(dataV2)
fileV1.close()
fileV2.close()

t_values = ['t-value']
p_values = ['p-value']

for feature in range(16): # For all 16 features asked about in this survey
    v1responses = []
    v2responses = []
    # Count the numbers of responses in each file
    for result in resultsV1:
        if result[0] == 'Study ID':
            continue
        if result[2+feature] == 'very unfair':
            v1responses.append(1)
        if result[2+feature] == 'unfair':
            v1responses.append(2)
        if result[2+feature] == 'somewhat unfair':
            v1responses.append(3)
        if result[2+feature] == 'neutral':
            v1responses.append(4)
        if result[2+feature] == 'somewhat fair':
            v1responses.append(5)
        if result[2+feature] == 'fair':
            v1responses.append(6)
        if result[2+feature] == 'very fair':
            v1responses.append(7)
    for result in resultsV2:
        if result[0] == 'Study ID':
            continue
        if result[2+feature] == 'very unfair':
            v2responses.append(1)
        if result[2+feature] == 'unfair':
            v2responses.append(2)
        if result[2+feature] == 'somewhat unfair':
            v2responses.append(3)
        if result[2+feature] == 'neutral':
            v2responses.append(4)
        if result[2+feature] == 'somewhat fair':
            v2responses.append(5)
        if result[2+feature] == 'fair':
            v2responses.append(6)
        if result[2+feature] == 'very fair':
            v2responses.append(7)

    # Perform MWU
    values = stats.mannwhitneyu(v1responses, v2responses)
    t_values.append(values[0])
    p_values.append(values[1])

top_row = ['Value','Recidivism-crimHis','Recidivism-substance','Recidivism-safety','Recidivism-education','Unemployment-age','Unemployment-gender','Unemployment-education','Unemployment-disability','Hospital-age','Hospital-gender','Hospital-residence','Hospital-hisMjH','Loan-income','Loan-age','Loan-marital','Loan-credit']

b_row = ["Bonferroni Corrected"]

# Apply the Bonferroni correction by multiplying the p-values by the 16 tests
for p in p_values:
    if p=='p-value':
        continue
    b_row.append(p*(len(p_values)-1))

rows = [top_row,t_values,p_values,b_row]

new_file = open('../results/FramingMWU.csv', 'w')
write = csv.writer(new_file)
write.writerows(rows)
new_file.close()

