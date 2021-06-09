# Practical 05 - PCA Eigenfaces
## 1 Scope of the Practical
This practical will make you familiar with the details of the Principal Component Analysis (PCA) and how
this can be applied to a face recognition task. We will interactively work on these practical tasks in a tutorial
style. However the full exercise sheet should be completed in order to prepare yourself for the final exam.
## 2 Approach
We will use for this practical a small sized face image dataset ORL (40 subjects* 10 presentations = 400 samples), which you will find in the task-material as orl-40-faces.zip. For a PCA-based face recognition
system we must conduct the general processing steps as follows:
1. Read the face images as input vectors to the PCA
2. Separate a training set and testing set
3. Compute an average face image from the training set
4. Compute the PCA
5. Reconstruct an input image from the principal components
6. Compute enrolment templates (weight vector as reference) for each subject
7. Recognize the test images
## 3 PCA based Face Recognition
You will implement the PCA based face recognition according to the above steps. Fortunately you don’t
need to start from scratch. You should download the task-material.zip, which contains the following
- A Matlab software framework
- The ORL dataset orl-40-faces.zip
- A tutorial on PCA
Now in the following subsections the individual steps are handled.
## 3.1 Analyze the Matlab framework
Get yourself familiar with the provided PCA face recognition Matlab framework and check, how the input
images are read. The Matlab framework is named pca_facerecog.m
Task: Unzip the orl-40-faces.zip. For each subject there are 10 images available in the ORL dataset.
Generate a conversion function fileconvert.m, in order to read all the images from orl-40-faces
folder into a mat file representing all images. The images must be stored as single column vector for each
face sample (for each subject) in sequential order into that data matrix. Save that resulting data matrix as
mat file named as data.mat.

## 3.2 Separate Training and Test Data
Load the data.mat file created in the previous task. For each subject there are 10 images available in the
ORL dataset. We must ensure a proper separation of training and testdata. Thus, we will use 8 samples
per subject for training (i.e. to compute the PCA eigenvalues and eigenfaces). In consequence only two
remaining samples will be used for testing the recognition accuracy.
Task: Ensure that in the framework pca_facerecog.m, the parameter GallerySampleNumPerSub to
read training samples is set to 8.
## 3.3 Average Face
The average face is an essential concept in the PCA approach. Analyze the framework and identify In this
step, we will compute the PCA values using following function, given the reference and probe samples.
Task: Check the computation of the average face. Investigate the function pca_face.m to understand,
how the average face is generated. Save the average face image as orl-average-face.jpg.
## 3.4 Compute the PCA
In this step, we will learn a proper subspace mapping for our facial feature vectors and thus compute the
PCA eigenvalues and eigenvectors, using the following function and the given reference images from the
training set.
``[train_face,test_face,rimg]=pca_face(G,P,GallerySampleNumPerSub,SubjectNum,PCNum)``
Task: Check the computation of the eigenfaces. Set the parameter PCNum=5; and then investigate the
function pca_face.m to understand, how the eigenfaces are computed. Save the 5 most significant eigenfaces as orl-eigenface-01.jpg to orl-eigenface-05.jpg.
## 3.5 Reconstruct the Facial Images
The eigenfacess (i.e. eigenvectors) that you have computed in the previous step can serve, to reconstruct
the input image. Each reconstructed input image is in this case represented as a linear combination from
the eigenfaces. Note that the eigenfaces are ordered according to their significance.
Task: Reconstruct in pca_facerecog.m the first sample from the first subject using a linear combination
of i) 10 most significant eigenvalues ii) 100 most significant eigenvalues iii) 200 most significant eigenvalues. Store the three reconstructed images as
orl-reconstruction-10.jpg,
orl-reconstruction-100.jpg,
orl-reconstruction-200.jpg.
Recall that with the parameter PCNum you can control the number of principal components used.
Task: Analyse, how the reconstruction_error changes, as you modify the PCNum parameter.
## 3.6 Reference Template Calculation for each Subject
In this step, you need to calculate a template for each image that was selected from the Gallery defining the
parameter GallerySampleNumPerSub. As in your previous function call you filled train_face you
now have PCA eigenface vectors for each subject. We essentially compute the weights that are attributed
to each eigenface in order to represent the data subject by the eigenvectors.
If you get a correct calculation result for train_face by the function pca_face, then train_face
should be a (PCNum)-by-(SubjectNum*GallerySampleNumPerSub) matrix.
Using the provided framework pca_facerecog and the parameters
PCNum=10, SubjectNum=40, GallerySampleNumPerSub=8
the train_face should be a 10-by-320 matrix, representing 40x8=320 PCA feature vectors with each having based on the 10 largest PCA coefficients.
Note that for each subject, 8 feature vectors were computed in the PCA training phase. Our goal is to
generate only one reference vector out of the 8 feature vectors for each subject. In order to realize this we
calculate a mean vector over these 8 feature vectors (for each of the 40 subjects). These should be stored as
the output T (should be a 10-by-40 matrix) of this comp_template function.
Task: Check comp_template, place a breakpoint in line 13 and observe, how matrix T is filled.
Task: Check face_data_separation for usage of parameters GallerySampleNumPerSub
and ProbeSampleNumPerSub.
## 3.7 Recognize the Test Images
Now we test the recognition accuracy of our PCA based face recognition system. We can compute the
weight vectors for the test images and compute the distance to the enrolled data subjects.
For this you need to consider the following functions and parameters:
``[genuine,impostor]=dis(T,test_face,PNumPS,SubjectNum)``
Task: Using the framework you need first to calculate in test_face the distance between each of the
(ProbeSampleNumPerSub) test feature vectors (the parameter should be set to 2) and their remaining
single-vector reference template in T for each subject, and output the results to the vector genuine which
represents the intra-class distance. In the default parameter settings, ProbeSampleNumPerSub=2, and
therefore totally 2*40=80 distance values can be obtained and genuine should be an 80-dimensional vector.
Task: As well, you need to calculate the distance between each of the (ProbeSampleNumPerSub) feature vectors for each subject in test_face and all those 40 feature vectors in T except their own feature
vector, and output the results to the vector impostor which represents the inter-class distance. In the
default parameter settings, ProbeSampleNumPerSub=2, and therefore totally 2*40*(40-1)=3120 distance
values can be obtained and impostor should be an 3120-dimensional vector.
## 3.8 Reporting
Now in order to report the accuracy of our PCA based system we need to compute FMR and FNMR based
on the obtained intra- and inter class distance calculation, which represents the dissimilarity scores.
Task: Analyze the following functions and parameters:
``[fnmr,fmr]=fnmr_fmr(genuine,impostor)``
In this step, you can calculate the FMR and FNMR from the given two vectors genuine and impostor.
Note that in the fingerprint practical you used the bozorth3.exe to generate comparison scores, where
higher scores represented higher similarity. But this time we have computed distance values instead of
comparison scores. What should you do with distance value this time? The function fnmr_fmr will also
plot a simple DET curve for you. Store that simple DET figure reporting the biometric performance of your
system as file orl-simple-DET.png.
Task: If you are finished already then check other methods to report your results. You can re-use the
standard DET-plot implementation that you have used in the previous fingerprint practical (standard NBL
code). Can you note a difference in the DET-plots? Store that standard DET figure reporting the biometric
performance of your system as file orl-standard-DET.png. Which figure do you prefer? Further compare the EER for PCNum=5 versus PCNum=100. Matlab scripts (EER plot Biocoourse.m and files in folder
’DET-Code’) for drawing standard DET curve can be found from the Practical 03 material.
