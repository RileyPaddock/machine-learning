class NaiveBayesClassifier:
    def __init__(self, dataframe, dependent_variable):
        self.df = dataframe
        self.dep_var = dependent_variable
        self.given_true = self.df.select_rows_where(lambda x: x[self.dep_var] == 1)
        self.given_false = self.df.select_rows_where(lambda x: x[self.dep_var] == 0)
        self.likeliehood_const_t = self.df.data_dict[self.dep_var].count(1)/len(self.df.data_dict[self.dep_var])
        self.likeliehood_const_f = self.df.data_dict[self.dep_var].count(0)/len(self.df.data_dict[self.dep_var])

        self.hl = {self.df.columns[i]:sum([elem[i] for elem in self.df.to_array()])/len(self.df.to_array()) for i in range(len(self.df.columns)) if self.df.columns[i] != self.dep_var}

    def conditional_probability(self, probability, given):
        total_given = self.given_true if given[1] == 1 else self.given_false
        total_true = total_given.select_rows_where(lambda x: True if (x[probability[0]]<self.hl[probability[0]] and probability[1]< self.hl[probability[0]]) or (x[probability[0]]>=self.hl[probability[0]] and probability[1]>= self.hl[probability[0]]) else False)
        return len(total_true.to_array())/len(total_given.to_array())

    def likelihood(self,probability,observations):
        result = 1
        for entry in observations:
            result*=self.conditional_probability((entry,observations[entry]),probability)
        if probability[1] == 1:
            return self.likeliehood_const_t*result
        else:
            return self.likeliehood_const_f*result

    def classify(self,observations):
        _true = self.likelihood((self.dep_var,1),observations)
        _false = self.likelihood((self.dep_var,0),observations)
        if _true > _false:
            return (self.dep_var ,1)
        else:
            return (self.dep_var, 0)

