import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

#all dimensions are in mm
r_chamber = 0.04     
L_chamber = 0.18    

# NOZZLE PARAMETERS

r_throat = 0.02      
r_exit   = 0.05      

L_conv = 0.05        
L_div  = 0.15        

# DISCRETIZATION

N = 100

# GEOMETRY CREATION

# Chamber (constant area)
x0 = np.linspace(0, L_chamber, N)
r0 = np.ones(N) * r_chamber

# Converging section
x1 = np.linspace(L_chamber, L_chamber + L_conv, N)
r1 = np.linspace(r_chamber, r_throat, N)

# Diverging section (smooth curve)
x2 = np.linspace(L_chamber + L_conv, L_chamber + L_conv + L_div, N)
r2 = r_throat + (r_exit - r_throat)*((x2 - (L_chamber + L_conv))/L_div)**1.5

# Combine all
x = np.concatenate([x0, x1, x2])
r = np.concatenate([r0, r1, r2])

# Area
A = np.pi * r**2
A_star = np.min(A)

# FLOW PROPERTIES

gamma = 1.4
T0 = 3000      # K, temperature in the combustion chamber
P0 = 3e6       # Pa, pressure in the combustion chamber
R = 287        # J/kgK, specific gas constant for air

# AREA-MACH FUNCTION

def area_mach(M, A_ratio):
    return (1/M)*((2/(gamma+1)*(1+(gamma-1)/2*M**2))**((gamma+1)/(2*(gamma-1)))) - A_ratio

# SOLVING MACH NUMBER

Mach = []

for Ai in A:
    A_ratio = Ai / A_star

    if Ai <= A_star:
        guess = 0.2   # subsonic 
    else:
        guess = 2.0   # supersonic

    M = fsolve(area_mach, guess, args=(A_ratio))[0]
    Mach.append(M)

Mach = np.array(Mach) # Mach number distribution along the nozzle

# THERMODYNAMIC PROPERTIES

T = T0 / (1 + (gamma-1)/2 * Mach**2)
P = P0 * (T/T0)**(gamma/(gamma-1))
rho = P / (R * T) # density at each section using ideal gas law
V = Mach * np.sqrt(gamma * R * T) # velocity at each section using Mach number and speed of sound

# MASS FLOW RATE

mdot = rho * A * V # mass flow rate at each section, should be constant along the nozzle

# THRUST CALCULATION

Pe = P[-1] # Exit pressure
Ve = V[-1] # Exit velocity
Ae = A[-1] # Exit area
Patm = 101325 # Atmospheric pressure

F = mdot[-1]*Ve + (Pe - Patm)*Ae # Thrust = momentum thrust + pressure thrust

print("Mass flow rate (kg/s):", mdot[-1])
print("Exit velocity (m/s):", Ve)
print("Thrust (N):", F)

# Plots for visualization of results
plt.figure()
plt.plot(x, r)
plt.title("Nozzle Geometry")
plt.xlabel("x (m)")
plt.ylabel("Radius (m)")
plt.grid()

plt.figure()
plt.plot(x, Mach)
plt.title("Mach Number Distribution")
plt.xlabel("x (m)")
plt.ylabel("Mach")
plt.grid()

plt.figure()
plt.plot(x, P)
plt.title("Pressure Distribution")
plt.xlabel("x (m)")
plt.ylabel("Pressure (Pa)")
plt.grid()

plt.figure()
plt.plot(x, T)
plt.title("Temperature Distribution")
plt.xlabel("x (m)")
plt.ylabel("Temperature (K)")
plt.grid()

plt.show()