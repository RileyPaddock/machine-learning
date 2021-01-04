import matplotlib.pyplot as plt

data = [[2,13,'B'],[2,13,'B'],[2,13,'B'],[2,13,'B'],[2,13,'B'],[2,13,'B'],
    [3,13,'B'],[3,13,'B'],[3,13,'B'],[3,13,'B'],[3,13,'B'],[3,13,'B'],
    [2,12,'B'],[2,12,'B'],
    [3,12,'A'],[3,12,'A'],
    [3,11,'A'],[3,11,'A'],
    [3,11.5,'A'],[3,11.5,'A'],
    [4,11,'A'],[4,11,'A'],
    [4,11.5,'A'],[4,11.5,'A'],
    [2,10.5,'A'],[2,10.5,'A'],
    [3,10.5,'B'],
    [4,10.5,'A']]

def plot(data):
    classes = {}
    for entry in data:
        classes[entry[2]] = [[],[],[]]
    for entry in data:
        classes[entry[2]][0].append(entry[0])
        classes[entry[2]][1].append(entry[1])
        classes[entry[2]][2].append(20*data.count(entry))

    plt.scatter(x=classes['A'][0], y=classes['A'][1], s=classes['A'][2], c='red')
    plt.scatter(x=classes['B'][0], y=classes['B'][1], s=classes['B'][2], c='blue')
    plt.savefig('scatter_plot.png')

plot(data)