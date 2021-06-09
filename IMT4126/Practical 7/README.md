# Practical 07 - Sample Quality and Data Privacy
## 1 Scope of the Practical
This practical will make you familiar with face sample quality assessment and a simple yet effective method
for privacy protection of biometric reference data. We will interactively work on these practical tasks in a
tutorial style. However the full exercise sheet should be completed in order to prepare yourself for the final
exam.
## 2 Sample Quality
Measuring sample quality is essential to avoid poor images entering your enrolment database. Thus, in this
task, we investigate face quality metrics and seek how we can measure for the given facial images a quality
score.
## 2.1 Quality Scores
In the task-material you can find Matlab code to compute face quality measures under quality-estimation
folder.

Task: Analyze the sample quality of the images provided.
- The sample face images are given in folder test-subject.
- Use the script estimate_quality.m to read the images and compute and document the face quality for the set of provided images.
- We estimate Blur, Sharpness, Exposure, Image Brightness, Image Contrast and Perceived Contrast of the image.
- Save the obtained quality metrics as a matrix ”data”, where each row represents one quality metric and each column represents one of the provided example images
## 3 Privacy Enhancing Technology
In order to comply with the Privacy by Design principle, we shall develop biometric systems, that incorporate biometric template protection. Those systems must handle pseudonymous identifiers, which comply
with three major requirements, in accordance with the ISO/IEC IS 24745:
- Irreversibility: it should not be feasible to recover the original biometric sample from the information stored in the template.
- Unlinkability: given two templates, enrolled in different systems, it should not be feasible to decide whether they conceal the same individual respectively the same biometric instance.
- Performance preservation: there should be no performance degradation with respect to the unprotected
system.

In this practical you will implement and evaluate a biometric template protection scheme based on
Bloom filters. To that end you should download the task-material.zip, which contains in the folder
data-privacy the following files:
- dataIrisCodes.mat: the binary unprotected templates extracted from each sample of the IITD iris
database.
- A Matlab software framework.

## 3.1 Bloom Filter based Template Protection
In the folder data-privacy you can further find Matlab code to compute pseudonymous identifiers from
binary feature vectors, and also the corresponding distance functions between unprotected and protected
templates in order to carry out recognition. Note that for this practical the MATLAB dsp-toolbox and also
the communication-system-toolbox is required. The biometric template protection scheme that you will
implement and evaluate is built in a two-step approach: i) first, unprotected binary templates (also known
as iriscodes) are extracted from the iris samples, and ii) second, the Bloom filter based protected templates
(i.e., pseudonymous identifiers) are computed from the iriscodes. The first step has already been done, and
you can find the extracted iriscodes in the file dataIrisCodes.mat.

Task: Now, we need to transform the provided unprotected feature set into Bloom filter based templates.
To that end, you need to consider the following script:
- scriptComputeBFTemplates: this script loads the iriscodes stored in dataIrisCodes.mat and
computes the corresponding protected Bloom filter based templates, storing them in the file
dataBFTemplates.mat.
Once the template protection scheme is implemented, we need to assess that the aforementioned requirements (i.e., irreversibility, unlinkability and performance preservation) are fulfilled. We will assume
that the Bloom filter transformation is irreversible, and evaluate the other two requirements in the following tasks.

Task: Analyse the degradation in performance, plotting the DET curves for the unprotected and protected
systems. To that end, you need to consider the following scripts:
- scriptComputeScores_Unprotected: this script loads the iriscodes stored in dataIrisCodes.
mat and computes the mated and non-mated distances between unprotected binary templates, storing them in the file unprotectedScores.mat.
- scriptComputeScores_BFTemplates: this script loads the protected templates stored in
dataBFTemplates.mat and computes the mated and non-mated distances between the protected
Bloom filter based templates, storing them in the file protectedScores.mat.

Task: Analyse whether the computed pseudonymous identifiers are unlinkable. Ideally, if we compare
templates which are protected with different keys, and protect samples from the same or different subjects
/ biometric instances, the distance should be very similar. In order to assess whether this is true for this
scheme, compute several protected templates for two or more samples belonging to two or more different
subjects, and compare their distances. To that end, you should consider the following functions:
- template=computeBFTemplate(features,nWords,nBits,key): given the Bloom filter extraction parameters nWords and nBits (you can use the values in scriptComputeBFTemplates),
and a secret key key, this function returns the protected template corresponding to the given unprotected template (features).
- d=BFdistance(A,B): this function returns the distance between two templates, A and B.
Examples of usage of the aforementioned functions may be found in scriptComputeBFTemplates and
scriptComputeScores_BFTemplates, respectively.
You can compare these scores to the scores generated for verification with scriptComputeScores_
BFTemplates, generating the histograms for the mated and non mated scores using the histogram function from Matlab (https://de.mathworks.com/help/matlab/ref/histogram.html).
