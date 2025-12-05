import math 
import numpy as np 
import matplotlib.pyplot as plt

# calculations and equations are written with unit as cm in mind
p_led = 1.6e-3
L = 10      # path length
T = 210     # temp in kelvin 
R = 0.16    # typical responsitvity of photodiode [TAKE FROM SG01XL-BC5]
area = 0.283       # area of photodiode [TAKEN FROM ISO]
theta = math.radians(1)     # half angle divergence of LED = 1 degree (to ensure tight beam)
w = L * np.tan(theta)       # calculate the beam radius at the photodiode
irradiance = 2*p_led /(math.pi * w**2)       # considering guassian beam (assumed flat beam between LED and PD)
power = irradiance  * area
sigma = 1.13 * 1e-16  # absorption cross section of ozone in cm^2/molecule
ppbv = np.arange(0.001,100,1)
N_O3 = ppbv * 1e-15 * 600 / (1.380649 * 10**(-23)*T)    # molecules per cm^3, pressure = 600 pascals
N = N_O3 * L
I_base = R * power      # base current 
transmittance = np.exp(-sigma * N)
absorption = 1 - transmittance
delta_I = I_base * (absorption)


print(delta_I)
print(area, w**2)
plt.plot(ppbv,delta_I)
print(I_base)
plt.xlabel('O3 concentration (ppbv)')
plt.ylabel('delta photocurrent (A)')
plt.title(' delta photocurrent vs O3 concentration at different temperatures')
plt.grid(1)
plt.show()
