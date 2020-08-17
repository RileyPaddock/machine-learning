import matplotlib.pyplot as plt
plt.style.use('bmh')
import sys
sys.path.append('analysis')
from logistic_regression import Logistic_Regressor
data = [(0, 0.01), (0, 0.01), (0, 0.05), (10, 0.02), (10, 0.15), (50, 0.12), (50, 0.28), (73, 0.03), (80, 0.10), (115, 0.06), (150, 0.12), (170, 0.30), (175, 0.24), (198, 0.26), (212, 0.25), (232, 0.32), (240, 0.45), (381, 0.93), (390, 0.87), (402, 0.95), (450, 0.98), (450, 0.85), (450, 0.95), (460, 0.91), (500, 0.95)]

lr = Logistic_Regressor(data)

print("coefficients:")
print(lr.solve_coefficients())
print("probability of beating a player with 300 hours:")
decimal = lr.evaluate(lr.solve_coefficients(),300)
print("\n   "+str(round(decimal, 3)))


x_coords = range(750)
win_chances = []
for time_played in range(750):
    win_chances.append(lr.evaluate(lr.
    solve_coefficients(),time_played))
plt.plot(x_coords,win_chances,linewidth = 0.75)
plt.legend(['Chance of beating average player'])
plt.xlabel('Hours Played')
plt.ylabel('Percent Chance of beating average player')
plt.title('Chance of beating average player based on time played.')
plt.show()