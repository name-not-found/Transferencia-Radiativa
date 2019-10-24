#!/usr/bin/env python3

# radiative transfer equation
# Copyright (C) <2019>  Angelica Nayeli Rivas Bedolla (angelica.nayeli@comunidad.unam.mx)
#                       Pablo Clemente Moreno (clemnte@comunidad.unam.mx)
#                       Gilberto Carlos Domínguez Aguilar (gilberto.carlos@comuniadad.unam.mx)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
 para nuestros proyectos. buscar:
 que estudiar de radiacion
 funcion de opacidad
 sol : thompson
"""
#libraries
import math

#files
from funciones import tau, S

c = 3e10 #cm/s

N = 6.96e5
i0 = 0. # ergios*unidad de area*unidad de tiempo*unidad de longitud de onda*unidad de radian
dx = 1e5 # cm
nu = 1e8 # Hz
wl = c/nu # wave length

layers = range(1, int(N)+1)

i=i0
x = 0.
for _ in layers:
    x = float(_)*dx
    i = i*math.exp(-tau(dx, x, wl))+S(x, wl)*(1.-math.exp(-tau(dx, x, wl)))
    print(i)
