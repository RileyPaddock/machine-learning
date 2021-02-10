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
df = df.rename_columns(['x','y','class', 'node_index'])
print(df.columns)


def make_training_sets(data):
    train = [elem for elem in data.to_array() if data.to_array().index(elem) <= len(data.to_array())//2]
    test = [elem for elem in data.to_array() if data.to_array().index(elem) > len(data.to_array())//2]
    return [DataFrame.from_array(train,data.columns), DataFrame.from_array(test,data.columns)]

sets = make_training_sets(df)



for j in [1,10,100,1000,10000]:
    total = 0
    correct = 0
    rt = RandomForest(j,4,0.3)
    rt.fit(sets[0])
    for test in sets[1].to_array():
        total += 1
        if rt.predict({'x':test[0], 'y':test[1]}) == test[2]:
            correct += 1
    print(str(j)+" Random Tree(s):"+str((correct/total)))

        
