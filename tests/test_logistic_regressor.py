import matplotlib.pyplot as plt
import sys
sys.path.append('src')
from logistic_regressor import LogisticRegressor
from dataframe import DataFrame

df1 = DataFrame.from_array(
    [[1,0],
    [2,0],
    [3,0],
    [2,1],
    [3,1],
    [4,1]],
    columns = ['x', 'y'])
df2 = df1.copy()
reg = LogisticRegressor(df1, prediction_column='y',max_value = 1)

reg.set_coefficients({'constant': 0.5, 'x': 0.5})

alpha = 0.01
delta = 0.01
num_steps = 20000
reg.calc_gradient(alpha, delta, num_steps, debug_mode = False)
print('reg')
print(reg.multipliers)
coords = [[],[]]
for x in range(20):
    coords[0].append(x/100)
    coords[1].append(reg.predict({'constant':1,'x':x}))

plt.style.use('bmh')
plt.plot(coords[0],coords[1],linewidth=2.5)
plt.legend(['gradient_descent'])
plt.savefig('gradient_descent.png')
plt.close()



all_coords = []
for bounds in [(0.1,0.9),(0.01,0.99),(0.001,0.999),(0.0001,0.9999)]:
    df = DataFrame.from_array(df2.to_array(),df2.columns)
    regressor = LogisticRegressor(df, prediction_column = 'y', max_value = 1, zero_rep = bounds[0],max_rep = bounds[1])
    print(regressor.multipliers)
    coords = [[],[]]
    for x in range(20):
        coords[0].append(x/100)
        coords[1].append(regressor.predict({'constant':1,'x':x}))

    all_coords.append(coords)

plt.style.use('bmh')
for coords in all_coords:
    plt.plot(coords[0],coords[1],linewidth=2.5)
plt.legend(['0.1','0.01','0.001','0.0001'])
plt.savefig('logistic_regressor.png')
