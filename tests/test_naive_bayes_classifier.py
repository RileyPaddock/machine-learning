import sys
sys.path.append('src')
from naive_bayes_classifier import NaiveBayesClassifier
from dataframe import DataFrame
df = DataFrame.from_array(
    [
        [False, False, False],
        [True, True, True],
        [True, True, True],
        [False, False, False],
        [False, True, False],
        [True, True, True],
        [True, False, False],
        [False, True, False],
        [True, False, True],
        [False, True, False]
    ],
    columns = ['errors', 'links', 'scam']
)
naive_bayes = NaiveBayesClassifier(df, dependent_variable='scam')

print(naive_bayes.probability('scam', True))
#0.4
print(naive_bayes.probability('scam', False))
#0.6

print(naive_bayes.conditional_probability(('errors',True), given=('scam',True)))
#1.0
print(naive_bayes.conditional_probability(('links',False), given=('scam',True)))
#0.25

print(naive_bayes.conditional_probability(('errors',True), given=('scam',False)))
#0.16666666666666666
print(naive_bayes.conditional_probability(('links',False), given=('scam',False)))
#0.5

observed_features = {
    'errors': True,
    'links': False
}
print(naive_bayes.likelihood(('scam',True), observed_features))
#0.1
print(naive_bayes.likelihood(('scam',False), observed_features))
#0.05

print(naive_bayes.classify(observed_features))
#'scam_True'