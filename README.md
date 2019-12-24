**Wino** project is a solution to problems which people usually come up with during the wine creation. It is device with embeded hardware called to provide an ability to observe and control fermentation process. 



## Features:

With our device you can see such **parameters** as:
With it you can see such **parameters** as:

- Brix °Bx (amount of sugar per 100 g of solution)
- Gas preassure (which tells you about dynamic of process)
- Carbon dioxide concentration (which tells you about dynamic of process)
- Temperature (important factor on which yeasts ability to live depends)


@@ -31,24 +27,24 @@ With our device you can see such **parameters** as:
## Previous decisions:

- Density Method
  You can check [Density measuring method](https://github.com/ch0c01ate/wino/blob/master/presentations/Measuring%20Density.ppt) to discover more about it.


  You can check [Density measuring method by Cypress](https://github.com/ch0c01ate/wino/blob/master/presentations/Measuring%20Density.ppt) to discover more about it.

- Optical Method

  Check [Optical method](https://github.com/ch0c01ate/wino/blob/master/presentations/Optical%20Method.pptx) to discover how it works. This method was rejected because of turbidity of the wine.




## Final decision:

Refractive method of the °Bx measurement the  was chosen. With help of camera we are going to get data about total internal reflection angle which depends on refractive indexes of a wine (which depends on brix since sugar is optically active). To make the angle big enough to measure it, we will use prism made of optical glass with refractive angle ~1.52.
To measure the °Bx the refractive method was chosen. Total internal reflection is to be used to find the refractive index of a wine (which depends on brix since sugar is optically active). We are going to use optical prism with relatively high refractive index to make total internal reflection angle bigger.



## Computations:

All computations related to light refraction provided in **calculation.py** file.
To be done



@@ -58,4 +54,4 @@ All computations related to light refraction provided in **calculation.py** file
- Optical prism 
- LED
- [Temperature sensor ](https://www.sparkfun.com/products/11050)([datasheet](https://cdn.sparkfun.com/datasheets/Sensors/Temp/DS18B20.pdf))
- [Pressure sensor](https://www.mondaykids.com/monday-kids-3-3-45-5v-digital-barometric-pressure-sensor-module-liquid-water-level-controller-board-0-45-40kpa-for-arduino.html) 
- [CO<sub>2</sub> sensor](https://www.sumozade.com/bmp180-digital-air-pressure-sensor-199) ([datasheet](https://learn.sparkfun.com/tutorials/bmp180-barometric-pressure-sensor-hookup-))
