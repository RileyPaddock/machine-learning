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

    def apply(self, column_name, function):
        temp_dict = self.data_dict
        temp_dict[column_name] = [function(elem) for elem in self.data_dict[column_name]]
        return DataFrame(temp_dict)

    def append_pairwise_interactions(self):
        matrix = self.to_array()
        data1 = []
        data2 = []
        for x in range(1,len(matrix[0])+1):
            for y in range(2,len(matrix[0])+1):
                if y > x:
                    data1.append(x-1)
                    data2.append(y-1)
        for i in range(len(matrix)):
            for j in range(len(self.columns)):
                matrix[i].append(matrix[i][data1[j]] * matrix[i][data2[j]])
        
        names_with_interaction = [column for column in self.columns]
        for name_1 in self.columns:
            for name_2 in self.columns:
                if self.columns.index(name_2) > self.columns.index(name_1):
                    names_with_interaction.append(name_1 + "_" + name_2)

        new_dict = {}
        for i in range(len(names_with_interaction)):
            new_dict[names_with_interaction[i]] = [matrix[j][i] for j in range(len(matrix))]
        return DataFrame(new_dict)

    def create_dummy_variables(self):
        new_dict = self.data_dict
        data_columns = []
        for key in new_dict:
            if isinstance(new_dict[key][0],str):
                data_columns.append(key)
        for key in data_columns:
            for data in self.data_dict[key]:
                new_dict[key + "_" + data] = [1 if data1 == data else 0 for data1 in self.data_dict[key]]
            del new_dict[key]
        return DataFrame(new_dict)

    def remove_columns(self,columns):
        new_dict = {}
        for column in self.data_dict:
            if column not in columns:
                new_dict[column] = self.data_dict[column]
        return DataFrame(new_dict)

    def append_columns(self, new_dict_data):
        new_dict = self.data_dict
        for key in new_dict_data:
            new_dict[key] = new_dict_data[key]
        return DataFrame(new_dict)
