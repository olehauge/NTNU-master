# Practical 06 - ePassport and Iris
## 1 Scope of the Practical
This practical will make you familiar to ePassport and the access control to the biometric reference data in
the RFID chip. Afterwards we will work on iris recognition. We will interactively work on these practical
tasks in a tutorial style. However the full exercise sheet should be completed in order to prepare yourself
for the final exam.
## 2 Reading Biometric Data from the ePassport
For the first part of the practical, you can work with your own electronic passport (if you like). Otherwise
you can work with the sample documents that are provided. With the following tasks you will make
yourself familiar with the passport and specifically with the information in data group (DG) 1, 2 and 3 of
the logical data structure (LDS) as defined by ICAO specification 9303.
## 2.1 Unique RFID
Each RFID provides a UID to authenticate with the passport reading device.
Task: Check the UID that is displayed for the sample metro ticket and the UID that is displayed for your
passport. What do you observe, when you present the RFID multiple times?
## 2.2 Access Control to Data Groups
You should understand the basic principle of the basic access control (BAC) protocol. Start the golden
reader tool and understand, what is the starting information to generate a key for the BAC protocol. With
this practical you will extract the face image and the fingerprint images from your passport (of course only
if you want to try).
Task: Use the information from the MRZ to access the information in DG1, DG2 and DG3. What is contained in DG3? Is it for all sample documents possible, to retrieve the content of DG3? What is missing, if
the reading fails?
## 2.3 Full Protection of the Passport
Some privacy concerned individuals do not trust the access control protocol.
Task: Which simple countermeasure can you use to shield the biometric data in your passport?
## 3 Iris Segmentation and Normalization
In order to get familiar with the preprocessing steps (segmentation and normalization) you should run all
processing steps with the provided Matlab framework.
To run all the preprocessing steps, you need to run the main program main_program_iris.m. We provide three BMP iris images for demonstration - 001_1_1.bmp, 008_1_1.bmp, which stem from the CASIA
database Version 1, and also the NIRIris.bmp downsized from the original image at:
https://en.wikipedia.org/wiki/Iris_recognition.
The parameter method denotes different methods for locating the two boundaries of the iris and the pupil.
You can set method = 1 (Daugman’s integro-differential operator method) or 2 (Canny operator and Hough
transform).

## 3.1 Segmentation
The first step in iris recognition is the segmentation of the textured iris pattern. You will use the implementation segmentiris.m for the purpose to isolate the useful iris region out of the whole image (i.e. to find
the iris and pupil boundaries). You can use the two methods based on Daugman or Canny operator.

In segmentiris.m, the functions SearchInnerBoundary and SearchOuterBoundary are used
by the Daugman method to find the pupil boundary and the iris boundary respectively; and the function
findcircle is used by the Canny method, to find the two boundaries for the iris and the pupil.
Task: When you set method = 1, the integro-differential operator is used for edge detection from the
iris images; when you set method = 2, the Canny operator and Hough transform are used for edge detection from the iris images. You shall test all the three iris images 001_1_1.bmp, 008_1_1.bmp and
000_wiki_iris.bmp.
Run the createiristemplate(’*.bmp’,method) and compare the boundary detection results
from the two methods, and especially check the result from 000_wiki_iris.bmp. Explain what you
observed.
## 3.2 Parameter Optimization
The Canny operator is used in the Matlab script for edge detection from the iris image. The 8th parameter to function findcircle is vert representing vertical edge contribution (0-1), and the 9th parameter to function findcircle is horz representing horizontal edge contribution (0-1). In segmentiris,
findcircle was used twice to detect iris boundary and pupil boundary, respectively, but with a different
vert and horz setting.
Task: Try to change horz to 1 and vert to 0, or other settings different from the original, to watch the
final boundary detection results on the test image 001_1_1.bmp and 008_1_1.bmp. Explain the detection results.

## 3.3 Normalization
One you have segmented the iris pattern in a robust manner you will implement the iris normalization
using normaliseiris.m. The purpose of this function is to transform the useful iris region (meaning that
eyelids, eyelashes and the pupil are removed) to a rectangular matrix.

Task: Check the meaning of 9th and 10th parameters to the function normaliseiris and try other settings.
Task: Consider this question: with a normalized iris matrix A as template, how can you achieve alignment of the normalized iris matrix if it was generated from a probe captured with slight rotation?
