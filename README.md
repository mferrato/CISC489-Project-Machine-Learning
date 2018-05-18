# Mars Terrain Classification  
Eric Wright & Mauricio Ferrato

## Motivation

![Image1](https://github.com/mferrato/CISC489-Project-Machine-Learning/blob/master/dataset/poster_images/swiss1.png)  

Based on the project [Planet Four: Terrains](https://www.zooniverse.org/projects/mschwamb/planet-four-terrains), we are trying to use machine learning and artifical neural networks to train a computer to be able to classify terrains in images of Mars (such as the image above). The original Planet Four project was a community effort, taking a brute-force and human-driven approach to classifying images of Mars. This project had various individuals from around the world classify over 20,000 images of Mars, placing them into various categories such as "Swiss", "Spiders", "Baby Spiders", "Craters", and "Channel Networks". However, the most import two classifcations highlighted in Planet Four's results was the swiss and spiders classification.

## The Data

The images we are using are from the Mars Reconnaissance Orbiter (MRO). 

![Image1](https://github.com/mferrato/CISC489-Project-Machine-Learning/blob/master/dataset/poster_images/MRO.jpg)  

The MRO was equipped with a special camera called a Context Camera (CTX) which was able to take the highest resolution images of Mars that are currently available. These images cover several hundred square km, and each pixel represents roughly 30 cm^2. In our project, we used ~90 raw CTX images, which were subdivided into over 20,000 800x600 px images. These images are grayscale, and represent various locations of Mars during different years and seasons.  
We are using the [ISIS3 Software](https://isis.astrogeology.usgs.gov/) to handle the processing and cleanup of the CTX images (which is a similar process to what Planet Four did). We are also using the same set of images that Planet Four used. These images vary in quality, and a handful of images were taken during a period when Mars was covered in ice.
