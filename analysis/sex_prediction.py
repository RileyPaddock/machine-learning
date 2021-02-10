import sys
sys.path.append('src')
from dataframe import DataFrame
from decision_tree import DecisionTree
from decision_tree import Node
from random_forest import RandomForest

path_to_datasets = '/home/runner/machine-learning/datasets/'
filename = 'freshman_lbs.csv' 
filepath = path_to_datasets + filename

df = DataFrame.from_csv(filepath)
df = df.remove_columns(["Weight (lbs, Apr)", "BMI (Apr)"])
df = df.swap_columns(0,2)
df = df.append_columns({'node_index':[i for i in range(len(df.to_array()))]})

def make_sets(df):
    dataframe = df.to_array()
    train = DataFrame.from_array([entry for entry in dataframe if dataframe.index(entry) <= len(dataframe)//2], df.columns)
    test = DataFrame.from_array([entry for entry in dataframe if dataframe.index(entry) > len(dataframe)//2],df.columns)
    return [train, test]


sets = make_sets(df)
total = 0
correct = 0
dt = DecisionTree('gini')
dt.fit(sets[0])
for test in sets[1].to_array():
    total += 1
    prediction = {df.columns[i]:test[i] for i in (range(len(test)-1))}
    if dt.classify(prediction) == test[2]:
        correct += 1
    else:
        print(sets[1].to_array().index(test)+len(sets[0].to_array()))
print("Decision Tree:"+str((correct/total)))