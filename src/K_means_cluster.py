import matplotlib.pyplot as plt
import random
class KMeans:
    def __init__(self, k, data):
        self.clusters = {i:[j for j in range(len(data)) if j%i == 0] for i in range(1,k+1)}
        self.data = data
        self.data_columns = {i:[data[x][i] for x in range(len(data))] for i in range(len(data[0]))}
        self.centers = self.calc_averages()

    def calc_averages(self):
        averages = {key:0 for key in self.clusters}
        for key in self.clusters:
            temp = [[] for _ in range(len(self.data[0]))]
            for i in self.clusters[key]:
                for x in range(len(temp)):
                    temp[x].append(self.data[i][x])

            averages[key] = [sum(vals)/len(vals) for vals in temp]
        return averages

    def calc_euclidian_distance(self, p1, p2):
        return sum([(p1[i] - p2[i])**2 for i in range(len(p1))])**0.5

    def update_clusters_once(self):
        clusters = {key:[] for key in self.clusters}
        for i in range(len(self.data)):
            closest_center = self.get_closest_center(i)
            clusters[closest_center].append(i)
        self.clusters = clusters

    def get_closest_center(self, i):
        distances = []
        for key in self.centers:
            distances.append(self.calc_euclidian_distance(self.data[i], self.centers[key]))
        return distances.index(min(distances))+1
        

    def run(self):
        while True:
            old_centers = self.centers.copy()
            self.update_clusters_once()
            self.centers = self.calc_averages()
            if self.centers == old_centers:
                break
    
    def elbow_calcs(self):
        distance = 0
        for i in range(len(self.data)):
            for j in self.clusters:
                if i in self.clusters[j]:
                    distance += self.calc_euclidian_distance(self.centers[j],self.data[i])
        return distance







data = [[0.14, 0.14, 0.28, 0.44],
        [0.22, 0.1, 0.45, 0.33],
        [0.1, 0.19, 0.25, 0.4],
        [0.02, 0.08, 0.43, 0.45],
        [0.16, 0.08, 0.35, 0.3],
        [0.14, 0.17, 0.31, 0.38],
        [0.05, 0.14, 0.35, 0.5],
        [0.1, 0.21, 0.28, 0.44],
        [0.04, 0.08, 0.35, 0.47],
        [0.11, 0.13, 0.28, 0.45],
        [0.0, 0.07, 0.34, 0.65],
        [0.2, 0.05, 0.4, 0.37],
        [0.12, 0.15, 0.33, 0.45],
        [0.25, 0.1, 0.3, 0.35],
        [0.0, 0.1, 0.4, 0.5],
        [0.15, 0.2, 0.3, 0.37],
        [0.0, 0.13, 0.4, 0.49],
        [0.22, 0.07, 0.4, 0.38],
        [0.2, 0.18, 0.3, 0.4]]

x_coords = [x for x in range(1,6)]
y_coords = []
for k in [x for x in range(1,6)]:
    k_means = KMeans(k, data)
    k_means.run()
    y_coords.append(k_means.elbow_calcs())

plt.plot(x_coords, y_coords)
plt.xlabel('k')
plt.ylabel('sum_squared_error')
plt.title('Best size k')
plt.savefig('Elbow_Method.png')