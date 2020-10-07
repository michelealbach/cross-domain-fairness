Pilot resuts:
Necessity.csv - For every domain, gives the proportion of respondents who checked each property at least once. The lowest propertion is 0.33 ('caused by group' in bail).
Sufficiency.csv - For every domain, gives the propertion of respondents who used the fill-in-the-blank 'other' option. The highest propertion is 0.09 (in loan).
FramingMWU.csv - For all 16 features (from four domains) asked about in this survey, gives the p-values obtained from comparing the responses to the 'mentioned' and 'not-mentioned' categories.

Consensus results:
ConsensusFair.csv - For every feature in every domain, gives the proportion of responses for all 7 possible answers (as well as the bucketed proportions), and the consensus levels (1 minus shannon entropy normalized between 0 and 1).
ConsensusProps.csv - For every feature in every domain, gives the consensus levels achieved for each property assignment question, as well as the average per feature. This table (combined with the consensus column from the above file) is presented in our appendix.

Initial survey results:
MainAccuraciesAndWeights.csv - Presents the achieved accuracies and errors from our logistic regression classifiers for the pooled, within domain, and cross domain predictors (which list their domains as 'trained' v 'tested'). Also gives the weights associated with each predictive property. The weights are not listed for the cross domain predictors because they are identical to the within domain predictor weights (for whichever domain was trained on). 
MainCombsAccuraciesAndWeights.csv - Presents the accuracies and errors when predicting with all but one property, or only a single property per domain (and repeats the full property accuracy level for comparison). The properties used in a given predictor are represented by having a listed weight. It is of note that removing 'relevance' substantially decreases accuracy, and that 'relevance' alone performs better than other single property predictors.
MainAllCombsWOAccuraciesAndWeights.csv - Presents the accuracies and errors for every combination of predictive properties excluding relevance to show that relevance alone performs better than them all in every domain (and all pooled).

Replaced with accuracy survey results:
ReplacedAccuraciesAndWeights.csv - Identical to MainAccuraciesAndWeights.csv but using 'replaced' survey results.
ReplacedCombsAccuraciesAndWeights.csv - Identical to MainCombsAccuraciesAndWeights.csv but using 'replaced' survey results.
ReplacedAllCombsWOAccuraciesAndWeights.csv - Identical to MainAllCombsWOAccuraciesAndWeights.csv but using 'replaced' survey results.

Removed relevance survey results:
RemovedAccuraciesAndWeights.csv - Identical to MainAccuraciesAndWeights.csv but using 'removed' survey results.
RemovedCombsAccuraciesAndWeights.csv - Identical to MainCombsAccuraciesAndWeights.csv but using 'removed' survey results.

Table and figures as in paper:
Table1.csv - Presents the accuracies and errors for the pooled, within domain, and cross domain predictors. Cross domain accuracies are averages from training or testing over each of the other five domains.
Figure1.pdf - Presents and compares the weights for each property by domain for every survey batch.
Figure2.pdf - Presents and compares accuracy levels achieved by various predictors.

DemoCounts - Presents the number of respondents from each questioned demographic group (by assigned domain) that answered our three primary surveys.
