# Practical 03 - Fingerprint Process Analysis
## 1 Scope of the Practical
The practical will discuss selected aspects of the lecture along the following tasks. We will interactively
work on these practical tasks in a tutorial style. However the source code that you have generated, together
with the generated DET-curve and the full question sheet (at the end of this document) shall be completed
and returned to the lecturer by the end of this week, in order to prepare yourself for the final exam. You
shall scan your answers and and upload to Blackboard.
Please start to download for this practical the fingerprint image zip-file (SD14), which you can find in
the practical 03 section in Blackboard. The SD14-zip-file is composed of 150 unique finger prints captured
in two different sessions. The scripts are provided for both Window’s and MAC platform in the respective
folders.
Please remember to change the total_number_subjects and total_number_sessions accordingly
when you use change the dataset.
The file names are encoded in a following format: SubjectNumber_SessionNumber_FingerPosition.
jpg, where the FingerPosition is encoded by the finger position code according to figure 1.
Figure 1: Finger position codes according to ISO/IEC 19794-2:2005
## 1.1 NIST SD14 dataset
SD14 fingerprint images are provided by the National Institute for Standards and Technology (NIST) in the
WSQ image format. This subset of SD14 is provided converted to JPEG format in the task folder for this
practical.
## 2 Data Processing
For data processing in this practical we will use the free fingerprint image software NBIS that is provided
by the National Institute of Standards and Technology (NIST). Extensive information on NBIS you can be
found on http://fingerprint.nist.gov/NBIS/index.html
The relevant software is provided in Blackbord.
Note that under the Windows environment, all NIST functions (mindtct,bozorth3,dwsq,cjpegb)
must be run under the same folder containing cygwin1.dll.
## 2.1 Extraction of Feature Vectors
Your task is to apply the Minutia Extractor mindtct and generate from each image a feature vector. In
consequence you should have for session-normal-1, session-normal-2 a set of minutia feature vector files. The
program mindtct can be used to generate a minutiae feature vector:
mindtct filename.jpg minutiafilename
Now use the MatLab program Extract_Minutiae_Template.m to loop over all collected samples that
are in your image folder in order to obtain for each image a minutia feature vector file (i.e. template).
## 3 Data Analysis
Compose two similarity matrix with genuine and impostor comparison scores which can be obtained using
the bozorth3 function. Compute FMR(t) and F NMR(t), for different values of t. Think about the
ways to set the values of t. Draw a Detection Error Trade-off curve (DET) to visualize the recognition
performance.
You should use fingerprint feature vectors stemming from capture session-1 as enrolment feature vectors
(i.e. templates). Use the fingerprint feature vectors stemming from capture session-2 as probe feature
vectors.
## 3.1 Comparison Score Computation between Minutia Templates
The program bozorth3 can be used to compare two feature vectors filename1.xyt and filename2.
xyt

Use the MatLab program To_Do_Comparison.m to loop over all collected samples that are in your image
folder in order to obtain a comparison score per image pair.
To plot the DET Curves, use the following MatLab Code, which was also provided by NIST and which
is the standard reporting code for all work in the Norwegian Biometrics Laboratory (NBL).
Matlab code to plot DET is available in task-material folder. Make sure to add this folder in path while
executing the function To_Plot_DET.m to plot the DET curves.
3.2 Operating Point
Use the genuine and impostor scores to write a program that computes FMR and FNMR for a given threshold (e.g. T h = 0.4).
