Solving Radiative Transfer Equation to obtain clouds width.
===================================

## Abstract

The transfer of energy in the form of electromagnetic radiation is one of the most interesting phenomena. The fields of application are both diverse and useful. In this project we aim to solve the **radiative transfer equation to calculate clouds thikness** by means of numerical aproximation.

## Introduction

As a beam of energy travels space, it encounters several conditions which modify the radiance in several ways:

1. Absorption
2. Emission 
3. Scattering

Each one of these either increase (+) or decrease (-) the radiation. 
### Clouds 
In meteorology, a cloud is an aerosol consisting of a visible mass of minute liquid droplets, frozen crystals, or other particles suspended in the atmosphere of a planetary body or similar space. Water or various other chemicals may compose the droplets and crystals. On Earth, clouds are formed as a result of saturation of the air when it is cooled to its dew point, or when it gains sufficient moisture (usually in the form of water vapor) from an adjacent source to raise the dew point to the ambient temperature.<br>
For this modeling we consider the components of a cloud, basically clouds are composed of water particles. Tiny particles of water are densely packed and sunlight cannot penetrate far into the cloud before it is reflected out, giving a cloud its characteristic white color, especially when viewed from the top. Cloud droplets tend to scatter light efficiently, so that the intensity of the solar radiation decreases with depth into the gases. As a result, the cloud base can vary from a very light to very-dark-grey depending on the cloud's thickness and how much light is being reflected or transmitted back to the observer.

## Methodology

To solve this, we use the **radiative transfer equation**:

![Radiative transfer Eq](img/rte.gif)

Where: 
- ![Opacity F](img/Kv.gif) are the **absortions** or  the **opacity function** at wavelength **v**.

- ![emission](img/epsv.gif) are the **emissions** at wavelength **v**. 

 And it's solution:

 ![solution](img/sol.gif)

Where: 
- ![Source f](img/Source.gif) is the **Source Function**,

- ![tau](img/tau.gif) is the **optical depth**,

- ![Intensity](img/Iv.gif) is the **pecific intensity** at iteration **i**.


## Implementation

## Results

## References

[ref1] (http://www.met.reading.ac.uk/~ross/Science/RadTrans.pdf).<br>
[ref2] (https://en.wikipedia.org/wiki/Cloud).<br>
