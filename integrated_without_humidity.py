import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#load heatwave data

heat_wave = pd.read_csv("birmingham_heatwave.csv", sep="\t", decimal=',')
print("Heat wave columns:", heat_wave.columns)

#clean
heat_wave = heat_wave.drop(['Temperature (°F)', 'Dew Point (°F)'], axis=1)

# get outdoor temp
temp_out = heat_wave['Temperature (°C)'].to_numpy()
print("Outdoor temperature data:", temp_out)

# each row = 1 hour
dt = 1.0  # [hours]
n_times = len(temp_out)
time_array = np.arange(n_times)*dt

#parameters and functions
storey_height = 3.0
u_uninsulated = 2.0
u_insulated   = 0.18

#dwellings data
dwellings = pd.read_csv("dwellings.csv", sep='\t')
print("Dwellings columns:", dwellings.columns)


# GEOMETRY, CAPACITY, EULER, PLOT

# ------------------- HOME 1 -------------------
storey_n   = int(dwellings['Home 1'].iloc[3])
floor_total= int(dwellings['Home 1'].iloc[5])
floor_A    = floor_total / storey_n
A          = 4*storey_height*storey_n + floor_A   # uninsulated logic
U          = u_uninsulated

# Convert kJ -> J
C_kJ = float(dwellings['Home 1'].iloc[7])
C    = C_kJ * 1000.0

UA_over_C = (U*A)/C

T_in = np.zeros(n_times)
T_in[0] = temp_out[0]

for i in range(n_times - 1):
    dTdt = UA_over_C*(temp_out[i] - T_in[i])
    T_in[i+1] = T_in[i] + dTdt*dt

plt.figure(figsize=(8,4))
plt.plot(time_array, temp_out, 'r--', label='Outdoor Temp')
plt.plot(time_array, T_in,     'b-',  label='Indoor Temp')
plt.xlabel('Time (hours)')
plt.ylabel('Temperature (°C)')
plt.title('Home 1: Indoor vs. Outdoor Temperature')
plt.legend()
plt.grid(True)


# ------------------- HOME 2 -------------------
storey_n   = int(dwellings['Home 2'].iloc[3])
floor_total= int(dwellings['Home 2'].iloc[5])
floor_A    = floor_total / storey_n
A          = 4*storey_height*storey_n + floor_A   # insulated logic
U          = u_insulated

# Convert kJ -> J
C_kJ = float(dwellings['Home 2'].iloc[7])
C    = C_kJ * 1000.0

UA_over_C = (U*A)/C

T_in = np.zeros(n_times)
T_in[0] = temp_out[0]

for i in range(n_times - 1):
    dTdt = UA_over_C*(temp_out[i] - T_in[i])
    T_in[i+1] = T_in[i] + dTdt*dt

plt.figure(figsize=(8,4))
plt.plot(time_array, temp_out, 'r--', label='Outdoor Temp')
plt.plot(time_array, T_in,     'b-',  label='Indoor Temp')
plt.xlabel('Time (hours)')
plt.ylabel('Temperature (°C)')
plt.title('Home 2: Indoor vs. Outdoor Temperature')
plt.legend()
plt.grid(True)


# ------------------- HOME 3 -------------------
storey_n   = int(dwellings['Home 3'].iloc[3])
floor_total= int(dwellings['Home 3'].iloc[5])
floor_A    = floor_total / storey_n
A          = 4*storey_height*storey_n + floor_A
U          = u_insulated  # also insulated

C_kJ = float(dwellings['Home 3'].iloc[7])
C    = C_kJ * 1000.0

UA_over_C = (U*A)/C

T_in = np.zeros(n_times)
T_in[0] = temp_out[0]

for i in range(n_times - 1):
    dTdt = UA_over_C*(temp_out[i] - T_in[i])
    T_in[i+1] = T_in[i] + dTdt*dt

plt.figure(figsize=(8,4))
plt.plot(time_array, temp_out, 'r--', label='Outdoor Temp')
plt.plot(time_array, T_in,     'b-',  label='Indoor Temp')
plt.xlabel('Time (hours)')
plt.ylabel('Temperature (°C)')
plt.title('Home 3: Indoor vs. Outdoor Temperature')
plt.legend()
plt.grid(True)


# ------------------- HOME 4 -------------------
storey_n   = int(dwellings['Home 4'].iloc[3])
floor_total= int(dwellings['Home 4'].iloc[5])
floor_A    = floor_total / storey_n
A          = 2*storey_height*storey_n + floor_A   # different logic
U          = u_uninsulated

C_kJ = float(dwellings['Home 4'].iloc[7])
C    = C_kJ * 1000.0

UA_over_C = (U*A)/C

T_in = np.zeros(n_times)
T_in[0] = temp_out[0]

for i in range(n_times - 1):
    dTdt = UA_over_C*(temp_out[i] - T_in[i])
    T_in[i+1] = T_in[i] + dTdt*dt

plt.figure(figsize=(8,4))
plt.plot(time_array, temp_out, 'r--', label='Outdoor Temp')
plt.plot(time_array, T_in,     'b-',  label='Indoor Temp')
plt.xlabel('Time (hours)')
plt.ylabel('Temperature (°C)')
plt.title('Home 4: Indoor vs. Outdoor Temperature')
plt.legend()
plt.grid(True)


# SHOW ALL PLOTS
plt.show()
