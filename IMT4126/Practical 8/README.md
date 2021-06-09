# Practical 08 - Presentation Attacks on Fingerprint/Face Capture Devices
## 1 Scope of the Practical
This practical will make you familiar with presentation attacks on face and fingerprint recognition systems.
We will interactively work on these practical tasks in a tutorial style. However the full exercise sheet should
be completed in order to prepare yourself for the final exam.
## 2 Presentation Attacks against Face Recognition System
## 2.1 Face Verification Process
In this task, we first analyse the working of a regular face biometric system based on Local Binary Pattern
(LBP) features. To that end, two different functions are provided:
- enrolment lbp features = get lbp features(enrollment image) extracts the LBP features
from a given image.
- score = sc pdist2(enrolment lbp features, verification lbp features, ’cs’) returns the comparison score between the enrolment and test LBP features sets.
These functions also depend on other Matlab files provided, so do not forget to include all the material
provided into your path.

Task: Check the working of the face verification system:
- Examine the images provided in the face samples folder.
- Check if the system is accepting the subject 1 and rejecting the subject 2.
- 
Task (optional): Check the working of the face verification system with your own images:
- Capture two images of yourself using your laptop’s camera.
- Verify yourselves using the first image as enrolment data and the second as test. Check if the system
is accepting you and rejecting others.
## 2.2 Artefact Production and Executing the Presentation Attack
In this task, we try to attack the system by presenting the artefact samples. As a first step, we produce two
different type of artefacts - printed artefacts (print your picture using the printer in the university premises)
and electronic artefacts (capture your face image from iPad provided). Note: Due to Corona, neither printer
nor ipad are physically available. Instead, please capture your face image from your notebook to create a
simple presentation attack.

Task: Attack the face verification system:
- Present the system with printed artefact face image provided.
- Note down if you are able to verify easily with print attack.

Task (optional): Attack the face verification system with your own images:
- Present the system with digital artefact face image for your verification.
- Note down if you are able to verify easily with print attack.

## 2.3 Testing Presentation Attack Detection
In the last part of this task, we try to avoid the attacks by making the system robust against presentation
attacks. To that end, a third function to carry out Presentation Attack Detection (PAD) based on LBP features
is provided (i.e., you can use the same LBP features from the image to execute this PAD method):
- [classified presentation, accuracy, prob estimates]
= svmpredict(0, verification lbp features’, pad detector, ’-b 1’) returns the probability (prob estimates) of a sample being classified as PA. Therefore, for prob estimates > 0.5,
we consider the sample an attack. This function is based on a pre-trained pad detector.
In addition, a set of pre-trained detectors for print attacks, iPad, iPad pro and iPhone are provided.

Task: Check the PAD module for face verification system:
- Using the normal ’pad dector’, check that your bona fide images are correctly classified as such.
- Present the system with printed artefact face image as in the previous task, checking whether the
samples are bona fides or PAs with the corresponding ’pad dector’.
- Note down if you are able to verify easily with print attack.
- Try using other pre-trained detectors: is the system still capable of detecting the attack?
## 3 Presentation Attacks against Fingerprint Recognition System
In this task, we will use again the NIST minutiae extractor and comparator utilised in the third practical. To that end, you will need to use the ’mindtct’ for feature extraction and the ’bozorth3’ for template
comparison. In addition, a set of images from different fingers from a single person are provided:
- On the one hand, three bona fide samples per finger.
- On the other hand, PAs fabricated with play-doh and silicone.

Task: First, familiarise yourself with the images:
- Are there any visual differences between the bona fides and the PAs?
Now, we will test the minutiae extracted with the NIST software:

Task: First, extract the minutiae files for at least two bona fide samples of the same subject, one from a
different subject, and one of each different PA.
- Are there any visual differences between the bona fides and the PAs?
- Is the number of minutiae extracted similar or different? (tip: open the xyt file with an editor and look
at the number of rows)
Finally, we will test the comparison scores:

Task: First, carry out all possible comparisons between the minutiae files extracted.
- Do you see any differences between the mated and non-mated comparison scores for the bona fides?
- And what about the comparisons between bona fides and PAs?
- Do you think these PAs would be positively verified?
