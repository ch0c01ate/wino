# wino:wine_glass:

Authors: [Hryts](https://github.com/Hryts), [ch0c01ate](https://github.com/ch0c01ate), [yankur](https://github.com/yankur)

## Description:

**Wino** project is a solution to problems which people usually come up with during the wine creation. It is a device with embedded hardware called to provide an ability to observe and control the fermentation process. 

## Features:

With our device, you can see such **parameters** as:

- Brix °Bx (amount of sugar per 100 g of solution)
- Gas pressure (which tells you about the dynamic of the process)
- Temperature (important factor on which yeasts ability to live depends)

## What is done:

- Many different approaches checked
- Components found, filtered and ordered
- Computations provided



## TODO:

- Construct and program the device



## Previous decisions:

- Density Method 

  You can check [the Density measuring method by Cypress](https://github.com/ch0c01ate/wino/blob/master/presentations/Measuring%20Density.ppt) to discover more about it.

- Optical Method (using light polarization)

  Check [Optical method](https://github.com/ch0c01ate/wino/blob/master/presentations/Optical%20Method.pptx) to discover how it works. This method was rejected because of the turbidity of the wine.

## Final decision:

Refractive method of the °Bx measurement the was chosen. With the help of camera, we are going to get data about total internal reflection angle, which depends on refractive indexes of wine (which, itself, depends on Brix since sugar is optically active). To make the angle big enough to measure it, we will use prism made of optical glass with a refractive angle ~1.52.

## Computations:

All computations related to light refraction provided in **calculation.py** file.

## Components:

- [Camera](https://www.sparkfun.com/products/15430) ([datasheet_1](https://cdn.sparkfun.com/assets/0/b/0/e/d/LI-IMX219-MIPI-FF-NANO_SPEC.pdf), [datasheet_2](https://pinoutguide.com/dev/Siemens/M55/))
- Optical prism 
- LED
- [Temperature sensor ](https://www.sparkfun.com/products/11050)([datasheet](https://cdn.sparkfun.com/datasheets/Sensors/Temp/DS18B20.pdf))
- [Pressure sensor](https://www.mondaykids.com/monday-kids-3-3-45-5v-digital-barometric-pressure-sensor-module-liquid-water-level-controller-board-0-45-40kpa-for-arduino.html) 
