class NaiveBayesClassifier:
    def __init__(self, dataframe, dependent_variable):
        self.df = dataframe
        self.dep_var = dependent_variable

    def probability(self, column, identifier):
        return sum([1 for entry in self.df.data_dict[column] if entry == identifier])/len(self.df.data_dict[column])

    def conditional_probability(self,probability, given):
        total = count = 0
        arr = self.df.to_array()
        p_i = self.df.columns.index(probability[0])
        g_i = self.df.columns.index(given[0])
        for i in range(len(arr)):
            if arr[i][g_i] == given[1]:
                total += 1
                if arr[i][p_i] == probability[1]:
                    count += 1
        return count/total

    def likelihood(self,probability,observations):
        result = 1
        for entry in observations:
            result*=self.conditional_probability((entry,observations[entry]),probability)
        return self.probability(probability[0],probability[1])*result

    def classify(self,observations):
        _true = self.likelihood((self.dep_var,True),observations)
        _false = self.likelihood((self.dep_var,False),observations)
        if _true > _false:
            return self.dep_var + "_True"
        else:
            return self.dep_var + "_False"

