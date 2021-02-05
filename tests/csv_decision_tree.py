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


def make_training_sets(data, num_sets):
    training_sets = []
    testing_sets = []
    break_point = len(data.to_array())//num_sets
    for i in range(num_sets):
        sets = [[],[]]
        for j in range(len(data.to_array())):
            if j > (i*break_point) and j <= (i*break_point + break_point):
                sets[1].append(data.to_array()[j])
            else:
                sets[0].append(data.to_array()[j])
        training_sets.append(DataFrame.from_array(sets[0],data.columns))
        testing_sets.append(DataFrame.from_array(sets[1],data.columns))
    print('splits finished')
    return [training_sets, testing_sets]

sets = make_training_sets(df, 5)



total = 0
correct = 0
dt = DecisionTree('gini')
for i in range(len(sets[0])):
    dt.fit(sets[0][i])
    for test in sets[1][i].to_array():
        total += 1
        if dt.classify({'x':test[0], 'y':test[1]}) == test[2]:
            correct += 1
print("Decision Tree:"+str((correct/total)))
for j in [1,10,100,1000]:
    total = 0
    correct = 0
    rt = RandomForest(j)
    for i in range(len(sets[0])):
        rt.fit(sets[0][i])
        for test in sets[1][i].to_array():
            total += 1
            if rt.predict({'x':test[0], 'y':test[1]}) == test[2]:
                correct += 1
    print(str(j)+" Random Tree(s):"+str((correct/total)))

        
