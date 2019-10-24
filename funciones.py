# adimensional - optical depth
def tau(dx, x):
	return (dx/2.0)*(k(x-dx)+k(x))

# opacity [cm-1]
def k(x):
    return 0.5* T(x)

# Source function [erg/cm2 sec cm ster]
def S(x):
	return 1.* T(x)

def T(x):
    return 1.0
