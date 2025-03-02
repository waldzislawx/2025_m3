import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# the poorer the region the higher the index
# the higher the environamental index the higher need (less trees, natural cooling)
# the more old people the higher

resid_data = pd.read_csv("residents1.csv", decimal=',', sep='\t')

regs = resid_data['Constituency']
resid_data['Population under 15'] = resid_data['Population under 15'] / resid_data['Total population']  
resid_data['Population 65 and over'] = resid_data['Population 65 and over'] / resid_data['Total population']  

print(resid_data.columns)

scaler = StandardScaler()

for column in resid_data.columns[1:]:
    print(resid_data[column])

    resid_data[column] = scaler.fit_transform(resid_data[column].to_numpy().reshape(-1, 1))

print(resid_data)
resid_data['Average annual income of employed residents in British pounds'] = -1 * resid_data['Average annual income of employed residents in British pounds']
vars = resid_data.drop(["Constituency", 'Total population'], axis=1).to_numpy()

#vars['Average annual income of employed residents in British pounds'] = -1 * vars['Average annual income of employed residents in British pounds']


index = vars.sum(axis=1)

for i in range(len(index)):
    print(i, " ", resid_data["Constituency"].iloc[i], " ", index[i])