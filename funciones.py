from astropy.modeling.blackbody import blackbody_lambda
from scipy.interpolate import interp1d
# from astropy import units as u

kb  = 1.38e-16 # [ergK-1] 
c = 3e10 #cm/s

# Temperature Model [K]
def T(x):
    with open("T.dat", "r") as f:
        T_dat = f.readlines()
    z = []
    Tr = []
    for data in T_dat:
        if data[0] != '#':
            a,b = data.split()
            z.append(float(a))
            Tr.append(float(b))
    
    f = interp1d(z,Tr)
    return f(x)

# Density model [cm-3]
def n(x):
    with open("n.dat", "r") as f:
        n_dat = f.readlines()
    z = []
    nr = []
    for data in n_dat:
        if data[0] != "#":
            a,b = data.split()
            z.append(float(a))
            nr.append(float(b))
    
    f = interp1d(z,nr)
    return f(x)
	
# Source function [erg/cm2 sec cm ster]
def S(x, wl):
	# return blackbody_lambda(wl*1e8,  T(x)) * 1e8 # A-1 to cm-1
	return blackbody_lambda(wl*1e8,  T(x)) # A-1 to cm-1

# opacity [cm-1]
def k(x, wl):
    # REF Dulk (1985) eq. 21
    # 0.8 - 12.5 mu []
    nu = c/wl
    return 1e5 * 0.2 * pow(n(x),2) * pow(T(x),-3/2) * pow(nu ,-2)
    # return 0.8
# adimensional - optical depth
def tau(dx, x, wl):
	return (dx/2.0)*(k(x-dx, wl)+k(x, wl))

def rayleigh(I, wl):
	return I.value * pow(wl, 4)/ (2.0*c*kb)