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

    def swap_columns(self, column1_indx, column2_indx):
        new_columns = [column for column in self.columns]
        new_columns[column1_indx] = self.columns[column2_indx]
        new_columns[column2_indx] = self.columns[column1_indx]
        return DataFrame(self.data_dict, new_columns)

    def rename_column(self,old_name,new_name):
        new_dict = {}
        new_columns = []
        for name in self.columns:
            if name != old_name:
                new_dict[name] = self.data_dict[name]
                new_columns.append(name)
            else:
                new_dict[new_name] = self.data_dict[name]
                new_columns.append(new_name)

        return DataFrame(new_dict, new_columns)

    def rename_columns(self,new_columns):
        new_dict = {}
        for i  in range(len(new_columns)):
            new_dict[new_columns[i]] = self.data_dict[self.columns[i]]
        return DataFrame(new_dict, new_columns)


    def apply(self, column_name, function):
        temp_dict = self.data_dict
        temp_dict[column_name] = [function(elem) for elem in self.data_dict[column_name]]
        return DataFrame(temp_dict)

    def append_pairwise_interactions(self):
        matrix = self.to_array()
        for i in range(len(matrix)):
            for x in range(len(self.columns)):
                for y in range(len(self.columns)):
                    if y > x:
                        matrix[i].append(matrix[i][x] * matrix[i][y])
                
        
        names_with_interaction = [column for column in self.columns]
        for name_1 in self.columns:
            for name_2 in self.columns:
                if self.columns.index(name_2) > self.columns.index(name_1):
                    names_with_interaction.append(name_1 + "_" + name_2)

        new_dict = {}
        for i in range(len(names_with_interaction)):
            new_dict[names_with_interaction[i]] = [matrix[j][i] for j in range(len(matrix))]
        return DataFrame(new_dict)

    def get_column(self, col):
        if col in self.columns:
            if col in self.data_dict.keys():
                return self.data_dict[col].copy()
            else:
                return []


    def create_dummy_variables(self):
        new_dict = self.data_dict
        data_columns = []
        for key in new_dict:
            if isinstance(new_dict[key][0],str) or isinstance(new_dict[key][0],list):
                data_columns.append(key)
        for key in data_columns:
            if isinstance(new_dict[key][0], str):
                for data in self.data_dict[key]:
                    new_dict[data] = [1 if data1 == data else 0 for data1 in self.data_dict[key]]
            elif isinstance(new_dict[key][0],list):
                entries = []
                for data_set in new_dict[key]:
                    for entry in data_set:
                        if entry not in entries:
                            entries.append(entry)
                data = self.get_data_from_list_entry(new_dict[key])
                for i in range(len(entries)):
                    new_dict[entries[i]] = data[i]
            del new_dict[key] 
        return DataFrame(new_dict)

    def get_data_from_list_entry(self,data):
        entries = []
        for data_set in data:
            for entry in data_set:
                if entry not in entries:
                    entries.append(entry)
        new_columns = []
        for entry in entries:
            new_columns.append([])
            for data_set in data:
                if entry in data_set:
                    new_columns[entries.index(entry)].append(1)
                else:
                    new_columns[entries.index(entry)].append(0)
        return new_columns

    def remove_columns(self,columns):
        new_dict = {}
        for column in self.data_dict:
            if column not in columns:
                new_dict[column] = self.data_dict[column]
        return DataFrame(new_dict)

    def append_columns(self, new_dict_data, column_order = None):
        new_dict = self.data_dict
        for key in new_dict_data:
            new_dict[key] = new_dict_data[key]
        return DataFrame(new_dict)
   
    @classmethod
    def from_array(cls, arr, columns):
        data_dict = {}
        for i in range(len(columns)):
            data_dict[columns[i]] = []
            for j in range(len(arr)):
                data_dict[columns[i]].append(arr[j][i])
        df = cls(data_dict)
        return df

    @classmethod
    def from_csv(cls, filepath, data_types, parser, header = False):
        columns = [column for column in data_types]
        with open(filepath, "r") as file:
            read = file.read()
        data = []
        for elem in read.split('\n'):
            if read.split('\n').index(elem) != 0:
                split_line = parser(elem)
                copy = []
                for char in split_line:
                    if len(char) > 0:
                        copy.append(data_types[columns[split_line.index(char)]](char))
                    elif data_types[columns[split_line.index(char)]] == str:
                        copy.append(' ')
                    else:
                        copy.append(0)
                for i in range(len(copy)):
                    if isinstance(copy[i],data_types[columns[i]]):
                        pass
                    else:
                        if data_types[columns[i]] == str:
                            copy[i] = ' '
                        else:
                            copy[i] = 0
                data.append(copy)
            else:
                data.append(columns)
        if header:
            return cls.from_array(data, columns)
        else:
            return cls.from_array([data[i] for i in range(len(data)) if i != 0], data[0])


    def select(self, columns):
        return DataFrame({column:self.data_dict[column] for column in columns})
        #returns a new dataframe of only columns in columns

    def select_rows(self, indicies):
        return DataFrame.from_array([entry for entry in self.to_array() if self.to_array().index(entry) in indicies], self.columns)
        #returns a new dataframe of only the data of certain indicies in the arr

    def remove_row(self,index):
        all_indicies = [i for i in range(len(self.to_array()))]
        all_indicies.remove(index)
        return self.select_rows(all_indicies)

    def where(self, param):
        arr = self.to_array()
        indicies = []
        for row in arr:
            tranformed_row = {self.columns[i]:row[i] for i in range(len(row))}
            if param(tranformed_row):
                indicies.append(arr.index(row))
        return self.select_rows(indicies)


    def order_by(self, column, ascending = True):
        if ascending:
            order = self.sorted_indicies(self.data_dict[column])
            return DataFrame.from_array([self.to_array()[i] for i in order], self.columns)
        else:
            order = self.sorted_indicies(self.data_dict[column])[::-1]
            return DataFrame.from_array([self.to_array()[i] for i in order], self.columns)

        #returns a new dataframe with the rows now sorted in either alphabetical or numerical order 

    def sorted_indicies(self, arr):
        return [y for x,y in sorted([(arr[i],i) for i in range(len(arr))])]

    def set_new_order(self,new_order):
        return DataFrame(self.data_dict, new_order)

    def group_by(self,column):
        distinct = []
        col_i = self.columns.index(column)
        for entry in self.data_dict[column]:
            if entry not in distinct:
                distinct.append(entry)
        
        new = {d:[[] for _ in range(len(self.columns)-1)] for d in distinct}
        for entry in self.to_array():
            for elem_i,elem in enumerate(entry):
                if elem_i != col_i:
                    index = elem_i if elem_i < col_i else elem_i-1
                    new[entry[col_i]][index].append(elem)


        

        new_array = [new[key][:col_i]+[key]+new[key][col_i:] for key in new]

        

        return DataFrame.from_array(new_array, self.columns)

    def aggregate(self,column, method):
        if method == 'max':
            f = max
        elif method == 'min':
            f = min
        elif method == 'count':
            f = len
        elif method == 'sum':
            f = sum 
        elif method == 'avg':
            f = lambda x: sum(x)/len(x)
        return self.apply(column,f)

    def query(self,query):
        keyword = query[:query.index(' ')]
        columns = query[query.index(' ')+1:]
        if keyword == 'SELECT':
            return self.select(columns.split(', '))
        




    