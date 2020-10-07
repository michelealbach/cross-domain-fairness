To generate all results (in results folder), run:
pilot/necessaryTest.py
pilot/sufficientTest.py
pilot/framingMWU.py
main/consensusFair.py
main/consensusProps.py
main/predictAll.py
main/predictAllCombs.py
replaced/predictAll.py
replaced/predictAllCombs.py
removed/predictAll.py
removed/predictAllCombs.py
makeWeightsFigure.py
makeAccuraciesFigure.py
countDemographics.py

Code Descriptions:

makeWeightsFigure.py - makes Figure 1
makeAccuraciesFigure.py - makes Figure 2
countDemographics.py - counts the number of respondents from each questioned demographic group

pilots:
Performs all pilot study analyses
necessaryTest.py - determines that the eight properties are necessary in each domain
sufficientTest.py - determines that the eight properties are sufficient to each domain
framingMWU.py - performs a Mann-Whitney U test to compare results between the two framing surveys

main:
Performs the consensus and prediction analyses using the main survey data
consensusFair.py - determines the consensus levels achieved in the fairness judgements
consensusProps.py - determines the consensus levels achieved in the property assignments
predictorAllDomains.py - performs 1000 50/50 train test splits on all pooled main survey data
predictorWithinDomain.py - performs 1000 50/50 train test splits on a particular domain of main survey data
predictorCrossDomains.py - performs one test by training in one domain and testing in another using main survey data
predictAll.py - calls all 'predictor' files and makes a table with all tests using all eight properties (using main survey data)
predictAllCombs - calls all 'predictor' files and makes tables with tests using multiple combinations of properties (using main survey data)

replaced:
Performs the prediction analyses using the data where 'relevance' is replaced by 'increases accuracy'
predictorAllDomains.py - performs 1000 50/50 train test splits on all pooled replaced survey data
predictorWithinDomain.py - performs 1000 50/50 train test splits on a particular domain of replaced survey data
predictorCrossDomains.py - performs one test by training in one domain and testing in another using replaced survey data
predictAll.py - calls all 'predictor' files and makes a table with all tests using all eight properties (using replaced survey data)
predictAllCombs - calls all 'predictor' files and makes tables with tests using multiple combinations of properties (using replaced survey data)

removed:
Performs the prediction analyses using the data where 'relevance' is removed entirely
predictorAllDomains.py - performs 1000 50/50 train test splits on all pooled removed survey data
predictorWithinDomain.py - performs 1000 50/50 train test splits on a particular domain of removed survey data
predictorCrossDomains.py - performs one test by training in one domain and testing in another using removed survey data
predictAll.py - calls all 'predictor' files and makes a table with all tests using all eight properties (using removed survey data)
predictAllCombs - calls all 'predictor' files and makes a table with tests using multiple combinations of properties (using removed survey data)

