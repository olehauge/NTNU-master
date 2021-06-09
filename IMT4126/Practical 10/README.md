# Practical 10 - Continuous Authentication
## 1 Scope of the Practical
This practical will make you familiar with Continuous Authentication. We will interactively work on these
practical tasks in a tutorial style. However the full exercise sheet should be completed in order to prepare
yourself for the final exam.
## 2 Data structure and feature extraction
You have received a set of data related to continuous authentication and some matlab functions needed for
the analysis. The data consists of free typing of 15 different persons, each describing 2 different paintings by
Norman Rockwell. The reference text is a description of the painting ”Stay at Home (Outward Bound)” and
the probe text is a description of the paining ”The Runaway”. Both texts are written on a desktop keyboard.

Task 1: Load the file ”User1.mat”. This file contains two variables: R and P. Both variables have the same
structure. Look at R (or equivalently P) and try to figure out the meaning of each of the three columns.
## 2.1 Reference creation
Open the file main.m and run lines 2-7 to create duration and latency profiles for all reference texts of the
users.

Task 2: Check the code for MakeDurProfile and determine what values can be found in RefDur.
Task 3: Check the code for MakeLatProfile and determine what values can be found in RefLat.
## 2.2 Probe creation
Repeat the above by executing lines 10-15 of main.m
## 2.3 Distance calculation (based on durations only)
Study lines 18-32 of main.m. These lines compare ”RefDur” of user ”UserR” to ”ProbeDur” of user ”UserP”
and calculate the R-measure.

Task 4: Run the code in lines 18-32. Explain why ”gen” at the end has length 15 and imp has length 210.
Task 5: Run the code in line 35 and see what the FMR, FNMR and Half Total Error Rate (HTER) is when
only durations are used for analysis
## 2.4 Distance calculation (based on latency only)
Repeat the above for latencies only by running lines 38-54 of main.m
