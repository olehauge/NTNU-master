# User Identification based on SSH packets (SSH) (pb)
## Background
In interactive mode will SSH send an IP package after every keystroke to
the remote host. This will reveal timing information on the typing pattern
of the user and might reveal information about his/her identity. Difference
with normal KD is that only one timing information is available per key,
instead of key-down and key-up time. On top of that can, due to network
conditions, the sending of keys be delayed.

## Task
- Perform an experiment to collect data
- Analyse data
- Write report on the findings.
## Expected Outcome
- Collected dataset
- Report on the performance of user authentication or identification based on SSH packets timing.
## Starting Reading and other Material
- [Flucke, T. J.: Identification of Users via SSH Timing Attack, MSc thesis, 2020](https://digitalcommons.calpoly.edu/cgi/viewcontent.cgi?article=3587&context=theses)

**NB!** All collected data is anonymized. 
