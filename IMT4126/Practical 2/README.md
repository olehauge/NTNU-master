# Practical 02 - Performance Metrics and Face Capture
## 1 Scope of the Practical
The practical will discuss selected aspects of the lecture along the following tasks. We will interactively
work on these practical tasks in a tutorial style. However the full question sheet (at the end of this document) shall be completed and returned to the lecturer by the end of this week, in order to prepare yourself
for the final exam. You shall scan your answers and upload to Blackboard.
## 2 Basic Terms in Biometrics
It is essential that your writing (in the term paper and also in the exam) is aligned with the ISO/IEC harmonized vocabulary. Check the following terms using the lecture slides and the definitions that you can
find at: http://www.christoph-busch.de/standards.html
- Biometric Characteristic: Investigate this term and differentiate it from the term template. Under
which conditions or in which context is it correct to phrase that facial features have been observed.
- Template: Investigate and explain, why there is a difference between a template and a biometric reference. Clarify whether or not a photo image that is stored in an electronic passport is considered as a
template?
- Comparison: Investigate this term and clarify, why the term matching that is still found in a large part
of the literature has been deprecated by ISO. What were the reasons causing the deprecation of this
term?
## 3 Biometric Performance
When you are testing the biometric performance it is essential that you use standardized metrics, which
were defined in ISO/IEC 19795-1 (available in Blackboard). You can find the relevant metrics explained in
the lecture slides. With that knowledge answer the following questions.
## 3.1 Test Types
Task: What types of performance testing do you know and why is it essential to differentiate them?
## 3.2 Thresholding
Assume a biometric system is characterized by Figure 1. The system operator can specify a threshold t for
the system.
Task: In which direction should the system operator move the threshold to obtain a more secure system
(i.e. lower likelihood of unauthorized access)? What is the impact on the FNMR(t) and FMR(t)?
Task: In which direction should the system operator move the threshold to obtain a more convenient system (i.e. lower likelihood of rejecting legitimate users)? What is the impact on the FNMR(t) and FMR(t) in
this case?
## 3.3 Metrics
You shall analyze, what is expressed by FMR, FNMR, FAR, FRR.
Task: Explain these metrics and specifically describe the difference between FMR and FAR? In a technology
testing, what should you observe to determine the FAR?
## 3.4 Combined Metrics
In a technology evaluation, cross-comparisons are computed on a gallery (corpus) of images. Those images included in the gallery do not cause a Failure-to-eXtract (FTX). However the FTE has been measured
in preparation of the data collection. Furthermore the FTC (Failure-to-Capture) was recorded in the acquisition process. The individual error rates are given as follows: F T E = 0.02 and F T C = 0.01. In the
experiment you observe the following error rates: FMR = 0.001 and F NMR = 0.01
Task: Compute from the above numbers the FAR, FRR, GFAR and GFRR.
