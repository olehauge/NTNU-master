# Practical 04 - Fingerprint Pipeline Implementation
## 1 Scope of the Practical
This practical will discuss a typical fingerprint processing pipeline and the relevant steps, which have been
used for many existing fingerprint recognition systems. We will interactively work on these practical tasks
in a tutorial style. However the full exercise sheet should be completed in order to prepare yourself for the
final exam.
## 2 Data Preparation
We will work with some sample images that are provided in the task-material folder. You might as well
continue with the data that we collected in the second practical.
## 3 General Pre-processing Steps for Fingerprint Images
Usually, a fingerprint image will undergo several pre-processing steps before a fingerprint template, such
as a minutiae vector, is created. The purpose of fingerprint image pre-processing is to improve the clarity
of ridge structures, which can be achieved in two ways:
• Enhancing the genuine ridges (and valleys) which are corrupted by a small amount of creases, smudges,
..., etc. but still visually recoverable by information provided by surrounding regions; and
• Removing i) non-ridge regions and ii) regions corrupted by a severe amount of noise and distortion
to a point that no true ridges and valleys can be recovered from surrounding regions.
The general pre-processing steps include:
1. Ridge region mask estimation
2. Pixel intensity normalization
3. Ridge orientation estimation
4. Ridge frequency estimation
5. Ridge region masking
6. Filtering
7. Binarization
8. Thinning
After the above 8 steps, fingerprint features such as minutiae points can be easily extracted for creating a
stable template.

## 4 Matlab Implementation of Fingerprint Pre-processing Pipeline
In this task you should implement a fingerprint image processing pipeline such that your code will provide
the skeleton of fingerprint ridges as a polygonal structure. You can implement the algorithms from scratch
if you are a skilled programmer - but we recommend that you apply some available Matlab code, which is
provided in this practical’s task-material package. This package includes 9 Matlab code-files for fingerprint
image preprocessing and 4 images from the public database FVC2002 DB2-A for testing.
Note that main_program.m is the main program.
- freqest.m
- plotridgeorient.m
- ridgefilter.m
- ridgefreq.m
- ridgeorient.m
- ridgesegment.m
- normalise.m
- fp_bwskel.m
are functions used by main_program.m.
Part of the source code has been extracted from:
http://www.csse.uwa.edu.au/˜pk/Research/MatlabFns/FingerPrints/Docs/index.html
with a reference publication:
Hong, L., Wan, Y., and Jain, A. K. ’Fingerprint image enhancement: Algorithm and performance evaluation’. IEEE Transactions on Pattern Analysis and Machine Intelligence 20, 8 (1998), pp 777-789.
Note that in the following sections the area in courier font are matlab codes. All parameters’ explanation
and settings can be found in the Matlab function description in the corresponding *.m files.
## 4.1 Step 0 - Image reading and showing
``
im=imread(’xxx.ext’);
``
xxx.ext is the fingeprint image filename that you want to process
``
figure(1)
imshow(im)
title(’originalimage’)
``
## 4.2 Step 1 and 2 - Intensity normalization and ridge region mask estimation
Identify ridge-like regions and normalize image
``
blksze=8;thresh=0.1;
[normim,mask]=ridgesegment(im,blksze,thresh);
figure(2)
imshow(normim,[min(min(normim))max(max(normim))]);
title(’intensitynormalizedimage’)
figure(3)
imshow(mask)
title(’maskimage’)
``
## 4.2.1 Task 1
Check the meaning of blksze and thresh and try other settings for values of blksze and thresh to
check the results.

## 4.2.2 Task 2
How was the region segmentation done in Step 2 of the program? What is the difference between fingerprint image enhancement (step 1-6) and a general image enhancement method (such as histogram
equalization) in terms of purpose and effect? The draft processing pipeline that is provided to you in
the main_program.m is operating on a histogram normalized image. Your task is now to find the MatLab function that does compute the histogram equalization and to process the histogram equalized image
versus the histogram normalized image. Check the result of both preprocessing methods and evaluate and
compare the impact on the subsequent steps in the pipeline.
## 4.3 Step 3 - Ridge orientation estimation
Determine ridge orientations.
``
[orientim,reliability]=ridgeorient(normim,1,5,5);
plotridgeorient(orientim,20,im,2)
figure(6)
imshow(reliability,[min(min(reliability))max(max(reliability))])
title(’orientationreliabilitymap’)
``
In the orientation reliability map, gray scales from 0 (black) to 255 (white) indicates the reliability from low
to high degrees. Note that the background areas are mostly with 0 (black) in reliability.
## 4.3.1 Task 3
Check the meaning of the second parameter of plotridgeorient and try other values. You should
increase by 50% and also reduce down to 50%
4.4 Step 4 - Ridge frequency estimation
Determine ridge frequency values across the image.
``
blksze=32;
[freq,medfreq]=ridgefreq(normim,mask,orientim,blksze,5,5,15);
figure(7)
imshow(freq,[min(min(freq))max(max(freq))])
title(’spatialfrequencymap’)
``
## 4.4.1 Task 4
Try other settings for values of blksze.
## 4.5 Step 5 - Ridge region masking
We use the ridge area mask obtained from the step 2 to find the trustful ridge regions, which also reduces
the computational complexity for the following steps.
``
freq_masked=freq.*mask;
``
## 4.5.1 Task 5
Try medfreq instead of freq in Step 5. Compare the results and think what freq and medfreq imply
respectively to the enhanced image (Figure 8) and also the binarized image (Figure 9).

## 4.6 Step 6 - Filtering
After ridge orientation estimation in Step 3 and ridge frequency estimation in Step 4, we can enhance the
image using the estimated orientation and ridge frequency in local areas (each image blocks). The Gabor
filter (details can be found in the reference HongJain-FPImageEnhancement-PAMI-1998.pdf inside the practical’s package) has both frequency-selective and orientation-selective properties and thus is used to perform
this enhancement. Now apply such filtering process to enhance the ridge pattern.
``
newim=ridgefilter(normim,orientim,freq_masked,0.5,0.5,1);
figure(8)
imshow(newim,[min(min(newim))max(max(newim))]);
title(’ridgeenhancedimage’)
``
## 4.6.1 Task 6
Check the meaning of the 4th and 5th parameters of ridgefilter and try 0.1 as a value for the 4th
parameter. Explain, why you can see low values for the ridge frequencies in the center of the fingerprint
area, if you work with the default image 14_8.tif ?
## 4.7 Step 7 - Binarization
Binarise, ridge/valley threshold is 0.
``
binim=newim>0;
figure(8)
imshow(binim);
title(’binarisedimage’)
``
## 4.8 Step 8 - Thinning
Thinning can be done by many algorithms.
## 4.8.1 Task 7
Check the usage of the matlab function bwmorph and use it with suitable parameters to thin the binarized
result from step 7.
## 4.8.2 Task 8
Check the usage of the provided function fp_bwskel and add code in your main_program that that you
use it to thin the binarized result from step 7. Details can be found in the reference Deutsch-ThinningAlgorithmsACM-1972.pdf inside the practical’s package. Compare this result to the result obtained using the matlab
function bwmorph.
