import math

absorption_cross = 1.1329 * 1e-17  # in cm^2/molecule   
T = float(input("temp: "))
ppbv = float(input("ppbv: "))
n = ppbv * 1e-15 * 600 / (1.380649 * 10**(-23)*T)  # molecules per cm^3
tau = n * absorption_cross * 10
R = 0.16
Pout = float(input("enter the led pout: "))
iph = R * Pout * 1e-3 * math.exp(-tau)
print(iph)
print(0.00016-iph)
inew = iph - 1e-10
tau_new = -1 * math.log(inew / (R * Pout * 1e-3))
print(tau_new)
n_new = tau_new / (absorption_cross * 10)
print(n_new)
ppbv_new = n_new * (1.380649 * 10**(-23)*T) / (600 * 1e-15)
print(ppbv_new)