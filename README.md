Solving Radiative Transfer Equation to obtain cloud's width.
===================================

## Abstract

The transfer of energy in the form of electromagnetic radiation is one of the most interesting phenomena. The fields of application are both diverse and useful. In this project we aim to solve the **radiative transfer equation to calculate clouds thickness** by means of numerical aproximation.

## Introduction

As a beam of energy travels space, it encounters several conditions which modify the radiance in several ways:

1. Absorption
2. Emission 
3. Scattering

Each one of these either increase (+) or decrease (-) the radiation. 
### Clouds 
In meteorology, a cloud is an aerosol consisting of a visible mass of diminutive liquid droplets, frozen crystals, or other particles suspended in the atmosphere of a planetary body or similar space. Water or various other chemicals compose the droplets and crystals. On Earth, clouds are formed as a result of saturation in the air when it is cooled to its dew point, or when it gains sufficient moisture (usually in the form of water vapor) from an adjacent source to raise the dew point to ambient temperature.<br>
For this modeling we consider the components of a cloud, basically clouds are composed of water particles. Tiny particles of water that are densely packed and sunlight cannot penetrate far into the cloud before it is reflected out, giving a cloud its characteristic white color, especially when viewed from the top. Cloud droplets tend to scatter light efficiently, so that the intensity of the solar radiation decreases according to the gases' depth. As a result, a cloud's base can vary from a very light to very-dark-grey depending on the cloud's thickness and how much light is being reflected or transmitted back to the observer.

## Methodology

To perform this task, we used the **radiative transfer equation** define as:

![Radiative transfer Eq](img/rte.gif)

Where: 
- ![Opacity F](img/Kv.gif) are the **absortions** or  the **opacity function** at wavelength **v**.

- ![emission](img/epsv.gif) are the **emissions** at wavelength **v**. 

 And its solution:

 ![solution](img/sol.gif)

Where: 
- ![Source f](img/Source.gif) is the **Source Function**.

- ![tau](img/tau.gif) is the **optical depth**.

- ![Intensity](img/Iv.gif) is the **specific intensity** at iteration **i**.
In this project, we aim to calculate the thickness of a water cloud by comparing the light that enters with the light that comes out of the cloud.
With this we can measure other things like water density and thus other properties that can be of potential interest to metheorological forecasting and the aerospace industry.  

### **Initial contidions:**

We started our simulation with the emission of a black-body-like object such as the Sun and calculate the initial emition

- ![I 0](img/I0.gif)


Obtained from **astropy.modeling.blackbody.blackbody_lambda**
with 4760 angstrom and 5700 K as parameters.

We solved the equation for the whole visible spectrum, but for simplicity we used the color cyan; we can locate cyan at the given wavelength 4760 Angstrom or 629'816'088'235'294 Hz.

#### **Water and the ES**
As we know, water is transparent, wich means water interactions with light are minimal in the visible spectrum; however these are the interactions we are looking for, in particular, how water interacts in liquid, gas and solid states at the given wavelength. 

For simplicity, we supposed that clouds do not emit, Source function is constant and **0** therefore the right side of the equation was removed. So the only things we have considered were the absorptions at the given wavelength. 



## Implementation

We used code writen in pure Python. Python is simple and easy to read wich makes it apropriate for this task.
The code is divided in several components:

- main.py
- funciones.py
- the data

The main module accounts for the calls to functions, defining global parameters (such as the light speed and Boltzman constant) needed for calculations and of course the main loop in wich we integrate the solution. 

The funciones.py module defines the components needed to solve the **RTE** and additional functionality such as data reading.



## Results

We show the following figure:

![result](img/res.png)

As we can see, the model works to a point; we can now see how **light would be absorbed** by the cloud starting on the top. 

We used a high-density water cloud (the absoption cooeficcient is constant). 

The model tends to 0 without limit because we have not yet programmed a system wich can diferentiate the limit of the cloud. Thus, we cannot compare the **output specific intensity** 
and cloud thickness.

## References

- [ref1] Bannister, R. (2007). The Radiative Transfer Equation. [ebook] Available at: http://www.met.reading.ac.uk/~ross/Science/RadTrans.pdf [Accessed 29 Nov. 2019].<br>
- [ref2] En.wikipedia.org. (2019). Cloud. [online] Available at: https://en.wikipedia.org/wiki/Cloud [Accessed 29 Nov. 2019].<br>
- [ref3] Chaplin, M. (2019). Water absorption spectrum. [online] Www1.lsbu.ac.uk. Available at: http://www1.lsbu.ac.uk/water/water_vibrational_spectrum.html [Accessed 29 Nov. 2019].<br>
- [ref4] Rouan D. (2011) Radiative Transfer. In: Gargaud M. et al. (eds) Encyclopedia of Astrobiology. Springer, Berlin, Heidelberg.<br>
- [ref5] De la Luz, V., Lara, A., Mendoza, E. and Shimojo, M. (2008). 3D Simulations of the Quiet Sun Radio Emission at Millimeter and Submillimeter Wavelengths. [ebook] Available at: http://www.scielo.org.mx/pdf/geoint/v47n3/v47n3a11.pdf [Accessed 29 Nov. 2019].
