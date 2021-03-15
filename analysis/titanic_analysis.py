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

def parse_line(line,quote_symbol = '"'):
    entries = []
    current_entry = []
    inside_quotes = False

    for char in line+',':
        if char == quote_symbol:
            inside_quotes = not inside_quotes
            current_entry.append(char)
        elif char == "," and not inside_quotes:
            entries.append(''.join(current_entry))
            current_entry = []
        else:
            current_entry.append(char)

    return entries

data_types = {
    "PassengerId": int,
    "Survived": int,
    "Pclass": int,
    "Name": str,
    "Sex": str,
    "Age": float,
    "SibSp": int,
    "Parch": int,
    "Ticket": str,
    "Fare": float,
    "Cabin": str,
    "Embarked": str
}
df = DataFrame.from_csv(filepath, data_types=data_types, parser=parse_line)

def surname(name):
    stop = name.index(",")
    surname = []
    for i in range(1,stop):
        surname.append(name[i])
    return ''.join(surname)
df = df.apply("Name", surname)
df = df.rename_column("Name","Surname")

Cabin_types = []
Cabin_nums = []
for cabin in df.data_dict['Cabin']:
    cabin_type = []
    cabin_number = []
    for char in cabin:
        try:
            test = int(char)
            cabin_number.append(char)
        except ValueError:
            if char != ' ':
                cabin_type.append(char)
    if len(cabin_type) > 0:
        Cabin_types.append(''.join(cabin_type))
    else:
        Cabin_types.append(None)
    if len(cabin_number) > 0:
        Cabin_nums.append(int(''.join(cabin_number)))
    else:
        Cabin_nums.append(None)

df = df.append_columns({'CabinType':Cabin_types, 'CabinNumber':Cabin_nums})
df = df.remove_columns(['Cabin'])

Ticket_types = []
Ticket_nums = []
for ticket in df.data_dict['Ticket']:
    ticket_type = []
    ticket_number = []
    try: 
        split = len(ticket) - ticket[::-1].index(' ')
    except ValueError:
        try: 
            int(ticket[-1])
            split = 0
        except ValueError: 
            split = len(ticket)
        
    for i in range(len(ticket)):
        if i < split:
            ticket_type.append(ticket[i])
        else:
            ticket_number.append(ticket[i])
    if len(ticket_type) > 0:
        Ticket_types.append(''.join(ticket_type))
    else:
        Ticket_types.append(None)
    if len(ticket_number) > 0:
        Ticket_nums.append(int(''.join(ticket_number)))
    else:
        Ticket_nums.append(None)

df = df.append_columns({'TicketType':Ticket_types, 'TicketNumber':Ticket_nums})
df = df.remove_columns(['Ticket'])

df = df.set_new_order(["PassengerId", "Survived", "Pclass", "Surname", "Sex", "Age", "SibSp", "Parch", "TicketType", "TicketNumber", "Fare", "CabinType", "CabinNumber", "Embarked"])
print(df.columns)
print(df.to_array()[:5])






# df = DataFrame.from_csv(filepath)
# df = df.remove_columns(["Name", "Ticket", "Fare", "Cabin"])
# pred = df.filter_columns(['Survived'])
# df = df.remove_columns(['Survived','PassengerId'])
# df = df.append_columns(pred.data_dict)
# df = df.apply('Sex', lambda s: 0 if s == 'male' else 1)
# df = df.apply('Embarked', lambda s: 0 if s =='S' else 1 if s == 'C' else 2)
# df = df.apply('Age', lambda i: i if isinstance(i, float) else 0)

# print(df.columns)

# path_to_datasets = '/home/runner/machine-learning/datasets/titanic/'
# filename = 'unkowns_to_predict.csv' 
# filepath = path_to_datasets + filename

# df2 = DataFrame.from_csv(filepath)
# df2 = df2.remove_columns(["Name", "Ticket", "Fare", "Cabin", "PassengerId"])
# df2 = df2.apply('Sex', lambda s: 0 if s == 'male' else 1)
# df2 = df2.apply('Embarked', lambda s: 0 if s =='S' else 1 if s == 'C' else 2)
# df2= df2.apply('Age', lambda i: i if isinstance(i, float) else 0)

# result = [['PassengerId', 'Survived']]

# # liR = LinearRegressor(df, 'Survived')
# # print(liR.coefficients)
# # i = 0
# # for test in df2.to_array():
# #     pred = liR.predict({df2.columns[i]:test[i] for i in range(len(test)-1)})
# #     output = 1 if pred >= 0.5 else 0
# #     result.append([i+892, output])
# #     i+=1

# print("start")

# i = 0
# dt = RandomForest(1000,10,1)
# dt.fit(df)
# for test in df2.to_array():
#     pred = dt.predict({df2.columns[i]:test[i] for i in range(len(test))})
#     result.append([i+892, int(pred)])
#     i += 1

# spamWriter = csv.writer(open('predictions.csv', 'w'), delimiter=',',quotechar="'", quoting=csv.QUOTE_MINIMAL)
# for row in result:
#     #print(row)
#     spamWriter.writerow(row)

# print('end')










# sets = {'train':DataFrame.from_array([elem for elem in df.to_array() if df.to_array().index(elem)%2 == 0], df.columns), 'test': DataFrame.from_array([elem for elem in df.to_array() if df.to_array().index(elem)%2 == 1], df.columns)}
# sets['train'] = sets['train'].remove_columns(['Age'])
# sets['test'] = sets['test'].remove_columns(['Age'])
# print(sets['train'].columns)
# total = 0
# correct = 0
# dt = DecisionTree('gini')
# dt.fit(df)
# for test in sets['test'].to_array():
#     total += 1
#     if dt.classify({df.columns[i]:test[i] for i in range(len(test))}) == test[-2]:
#         correct += 1
# print("Decision Tree:"+str((correct/total)))

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

# for j in [5]:
#     total_te = 0
#     correct_te = 0
#     total_tr = 0
#     correct_tr = 0
#     rt = RandomForest(100,j,1)
#     rt.fit(sets['train'])
#     for test in sets['test'].to_array():
#         total_te += 1
#         if rt.predict({sets['test'].columns[i]:test[i] for i in range(len(test)-1)}) == test[len(test)-2]:
#             correct_te += 1
#     print(str(j)+" Random Tree(s):"+str((correct_te/total_te)))
#     for test in sets['train'].to_array():
#         total_tr += 1
#         if rt.predict({sets['train'].columns[i]:test[i] for i in range(len(test)-1)}) == test[len(test)-2]:
#             correct_tr += 1
#     print(str(j)+" Random Tree(s):"+str((correct_tr/total_tr)))

# sets = {'train':DataFrame.from_array([elem for elem in df.to_array() if df.to_array().index(elem)%2 == 0], df.columns), 'test': DataFrame.from_array([elem for elem in df.to_array() if df.to_array().index(elem)%2 == 1], df.columns)}
# sets['test'] = sets['train']



# total = 0
# correct = 0
# NBC = NaiveBayesClassifier(sets['train'], 'Survived')
# for test in sets['train'].to_array():
#     print(sets['test'].to_array().index(test))
#     total+=1
#     pred = NBC.classify({sets['train'].columns[i]:test[i] for i in range(len(test)-1)})[1]
#     if pred == test[-2]:
#         correct+=1
# print("Naive Bayes: "+str(correct/total))