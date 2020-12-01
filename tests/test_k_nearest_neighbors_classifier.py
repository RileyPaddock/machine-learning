import matplotlib.pyplot as plt
import sys
sys.path.append('src')
from k_nearest_neighbors_classifier import KNearestNeighborsClassifier
from dataframe import DataFrame

df = DataFrame.from_array(
    [['Shortbread'  ,     0.14     ,       0.14     ,      0.28     ,     0.44      ],
    ['Shortbread'  ,     0.10     ,       0.18     ,      0.28     ,     0.44      ],
    ['Shortbread'  ,     0.12     ,       0.10     ,      0.33     ,     0.45      ],
    ['Shortbread'  ,     0.10     ,       0.25     ,      0.25     ,     0.40      ],
    ['Sugar'       ,     0.00     ,       0.10     ,      0.40     ,     0.50      ],
    ['Sugar'       ,     0.00     ,       0.20     ,      0.40     ,     0.40      ],
    ['Sugar'       ,     0.10     ,       0.08     ,      0.35     ,     0.47      ],
    ['Sugar'       ,     0.00     ,       0.05     ,      0.30     ,     0.65      ],
    ['Fortune'     ,     0.20     ,       0.00     ,      0.40     ,     0.40      ],
    ['Fortune'     ,     0.25     ,       0.10     ,      0.30     ,     0.35      ],
    ['Fortune'     ,     0.22     ,       0.15     ,      0.50     ,     0.13      ],
    ['Fortune'     ,     0.15     ,       0.20     ,      0.35     ,     0.30      ],
    ['Fortune'     ,     0.22     ,       0.00     ,      0.40     ,     0.38      ]],

    columns = ['Cookie Type' ,'Portion Eggs','Portion Butter','Portion Sugar','Portion Flour' ]
    )
knn = KNearestNeighborsClassifier(3)
knn.fit(df, dependant_variable = 'Cookie Type')
observation = {
    'Portion Eggs': 0.10,
    'Portion Butter': 0.15,
    'Portion Sugar': 0.30,
    'Portion Flour': 0.45
}

print("\nTesting compute_distances:")
rounded = [[round(entry[0],3),entry[1]] for entry in knn.compute_distances(observation).to_array()] 
assert rounded == [[0.047, 'Shortbread'], [0.037, 'Shortbread'],
[0.062, 'Shortbread'],
[0.122, 'Shortbread'],
[0.158, 'Sugar'],
[0.158, 'Sugar'],
[0.088, 'Sugar'],
[0.245, 'Sugar'],
[0.212, 'Fortune'],
[0.187, 'Fortune'],
[0.396, 'Fortune'],
[0.173, 'Fortune'],
[0.228, 'Fortune']], 'Compute_distances_error'
print("     passed")

print("\nTesting nearest_neighbors:")
rounded = [[round(entry[0],3),entry[1]] for entry in knn.nearest_neighbors(observation).to_array()] 
assert rounded == [[0.037, 'Shortbread'],
 [0.047, 'Shortbread'],
 [0.062, 'Shortbread'],
 [0.088, 'Sugar'],
 [0.122, 'Shortbread'],
 [0.158, 'Sugar'],
 [0.158, 'Sugar'],
 [0.173, 'Fortune'],
 [0.187, 'Fortune'],
 [0.212, 'Fortune'],
 [0.228, 'Fortune'],
 [0.245, 'Sugar'],
 [0.396, 'Fortune']], 'nearest_neighbors error'
print("     passed")

print("\nTesting compute_average_distance:")
rounded = {category:round(knn.compute_average_distances(observation)[category],3) for category in knn.compute_average_distances(observation)}
assert rounded ==  {
    'Shortbread': 0.067,
    'Sugar': 0.162,
    'Fortune': 0.239
}, 'compute_avg_distances error'
print("     passed")


print("\nTesting classify:")
assert knn.classify(observation) == 'Shortbread', 'classify error'
print("     passed")



