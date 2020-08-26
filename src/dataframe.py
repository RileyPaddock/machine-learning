class DataFrame:
    def __init__(self,dict,column_order = None):
        if column_order is None:
            self.columns = [entry for entry in dict]
        else:
            self.columns = column_order
        self.data_dict = {}
        for column in self.columns:
            self.data_dict[column] = dict[column]
        
    def to_array(self):
        arr = []
        for i in range(len(self.data_dict[self.columns[0]])):
            arr.append([])
            for entry in self.columns:
                arr[i].append(self.data_dict[entry][i])
        return arr

    def filter_columns(self,new_columns):
        return DataFrame(self.data_dict, new_columns)


data_dict = {
    'Pete': [1, 0, 1, 0],
    'John': [2, 1, 0, 2],
    'Sara': [3, 1, 4, 0]
}

df1 = DataFrame(data_dict, column_order = ['Pete', 'John', 'Sara'])
print(df1.data_dict)
# {
#     'Pete': [1, 0, 1, 0],
#     'John': [2, 1, 0, 2],
#     'Sara': [3, 1, 4, 0]
# }

print(df1.to_array())
# [[1, 2, 3]
#  [0, 1, 1]
#  [1, 0, 4]
#  [0, 2, 0]]

print(df1.columns)
#['Pete', 'John', 'Sara']

df2 = df1.filter_columns(['Sara', 'Pete'])
print(df2.to_array())
# [[3, 1],
#  [1, 0],
#  [4, 1],
#  [0, 0]]

print(df2.columns)
# ['Sara', 'Pete']
