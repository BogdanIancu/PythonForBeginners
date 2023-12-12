import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

movie_data = pd.read_csv("data.csv")
print(movie_data.info)
print(movie_data.describe())

movie_data = pd.read_csv("data.csv")
ages = movie_data['age']

mean_age = np.mean(ages)
std_age = np.std(ages)
plt.hist(ages, bins=10, edgecolor='black', color='blue', density=True, alpha=0.7)
x = np.linspace(min(ages), max(ages), 100)
y = norm.pdf(x, mean_age, std_age)
plt.plot(x, y, 'r--', label='Gaussian Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Distribution of Ages with Gaussian Distribution')
plt.legend()
plt.show()

movie_data = pd.read_csv("data.csv")
cleared_data = movie_data[movie_data['IMDB_rating'] >= 6.5]

cleared_data.to_csv('cleared_data.csv', index=False)



