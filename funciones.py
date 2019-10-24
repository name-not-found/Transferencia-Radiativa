# adimensional - optical depth
def tau(dx, x):
	return (dx/2.0)*(k(x-dx)+k(x))

# opacity [cm-1]
def k(x):
    return 0.5* x

# Source function [erg/cm2 sec cm ster]
def S(x):
	return 1.* x
