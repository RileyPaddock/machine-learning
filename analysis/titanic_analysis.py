import sys
import math
import csv
sys.path.append('src')
from dataframe import DataFrame
from decision_tree import DecisionTree
from decision_tree import Node
from random_forest import RandomForest
from linear_regressor import LinearRegressor
from logistic_regressor import LogisticRegressor
from naive_bayes_classifier import NaiveBayesClassifier
from k_nearest_neighbors_classifier import KNearestNeighborsClassifier

path_to_datasets = '/home/runner/machine-learning/datasets/titanic/'
filename = 'dataset_of_knowns.csv' 
filepath = path_to_datasets + filename


df = DataFrame.from_csv(filepath)
df = df.remove_columns(["Name", "Ticket", "Fare", "Cabin"])
pred = df.filter_columns(['Survived'])
df = df.remove_columns(['Survived','PassengerId'])
df = df.append_columns(pred.data_dict)
df = df.apply('Sex', lambda s: 0 if s == 'male' else 1)
df = df.apply('Embarked', lambda s: 0 if s =='S' else 1 if s == 'C' else 2)
df = df.apply('Age', lambda i: i if isinstance(i, float) else 0)

print(df.columns)

path_to_datasets = '/home/runner/machine-learning/datasets/titanic/'
filename = 'unkowns_to_predict.csv' 
filepath = path_to_datasets + filename

df2 = DataFrame.from_csv(filepath)
df2 = df2.remove_columns(["Name", "Ticket", "Fare", "Cabin", "PassengerId"])
df2 = df2.apply('Sex', lambda s: 0 if s == 'male' else 1)
df2 = df2.apply('Embarked', lambda s: 0 if s =='S' else 1 if s == 'C' else 2)
df2= df2.apply('Age', lambda i: i if isinstance(i, float) else 0)

result = [['PassengerId', 'Survived']]

# liR = LinearRegressor(df, 'Survived')
# print(liR.coefficients)
# i = 0
# for test in df2.to_array():
#     pred = liR.predict({df2.columns[i]:test[i] for i in range(len(test)-1)})
#     output = 1 if pred >= 0.5 else 0
#     result.append([i+892, output])
#     i+=1

i = 0
dt = DecisionTree('gini')
dt.fit(df)
for test in df2.to_array():
    pred = dt.classify({df2.columns[i]:test[i] for i in range(len(test))})
    result.append([i+892, int(pred)])
    i += 1

spamWriter = csv.writer(open('predictions.csv', 'w'), delimiter=',',quotechar="'", quoting=csv.QUOTE_MINIMAL)
for row in result:
    #print(row)
    spamWriter.writerow(row)

print('end')

sets = {'train':DataFrame.from_array([elem for elem in df.to_array() if df.to_array().index(elem)%2 == 0], df.columns), 'test': DataFrame.from_array([elem for elem in df.to_array() if df.to_array().index(elem)%2 == 1], df.columns)}
# sets['train'] = sets['train'].remove_columns(['Age'])
# sets['test'] = sets['test'].remove_columns(['Age'])
print(sets['train'].columns)
total = 0
correct = 0
dt = DecisionTree('gini')
dt.fit(df)
for test in sets['test'].to_array():
    total += 1
    if dt.classify({df.columns[i]:test[i] for i in range(len(test))}) == test[-2]:
        correct += 1
print("Decision Tree:"+str((correct/total)))

# sets = {'train':DataFrame.from_array([elem for elem in df.to_array() if df.to_array().index(elem)%2 == 0], df.columns), 'test': DataFrame.from_array([elem for elem in df.to_array() if df.to_array().index(elem)%2 == 1], df.columns)}


# total = 0
# correct = 0
# Knn = KNearestNeighborsClassifier(10)
# print(1)
# Knn.fit(sets['train'], 'Survived')
# print(2)
# for test in sets['train'].to_array():
#     print(3)
#     total+=1
#     pred = Knn.classify({sets['train'].columns[i]:test[i] for i in range(len(test)-1)})
#     if pred == test[-2]:
#         correct+=1
# print("K Nearest Neighbors: "+str(correct/total))

# total = 0
# correct = 0
# Knn = KNearestNeighborsClassifier(10)
# Knn.fit(sets['train'], 'Survived')
# for test in sets['test'].to_array():
#     total+=1
#     pred = Knn.classify({sets['test'].columns[i]:test[i] for i in range(len(test)-1)})
#     if pred == test[-2]:
#         correct+=1
# print("K Nearest Neighbors: "+str(correct/total))

# sets = {'train':DataFrame.from_array([elem for elem in df.to_array() if df.to_array().index(elem)%2 == 0], df.columns), 'test': DataFrame.from_array([elem for elem in df.to_array() if df.to_array().index(elem)%2 == 1], df.columns)}

# for j in [3,5]:
#     total = 0
#     correct = 0
#     rt = RandomForest(100,j,1)
#     rt.fit(sets['train'])
#     for test in sets['test'].to_array():
#         total += 1
#         if rt.predict({sets['test'].columns[i]:test[i] for i in range(len(test)-1)}) == test[len(test)-2]:
#             correct += 1
#     print(str(j)+" Random Tree(s):"+str((correct/total)))

# sets = {'train':DataFrame.from_array([elem for elem in df.to_array() if df.to_array().index(elem)%2 == 0], df.columns), 'test': DataFrame.from_array([elem for elem in df.to_array() if df.to_array().index(elem)%2 == 1], df.columns)}
# sets['test'] = sets['train']

# total = 0
# correct = 0
# NBC = NaiveBayesClassifier(sets['train'], 'Survived')
# for test in sets['test'].to_array()[0:10]:
#     total+=1
#     pred = NBC.classify({sets['test'].columns[i]:test[i] for i in range(len(test)-1)})[1]
#     if pred == test[-2]:
#         correct+=1
# print("Naive Bayes: "+str(correct/total))

# total = 0
# correct = 0
# NBC = NaiveBayesClassifier(sets['train'], 'Survived')
# for test in sets['train'].to_array()[0:10]:
#     total+=1
#     pred = NBC.classify({sets['train'].columns[i]:test[i] for i in range(len(test)-1)})[1]
#     if pred == test[-2]:
#         correct+=1
# print("Naive Bayes: "+str(correct/total))