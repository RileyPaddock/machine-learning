class GradientDescent():
    def __init__(self, f):
        self.f = f
        self.num_variables = self.f.__code__.co_argcount
        self.minimum = [0 for i in range(self.num_variables)]

    def f_partials(self, position, delta=0.001):
        partials = []
        for i in range(len(position)):
            forward = [position[i] for i in range(len(position))]
            backward = [position[i] for i in range(len(position))]
            forward[i] += delta
            backward[i] -= delta
            partials.append((self.f(*forward) - self.f(*backward)) / (2 * delta))
        return partials

    def descend(self, scaling_factor=0.001, delta=0.01, num_steps=1, logging=False):
        for _ in range(num_steps):
            partials = self.f_partials(self.minimum, delta)
            for j in range(len(self.minimum)):
                self.minimum[j] = self.minimum[j] - (scaling_factor * partials[j])
            if logging:
                print(self.minimum)

    def grid_search(self, ranges):
        completion_check = False
        output = [ranges[i][0] for i in range(len(ranges))]
        min_check = [0 for i in range(len(ranges))]
        num_of_bounds = [len(elem) for elem in ranges]
        while not completion_check:
            smallest_check = 0
            for i in range(len(ranges)):
                if num_of_bounds[i] == min_check[i]:
                    smallest_check += 1
            if smallest_check == len(ranges):
                completion_check = True
            if self.f(*output) < self.f(*self.minimum):
                for i in range(len(ranges)):
                    self.minimum[i] = output[i]
            i = 0
            change = True
            while change and i < len(ranges):
                if min_check[i] + 1 > num_of_bounds[i]:
                    min_check[i] = 0
                    output[i] = ranges[i][0]
                    change = True
                else:
                    min_check[i] += 1
                    output[i] = ranges[i][min_check[i] - 1]
                    change = False
                i += 1
        return self.minimum

    def compute_gradient(self, delta=0.01):
        return self.f_partials(self.minimum, delta)
