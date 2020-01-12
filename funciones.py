from astropy.modeling.blackbody import blackbody_lambda
from scipy.interpolate import interp1d
import random
import numpy as np
# from astropy import units as u

kb  = 1.38e-16 # [ergK-1] 
c = 3e10 #cm/s

def inter(x,y):
    return interp1d(x,y)
# Density Model [particles per gram]    
def make_density_profile():
    """
    WATER DENSITY PARAMETERS:
    0.9970479 g/cm3 at 25 °C [wikipedia]
    3.34e22 particles per gram (according to a molar mass of 
    18.01528 gmol-1 [Wikipedia]) 
    """
    
    mean = 3.34e22
    std = 1e2
    num_samples = 10000
    densities = np.random.normal(mean, std, size=num_samples)
    
    # distance is in cm,
    # sizes are:
    # sample cloud is 100m thick (10'000 cm)
    distance = np.linspace(0, 2e4, num_samples) # from 0 to N*dx
    n = inter(distance, densities)
    
    return n

def make_temp_profile():
    """
    WATER TEMPERATURE PARAMETERS:
    300 K or 26.85 Celsius
    """
     
    mean = 300 
    std = 10
    num_samples = 10000
    temps = np.random.normal(mean, std, num_samples)
    
    # distance is in cm,
    # sizes are:
    # sample cloud is 100m thick (10'000 cm)
    distance = np.linspace(0, 2e4, num_samples)
    t = inter(distance, temps)

    return t

t, n = make_temp_profile(), make_density_profile()

# Source function [erg/cm2 sec cm ster]
def S(x, wl):
	# return blackbody_lambda(wl*1e8,  T(x)) * 1e8 # A-1 to cm-1
	# return blackbody_lambda(wl*1e8,  T(x)) # A-1 to cm-1
    return 0

# opacity [cm-1]
def k(x, wl):
    nu = c/wl
    theta = 300./t(x)
    # theta = 1
    #P = 0.0005*kb*300
    P = n(x)*kb*t(x)
    C = 7.9e-6
    return (pow(nu, -2) * theta * P) / C
    
# adimensional - optical depth
def tau(dx, x, wl):
	return (dx/2.0)*(k(x-dx, wl)+k(x, wl))

def rayleigh(I, wl):
	#return I.value * pow(wl, 4)/ (2.0*c*kb)
	return I * pow(wl, 4)/ (2.0*c*kb)


