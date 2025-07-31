import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df['Salary'].plot(kind='hist')

plt.show()