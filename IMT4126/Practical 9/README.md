# Practical 09 - Keystroke Devices
## 1 Scope of the Practical
This practical will make you familiar with keystroke recognition. We will interactively work on these practical tasks in a tutorial style. However the full exercise sheet at, the end of the document, should be completed in order to prepare yourself for the final exam. You should scan your answers and upload this to
Blackboard
## 2 Data structure and feature extraction
The dataset consists of 20 files. Each file contains the captured data from a single user. Each user has typed
the password ”welcome42” 100 times. Users were allowed to make typing corrections during the data
capturing, but only the information from typing the correct password is available now. This means that if a
user typed ”welcome52” then the data is not available, but if he/she typed ”welcome42” using corrections,
then this data is available. Correcting will in fact have resulted in one or more large latency values!
Data is stored during capture as Action|time|value, while start and stop of a sample are indicated
by -|sampleNr|-.

Task 1: Open file 1.txt to see structure of the data
## 2.1 Loading data into Matlab
Reading the data into Matlab is done using the readtable command. A function LoadData.m is created
that reads a single file and stores the information in the variable data.

Task 2: Set user to 1, execute line 12 of main.m and display the first 20 lines of data.
## 2.2 Feature extraction
Run the feature extraction on the given data of user 1, using line 14 in main.m. The resulting features are
stored in variable f. The size of f will be 100x17.

Task 3: Confirm and explain the dimensions of the feature matrix f.
Task 4: Display the features of the first typing of the password and use the result of task 2 to confirm these
results.
## 3 Reference creation
Run lines 8-19 of the script first. Then run lines 22 and 25 of the main script (for different values in line 22)
to calculate the reference based on the number of samples in line 22.

Task 5: Check the influence of changing the number of samples for creating the reference on the mean (Mu)
and the standard deviation (Sigma).
## 4 Performance analysis
Line 28 will call a function that will calculate all genuine and impostor distance scores, while line 31 of the
main script will calculate the EER based on the genuine and impostor scores. The script CalculateScores.
m will call the script Dist.m where the actual calculation of the distance between reference and probe is
performed. Currently the scripts calculate the Scaled Manhattan Distance (SMD), and outliers (maybe as
a result of correcting a typo) are not considered in the distance calculation script. With 75 probes per user,
there are 64 latencies between the ’e’ and the ’4’ that are more than 0.75 second of which 33 are more than 1
second.

Task 6: Adjust the distance metric such that latencies over 1 second are ignored. The contribution to the
distance score should be the average of contributions of the other latencies
