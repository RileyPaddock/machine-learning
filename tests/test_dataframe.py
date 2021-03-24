import sys
sys.path.append('src')
from dataframe import DataFrame

df = DataFrame.from_array(
    [['Kevin', 'Fray', 5],
    ['Charles', 'Trapp', 17],
    ['Anna', 'Smith', 13],
    ['Sylvia', 'Mendez', 9]],
    columns = ['firstname', 'lastname', 'age']
)
assert df.select(['firstname','age']).to_array() == [['Kevin', 5],
['Charles', 17],
['Anna', 13],
['Sylvia', 9]]
assert df.where(lambda row: row['age'] > 10).to_array() == [['Charles', 'Trapp', 17],
['Anna', 'Smith', 13]]
assert df.order_by('firstname').to_array() == [['Anna', 'Smith', 13],
['Charles', 'Trapp', 17],
['Kevin', 'Fray', 5],
['Sylvia', 'Mendez', 9]]
assert df.order_by('firstname', ascending=False).to_array() == [['Sylvia', 'Mendez', 9],
['Kevin', 'Fray', 5],
['Charles', 'Trapp', 17],
['Anna', 'Smith', 13]]
assert df.select(['firstname','age']).where(lambda row: row['age'] > 10).order_by('age').to_array() == [['Anna', 13],
['Charles', 17]]

df = DataFrame.from_array(
    [
        ['Kevin Fray', 52, 100],
        ['Charles Trapp', 52, 75],
        ['Anna Smith', 52, 50],
        ['Sylvia Mendez', 52, 100],
        ['Kevin Fray', 53, 80],
        ['Charles Trapp', 53, 95],
        ['Anna Smith', 53, 70],
        ['Sylvia Mendez', 53, 90],
        ['Anna Smith', 54, 90],
        ['Sylvia Mendez', 54, 80],
    ],
    columns = ['name', 'assignmentId', 'score']
)

assert df.group_by('name').to_array() == [
    ['Kevin Fray', [52, 53], [100, 80]],
    ['Charles Trapp', [52, 53], [75, 95]],
    ['Anna Smith', [52, 53, 54], [50, 70, 90]],
    ['Sylvia Mendez', [52, 53, 54], [100, 90, 80]],
]

assert df.group_by('name').aggregate('score', 'count').to_array() == [
   ['Kevin Fray', [52, 53], 2],
   ['Charles Trapp', [52, 53], 2],
   ['Anna Smith', [52, 53, 54], 3],
   ['Sylvia Mendez', [52, 53, 54], 3],
]

assert df.group_by('name').aggregate('score', 'max').to_array() == [
   ['Kevin Fray', [52, 53], 100],
   ['Charles Trapp', [52, 53], 95],
   ['Anna Smith', [52, 53, 54], 90],
   ['Sylvia Mendez', [52, 53, 54], 100],
]

assert df.group_by('name').aggregate('score', 'min').to_array() == [
   ['Kevin Fray', [52, 53], 80],
   ['Charles Trapp', [52, 53], 75],
   ['Anna Smith', [52, 53, 54], 50],
   ['Sylvia Mendez', [52, 53, 54], 80],
]

assert df.group_by('name').aggregate('score', 'sum').to_array() == [
   ['Kevin Fray', [52, 53], 180],
   ['Charles Trapp', [52, 53], 170],
   ['Anna Smith', [52, 53, 54], 210],
   ['Sylvia Mendez', [52, 53, 54], 270],
]

assert df.group_by('name').aggregate('score', 'avg').to_array() == [
   ['Kevin Fray', [52, 53], 90],
   ['Charles Trapp', [52, 53], 85],
   ['Anna Smith', [52, 53, 54], 70],
   ['Sylvia Mendez', [52, 53, 54], 90],
]

df = DataFrame.from_array(
    [['Kevin', 'Fray', 5],
    ['Charles', 'Trapp', 17],
    ['Anna', 'Smith', 13],
    ['Sylvia', 'Mendez', 9]],
    columns = ['firstname', 'lastname', 'age']
)

assert df.query('SELECT firstname, age').to_array() == [['Kevin', 5],
['Charles', 17],
['Anna', 13],
['Sylvia', 9]]

assert df.query("SELECT lastname, firstname, age ORDER_BY age DESC").to_array() == [['Trapp', 'Charles', 17],
['Smith', 'Anna', 13],
['Mendez', 'Sylvia', 9],
['Fray', 'Kevin', 5]]

assert df.query("SELECT firstname ORDER_BY lastname ASC").to_array() == [['Kevin'],
['Sylvia'],
['Anna'],
['Charles']]

df = DataFrame.from_array(
    [['Kevin', 'Fray', 5],
    ['Melvin', 'Fray', 5],
    ['Charles', 'Trapp', 17],
    ['Carl', 'Trapp', 17],
    ['Anna', 'Smith', 13],
    ['Hannah', 'Smith', 13],
    ['Sylvia', 'Mendez', 9],
    ['Cynthia', 'Mendez', 9]],
    columns = ['firstname', 'lastname', 'age']
)

assert df.query("SELECT lastname, firstname, age ORDER_BY age ASC, firstname DESC").to_array() == [['Fray', 'Melvin', 5],
['Fray', 'Kevin', 5],
['Mendez', 'Sylvia', 9],
['Mendez', 'Cynthia', 9],
['Smith', 'Hannah', 13],
['Smith', 'Anna', 13],
['Trapp', 'Charles', 17],
['Trapp', 'Carl', 17]]