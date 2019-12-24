# WINO

Authors: [Hryts](https://github.com/Hryts), [ch0c01ate](https://github.com/ch0c01ate), [yankur](https://github.com/yankur)



## Description:

**Wino** project is a solution to problems which people usually come up with during the wine creation. It is device with embeded hardware called to provide an ability to observe and control fermentation process. 

With it you can see such **parameters** as:

- Brix °Bx (amount of sugar per 100 g of solution)
- Carbon dioxide concentration (which tells you about dynamic of process)
- Temperature (important factor on which yeasts ability to live depends)



## What is done:

- Many different approaches checked
- Components found, filtered and ordered
- Computations provided

 

## Previous decisions:

To be done



## Final decision:

To measure the °Bx the refractive method was chosen. Total internal reflection is to be used to find the refractive index of a wine (which depends on brix since sugar is optically active). We are going to use optical prism with relatively high refractive index to make total internal reflection angle bigger.



## Computations:

To be done



## Components:

- [Camera](https://www.sparkfun.com/products/15430)  ([datasheet](https://cdn.sparkfun.com/assets/0/b/0/e/d/LI-IMX219-MIPI-FF-NANO_SPEC.pdf))
- Optical prism 
- Led
- [Temperature sensor ](https://www.sparkfun.com/products/11050)([datasheet](https://cdn.sparkfun.com/datasheets/Sensors/Temp/DS18B20.pdf))
- [CO<sub>2</sub> sensor](https://www.youtube.com/watch?v=q86g1aop6a8) ([datasheet](https://www.youtube.com/watch?v=q86g1aop6a8))
