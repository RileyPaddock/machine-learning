from src.cartesian_product import cartesian_product
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

    def grid_search(self,ranges):
        points = cartesian_product(ranges)
        self.minimum = points[0]
        for coordinates in points:
            if self.f(*coordinates) < self.f(*self.minimum):
                self.minimum = coordinates
        return self.minimum

    def compute_gradient(self, delta=0.01):
        return self.f_partials(self.minimum, delta)
