# Practical 12 - Mouse Dynamics
## 1 Scope of the Practical
This practical will make you familiar with mouse dynamics. We will interactively work on these practical
tasks in a tutorial style. However the full exercise sheet at, the end of the document, should be completed in
order to prepare yourself for the final exam. You should scan your answers and upload this to Blackboard.
## 2 Data structure and feature extraction
We have data of 15 users while using their computer for a long period of time. From 15 users we extracted
the Mouse Move (MM) data which is presented in 15 different files. Each file consists of a long array of
5 columns. Column 1 is a unique identifier, columns 2 and 3 represent X and Y coordinate of the mouse
pointer and column 4 is the timing information. Finally column 5 is a reference back to the identifier. If this
is value 0, then this means the start of a new MM, while otherwise it is a reference back to the identifier in
column 1.

Task 1: Open file MM1.mat to see structure of the data

Task 2: Can you write a short script to detect how many MM you find in each of the 15 files?

Task 3: Look at the ExtractMouseMoveFeatures.m code. Why do you think you need the condition
statement in line 13?

Task 4: Run the ExtractMouseMoveFeatures.m code twice. Once with and once without the conditional statement from line 13. What are the differences in the results?.

Task 5: Adapt the code of ExtractSingleMouseMoveFeatures.m to include extraction of other features.
