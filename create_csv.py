import pandas as pd
import numpy as np

df = pd.DataFrame()
df['Date'] = pd.date_range(start='1/1/2020', end='1/1/2025')

# Good daily estimate
mu, sigma = 0.0003, 0.01 
s = np.random.normal(mu, sigma, len(df))
df['Returns'] = s

df.to_csv('example.csv', index=False)
