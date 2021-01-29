import sys
sys.path.append('src')
from dataframe import DataFrame
from decision_tree import DecisionTree


data = [[x,y,'positive' if x*y > 0 else 'negative'] for x in range(-5,6) if x != 0 for y in range(-5,6) if y != 0]
df = DataFrame.from_array(data, columns = ['x','y', 'class'])
print(len(df.to_array()))

print("Testing random splits")
dt = DecisionTree('random')
dt.fit(df)
total = 0
correct = 0
for entry in df.to_array():
    total += 1
    if dt.classify({'x':entry[0], 'y':entry[1]}) == entry[2]:
        correct += 1
print("Decision Tree:"+str((correct/total)))

data = [[x,y,'A'] for x in range(-5,6) if x!= 0 for y in range(-5,6) if y != 0] + [[x,y,'B'] for x in range(1,6) for y in range(1,6)] + [[x,y,'B'] for x in range(1,6) for y in range(1,6)]
df = DataFrame.from_array(data, columns = ['x','y', 'class'])
print(len(df.to_array()))


print("Testing random splits")
dt = DecisionTree('random')
dt.fit(df)
total = 0
correct = 0
for entry in df.to_array():
    total += 1
    if dt.classify({'x':entry[0], 'y':entry[1]}) == entry[2]:
        correct += 1
print("Decision Tree:"+str((correct/total)))

data = [[x,y,z,'positive' if x>0 and y>0 and z>0 else 'negative'] for x in range(-5,6) if x!=0 for y in range(-5,6) if y!=0 for z in range(-5,6) if z!=0]
df = DataFrame.from_array(data, columns = ['x','y','z', 'class'])
print(len(df.to_array()))


print("Testing random splits")
dt = DecisionTree('random')
dt.fit(df)
total = 0
correct = 0
for entry in df.to_array():
    total += 1
    if dt.classify({'x':entry[0], 'y':entry[1], 'z':entry[2]}) == entry[3]:
        correct += 1
print("Decision Tree:"+str((correct/total)))

data = [[x,y,z,'A'] for x in range(-5,6) if x!= 0 for y in range(-5,6) if y != 0 for z in range(-5,6) if z != 0] + [[x,y,z,'B'] for x in range(1,6) for y in range(1,6) for z in range(1,6)] + [[x,y,z,'B'] for x in range(1,6) for y in range(1,6) for z in range(1,6)]
df = DataFrame.from_array(data, columns = ['x','y','z', 'class'])
print(len(df.to_array()))

print("Testing random splits")
dt = DecisionTree('random')
dt.fit(df)
total = 0
correct = 0
for entry in df.to_array():
    total += 1
    if dt.classify({'x':entry[0], 'y':entry[1], 'z':entry[2]}) == entry[3]:
        correct += 1
print("Decision Tree:"+str((correct/total)))


