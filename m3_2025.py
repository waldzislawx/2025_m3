import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

heat_wave = pd.read_csv("birmingham_heatwave.csv", sep="\t", decimal=',')
print(heat_wave.columns)
heat_wave = heat_wave.drop(['Temperature (°F)', 'Dew Point (°F)'], axis=1)
temp_out = heat_wave['Temperature (°C)'].to_numpy()
print(temp_out)

storey_height = 3
u_uninsulated = 2
u_insulated = 0.18

Capacity_Dry= 1.006 * 10**3
Capacity_vapour=  1.9 * 10**3
def Capacity_moist(humidity):
    capacity = (1-humidity)*Capacity_Dry + humidity*Capacity_vapour
    return capacity

Capacity_dry = 1.006 *1000

dwellings = pd.read_csv("dwellings.csv", sep='\t')
print(dwellings.columns)

#Dividing total area by number of number of stories
storey_n = int(dwellings['Home 1'].iloc[3])
floor_total= int(dwellings['Home 1'].iloc[5])
floor_A = floor_total / storey_n
A = 4 * storey_height * storey_n  + floor_A

#here put graph and integration

#Dividing total area by number of number of stories
storey_n = int(dwellings['Home 2'].iloc[3])
floor_total= int(dwellings['Home 2'].iloc[5])
floor_A = floor_total / storey_n
A = 4 * storey_height * storey_n  + floor_A

#here put graph and integration

#Dividing total area by number of number of stories
storey_n = int(dwellings['Home 3'].iloc[3])
floor_total= int(dwellings['Home 3'].iloc[5])
floor_A = floor_total / storey_n
A = 4 * storey_height * storey_n  + floor_A

#here put graph and integration

#Dividing total area by number of number of stories
storey_n = int(dwellings['Home 4'].iloc[3])
floor_total= int(dwellings['Home 4'].iloc[5])
floor_A = floor_total / storey_n
A = 4 * storey_height * storey_n  + floor_A

#here put graph and integration