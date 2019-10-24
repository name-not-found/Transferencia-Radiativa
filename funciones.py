from astropy.modeling.blackbody import blackbody_lambda
kb  = 1.38e-16 # [ergK-1]
c = 3e10 #cm/s
# Source function [erg/cm2 sec cm ster]
def S(x, wl):
	return blackbody_lambda(wl,  T(x))

# Temperature Model [K]
def T(x):
    return 1e6

# Density model [cm-3]
def n(x):
	return 1e7

# opacity [cm-1]
def k(x, wl):
    # REF Dulk (1985) eq. 21
    nu = c/wl
    return 0.2 * pow(n(x),2) * pow(T(x),-3/2) * pow(nu ,-2)

# adimensional - optical depth
def tau(dx, x, wl):
	return (dx/2.0)*(k(x-dx, wl)+k(x, wl))

def rayleigh(I, wl):
	return I.value * pow(wl, 4)/ (2.0*c*kb)