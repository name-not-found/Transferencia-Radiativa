from astropy.modeling.blackbody import blackbody_lambda
from scipy.interpolate import interp1d
import random
import numpy as np
# from astropy import units as u

kb  = 1.38e-16 # [ergK-1] 
c = 3e10 #cm/s

def inter(x,y):
    return interp1d(x,y)
    
def make_density_profile():
    """
    WATER PARAMETERS:
    0.9970479 g/cm3 at 25 °C [wikipedia]
    3.34e22 particles per gram (according to a molar mass of 
    18.01528 gmol-1 [Wikipedia])
    """
    mean = 3.34e22
    std = 1e2
    num_samples = 10000
    distance = np.linspace(0,2000000,num_samples)
    samples = np.random.normal(mean, std, size=num_samples)
    n = inter(distance, samples)
    
    return n

def make_temp_profile():
    """
    300 K or 26.85 Celsius
    """
    mean = 300
    std = 10
    num_samples = 10000
    samples = np.random.normal(mean, std, size=num_samples)
    distance = np.linspace(0,2000000, num_samples)
    t = inter(distance, samples)

    return t

t, n = make_temp_profile(), make_density_profile()
# Temperature Model [K]
# def T(x):
    # with open("T.dat", "r") as f: 
    #     T_dat = f.readlines()
    # z = []
    # Tr = []
    # for data in T_dat:
    #     if data[0] != '#':
    #         a,b = data.split()
    #         z.append(float(a))
    #         Tr.append(float(b))
    
    # f = interp1d(z,Tr)
    # return t(x)

# Density model [kg/m3] https://www.mentalfloss.com/article/49786/how-much-does-cloud-weigh
# def n(x):
    # with open("n.dat", "r") as f:
    #     n_dat = f.readlines()
    # z = []
    # nr = []
    # for data in n_dat:
    #     if data[0] != "#":
    #         a,b = data.split()
    #         z.append(float(a))
    #         nr.append(float(b))
    
    # f = interp1d(z,nr)
    # return n(x)                 
	
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


