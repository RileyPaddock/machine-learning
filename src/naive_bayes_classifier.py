class NaiveBayesClassifier:
    def __init__(self, dataframe, dependent_variable):
        self.df = dataframe
        self.dep_var = dependent_variable

    def probability(self, column, identifier):
        return self.df.data_dict[column].count(identifier)/len(self.df.data_dict[column])

    def conditional_probability(self, probability, given):
        total_given = self.df.select_rows_where(lambda x: x[given[0]] == given[1])
        total_true = self.df.select_rows_where(lambda x: x[given[0]] == given[1] and x[probability[0]] == probability[1])
        return len(total_true.to_array())/len(total_given.to_array())

    def likelihood(self,probability,observations):
        result = 1
        for entry in observations:
            result*=self.conditional_probability((entry,observations[entry]),probability)
        return self.probability(probability[0],probability[1])*result

    def classify(self,observations):
        _true = self.likelihood((self.dep_var,True),observations)
        _false = self.likelihood((self.dep_var,False),observations)
        if _true > _false:
            return (self.dep_var ,True)
        else:
            return (self.dep_var, False)

