# Mars Terrain Classification  
Eric Wright & Mauricio Ferrato

## Motivation

![Image1](https://github.com/mferrato/CISC489-Project-Machine-Learning/blob/master/dataset/poster_images/swiss1.png)  

Based on the project [Planet Four: Terrains](https://www.zooniverse.org/projects/mschwamb/planet-four-terrains), we are trying to use machine learning and artifical neural networks to train a computer to be able to classify terrains in images of Mars (such as the image above). The original Planet Four project was a community effort, taking a brute-force and human-driven approach to classifying images of Mars. This project had various individuals from around the world classify over 20,000 images of Mars, placing them into various categories such as "Swiss", "Spiders", "Baby Spiders", "Craters", and "Channel Networks". However, the most import two classifcations highlighted in Planet Four's results was the swiss and spiders classification.

## The Data

The images we are using are from the Mars Reconnaissance Orbiter (MRO). 

![Image2](https://github.com/mferrato/CISC489-Project-Machine-Learning/blob/master/dataset/poster_images/MRO.jpg)  

The MRO was equipped with a special camera called a Context Camera (CTX) which was able to take the highest resolution images of Mars that are currently available. These images cover several hundred square km, and each pixel represents roughly 30 cm^2. In our project, we used ~90 raw CTX images, which were subdivided into over 20,000 800x600 px images. These images are grayscale, and represent various locations of Mars during different years and seasons.  

![Image3](https://github.com/mferrato/CISC489-Project-Machine-Learning/blob/master/dataset/poster_images/CTX.jpg)  
The Context Camera found on the Mars Reconnaissance Orbiter.

We are using the [ISIS3 Software](https://isis.astrogeology.usgs.gov/) to handle the processing and cleanup of the CTX images (which is a similar process to what Planet Four did). We are also using the same set of images that Planet Four used. These images vary in quality, and a handful of images were taken during a period when Mars was covered in ice.

![Image4](https://github.com/mferrato/CISC489-Project-Machine-Learning/blob/master/dataset/poster_images/ice1.png)  
Image of Mars surface covered in ice.

Planet Four also defines a subset of the images as being "gold standard", meaning that they are the clearest images that we have available. These images also have classifications done by the Planet Four staff, and includes all possible classification categories, whereas the general, complete dataset only contains swiss and spiders.

## Methods

We are using the [DIGITs software](https://developer.nvidia.com/digits) to handle the execution of our machine learning algorithms and artificial neural network. Through DIGITs, we were able to create several different datasets for testing, and then use those datasets in different "jobs", where each job will allow us to train and test a neural network with various different settings. In terms of algorithms, we had LeNet, AlexNet, and GoogLeNet available to us, but only used AlexNet and GoogLeNet because LeNet is designed for much smaller images than ours.

### Gold Dataset - Squashed down to 512x512 px  
We squashed all of the images in the gold dataset from the base 800x600 image size down to 512x512 as this should work better with the algorithms. We also reserved a smaller percentage of the images to be used as a "validation" dataset, allowing DIGITs to test the neural network along the way and give us estimated accuracy of prediction. When using the 512x512 images in GoogLeNet or AlexNet, we tested it by taking a random crop of the images of 256x256 (which is what the algorithms are designed to use), and we also ran it without cropping.


### Gold Dataset - Squashed down to 256x256 px  
We also squashed the gold dataset striaght from 800x600 px to 256x256 px. We are worried that by squashing it by so much, we may lose a significant ammount of the features that the algorithm will need to properly identify the terrain.

### Total Dataset - Squashed down to 512x512 px  
We also used these methods on the full dataset. When using the full dataset, it is more difficult to test, because we can only test using "training images", or images that the neural network has already seen. Also, when using the full dataset, we are also including images that contain ice and images that may be subpar quality. However, this does give us a much larger selection of images.

### Total Dataset - Squashed down to 256x256 px  
Squashing the total dataset down to 256x256 is even more concerning, as we are worried that the loss in quality will be too much for some of the subpar images.

### Image Alterations  
We also tried a few alterations to the images to see if it would train the neural network any better. It didn't. But here's what we tried.

We were worried that since some images are light, and other are dark. So we took all of our images, and inverted the pixels; black pixels became white, and white became black. Here's an example of a before and after.

![Image6](https://github.com/mferrato/CISC489-Project-Machine-Learning/blob/master/dataset/poster_images/spiders2.png)  
![Image7](https://github.com/mferrato/CISC489-Project-Machine-Learning/blob/master/dataset/poster_images/spiders2_invert.png)  

We also attempted to do some color correction by ommiting the background of the image. For example, we could take a dark backgrounded image, and replace it with white. The image below is an example.

![Image8](https://github.com/mferrato/CISC489-Project-Machine-Learning/blob/master/dataset/poster_images/blackwhite.png)  

Again, neither of these approaches helped in the long run.

## Problems and Hardships  
We are having trouble getting the neural network to recognize the spiders terrain. Spiders appears as dots or splotches on the surface, and are often misclassified as having no discernable features. Some images will have spiders appear as dark splotches, and others will have them as light splotches.

![Image5](https://github.com/mferrato/CISC489-Project-Machine-Learning/blob/master/dataset/poster_images/spiders1.png)  
Surface containing spiders terrain.

We also see some outliers in our dataset. Some images contain the surface covered in ice, which are significantly darker than the average image. We also see some images as very blurry or grainy. Using the gold standard dataset can allieviate some of this, however.

## Results

For our main results, we are looking for accuracy of predicting swiss cheese, spiders, and none terrains against our entire 20,000+ dataset. Overall, the neural network is very good at predicting swiss and none. Spiders poses a problem, however. The highest accuracy neural network we achieved was using GoogLeNet, gold dataset, squashing image to 512x512 px, taking a random crop of 256x256, no extra data (such as inverted colors or color correction), and limiting the categories to 150 images (which is the size of the gold spider dataset).

Total Accuracy = 86.09%  
Swiss Accuracy = 100.00%  
None Accuracy = 85.57%  
Spiders Accuracy = 60.20%  

This neural network was a little bit less accurate for the none dataset (others were able to get 95% on none), but it is by far the most accurate for spiders (others were around 30-40% accurate).

Some of our results can be found in our .result files.

## Conclusion



## Future Direction

