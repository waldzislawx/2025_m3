import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ============== 1) LOAD HEAT-WAVE DATA ==============
heat_wave = pd.read_csv("birmingham_heatwave.csv", sep="\t", decimal=',')
print("Heat wave columns:", heat_wave.columns)

# Drop columns not needed
heat_wave = heat_wave.drop(['Temperature (°F)', 'Dew Point (°F)'], axis=1)

# Outdoor temp array [°C]
temp_out = heat_wave['Temperature (°C)'].to_numpy()
print("Outdoor temperature data:", temp_out)

# Each row = 1 hour
dt = 1.0  
n_times = len(temp_out)
time_array = np.arange(n_times)*dt

# ============== 2) PARAMETERS & HUMIDITY FUNCTION ==============
storey_height = 3.0
u_uninsulated = 2.0
u_insulated   = 0.18

# Specific heats [J/(kg·K)]:
Capacity_Dry    = 1.006e3       # ~1006 J/(kg·K)
Capacity_vapour = 1.9e3         # ~1900 J/(kg·K)

def capacity_moist(humidity):
    """
    Return the specific heat [J/(kg·K)] for air at given humidity fraction [0..1].
    0 => purely dry air (~1006 J/(kg·K)), 
    1 => purely water vapor (~1900 J/(kg·K)).
    """
    return (1 - humidity)*Capacity_Dry + humidity*Capacity_vapour

# For our simple approach, we'll use this function to get a *ratio* that 
# scales the building's "base capacity at 0% humidity" into 
# "actual capacity at the given humidity."
def humidity_scaling_factor(h):
    cp_dry   = capacity_moist(0.0)      # 1006 J/(kg·K)
    cp_moist = capacity_moist(h)       
    return cp_moist / cp_dry


# ============== 3) LOAD DWELLINGS DATA ==============
dwellings = pd.read_csv("dwellings.csv", sep='\t')
print("Dwellings columns:", dwellings.columns)

# ============== 4) HOME 1 ==============
storey_n   = int(dwellings['Home 1'].iloc[3])
floor_total= int(dwellings['Home 1'].iloc[5])
floor_A    = floor_total / storey_n
A          = 4*storey_height*storey_n + floor_A   # uninsulated logic
U          = u_uninsulated

# (a) Read the base capacity (kJ) at 0% humidity:
C_kJ_dry = float(dwellings['Home 1'].iloc[7])
# (b) Read the actual humidity fraction:
humidity1 = float(dwellings['Home 1'].iloc[8])  # e.g., 0.40 => 40% humidity
# (c) Scale that base capacity by the humidity ratio:
scale_1 = humidity_scaling_factor(humidity1)
C_kJ = C_kJ_dry * scale_1
# Convert to J:
C = C_kJ * 1000.0

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
plt.title('Home 1: Indoor vs. Outdoor Temperature (with humidity)')
plt.legend()
plt.grid(True)

# ============== HOME 2 ==============
storey_n   = int(dwellings['Home 2'].iloc[3])
floor_total= int(dwellings['Home 2'].iloc[5])
floor_A    = floor_total / storey_n
A          = 4*storey_height*storey_n + floor_A   # insulated
U          = u_insulated

C_kJ_dry = float(dwellings['Home 2'].iloc[7])
humidity2= float(dwellings['Home 2'].iloc[8])
scale_2  = humidity_scaling_factor(humidity2)
C_kJ     = C_kJ_dry * scale_2
C        = C_kJ * 1000.0

UA_over_C = (U*A)/C
T_in = np.zeros(n_times)
T_in[0] = temp_out[0]

for i in range(n_times - 1):
    dTdt      = UA_over_C*(temp_out[i] - T_in[i])
    T_in[i+1] = T_in[i] + dTdt*dt

plt.figure(figsize=(8,4))
plt.plot(time_array, temp_out, 'r--', label='Outdoor Temp')
plt.plot(time_array, T_in,     'b-',  label='Indoor Temp')
plt.xlabel('Time (hours)')
plt.ylabel('Temperature (°C)')
plt.title('Home 2: Indoor vs. Outdoor Temperature (with humidity)')
plt.legend()
plt.grid(True)

# ============== HOME 3 ==============
storey_n   = int(dwellings['Home 3'].iloc[3])
floor_total= int(dwellings['Home 3'].iloc[5])
floor_A    = floor_total / storey_n
A          = 4*storey_height*storey_n + floor_A
U          = u_insulated  # also insulated

C_kJ_dry = float(dwellings['Home 3'].iloc[7])
humidity3= float(dwellings['Home 3'].iloc[8])
scale_3  = humidity_scaling_factor(humidity3)
C_kJ     = C_kJ_dry * scale_3
C        = C_kJ * 1000.0

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
plt.title('Home 3: Indoor vs. Outdoor Temperature (with humidity)')
plt.legend()
plt.grid(True)

# ============== HOME 4 ==============
storey_n   = int(dwellings['Home 4'].iloc[3])
floor_total= int(dwellings['Home 4'].iloc[5])
floor_A    = floor_total / storey_n
A          = 2*storey_height*storey_n + floor_A   # uninsulated
U          = u_uninsulated

C_kJ_dry = float(dwellings['Home 4'].iloc[7])
humidity4= float(dwellings['Home 4'].iloc[8])
scale_4  = humidity_scaling_factor(humidity4)
C_kJ     = C_kJ_dry * scale_4
C        = C_kJ * 1000.0

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
plt.title('Home 4: Indoor vs. Outdoor Temperature (with humidity)')
plt.legend()
plt.grid(True)


# ============== SHOW ALL PLOTS ==============
plt.show()
