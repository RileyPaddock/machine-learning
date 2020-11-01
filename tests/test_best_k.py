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
['Sugar'       ,     0.02     ,       0.08     ,      0.45     ,     0.45      ],
['Sugar'       ,     0.10     ,       0.15     ,      0.35     ,     0.40      ],
['Sugar'       ,     0.10     ,       0.08     ,      0.35     ,     0.47      ],
['Sugar'       ,     0.00     ,       0.05     ,      0.30     ,     0.65      ],
['Fortune'     ,     0.20     ,       0.00     ,      0.40     ,     0.40      ],
['Fortune'     ,     0.25     ,       0.10     ,      0.30     ,     0.35      ],
['Fortune'     ,     0.22     ,       0.15     ,      0.50     ,     0.13      ],
['Fortune'     ,     0.15     ,       0.20     ,      0.35     ,     0.30      ],
['Fortune'     ,     0.22     ,       0.00     ,      0.40     ,     0.38      ],
['Shortbread'  ,     0.05     ,       0.12     ,      0.28     ,     0.55      ],
['Shortbread'  ,     0.14     ,       0.27     ,      0.31     ,     0.28      ],
['Shortbread'  ,     0.15     ,       0.23     ,      0.30     ,     0.32      ],
['Shortbread'  ,     0.20     ,       0.10     ,      0.30     ,     0.40      ]],

    columns = ['Cookie Type' ,'Portion Eggs','Portion Butter','Portion Sugar','Portion Flour' ]
    )
knn = KNearestNeighborsClassifier(df, prediction_column = 'Cookie Type')
plot_data = []
num_k = len(knn.data.to_array())
arr = []

for k in range(1,num_k):
    correct_observations = 0
    print('Testing k = '+str(k))
    for i in range(len(knn.data.to_array())):
        correct = knn.data.to_array()[i][0]
        observation = {column:knn.data.data_dict[column][i] for column in knn.data.columns if column != 'Cookie Type'}
        copy = knn.data.to_array()
        del copy[i]
        df1 = DataFrame.from_array(copy, columns = knn.data.columns)
        knn2 = KNearestNeighborsClassifier(df1, prediction_column = 'Cookie Type')
        if knn2.classify(observation, k = k) == correct:
            correct_observations += 1
    arr.append(correct_observations/len(knn.data.to_array()))




plt.plot([x for x in range(1,num_k)],arr,linewidth = 0.75)
plt.xlabel('k')
plt.ylabel('accuracy')
plt.title('Best size k')
plt.savefig('K_nearest.png')
