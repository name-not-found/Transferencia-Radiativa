from astropy.modeling.blackbody import blackbody_lambda

# Source function [erg/cm2 sec cm ster]
def S(x, wl):
	return blackbody_lambda(wl,  T(x))

# Temperature Model [K]
def T(x):
    return 5800.0

# Density model [cm-3]
def n(x):
	return 1.0

# opacity [cm-1]
def k(x):
    return 0.5*T(x)*n(x)

# adimensional - optical depth
def tau(dx, x):
	return (dx/2.0)*(k(x-dx)+k(x))
