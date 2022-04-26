# Analysis of the Grasshopper block cipher
## 1 Background
The Grasshopper (Kuznyechik) block cipher (GOST R34.12-2015)is the Russian block
cipher standard used by the government (non-military) institutions of that country. It
is also known by the name RFC7801. The goal for the designers was to replace the
old Russian standard block cipher (GOST 29147–89) known to be broken by several authors. The design follows the modern principles. It is a 9-round Substitution Permutation Network (SPN) with the block length of 128 bits and a 256-bit key. However, the criteria for choosing exactly the S-box used in this cipher have not been published. Biryukov et al. [1] published an analysis of this S-box and discovered its hidden
structure that offers possibilities for efficient implementation of the cipher, but at the
same time reduces the cryptographic strength of the cipher. The detailed description of
the Grasshopper block cipher is available in [2].

## 2 The task for the student
1. Read the description of the Grasshopper cipher [2]. Draw the schematic of the cipher. (10 points)
2. 
3. Implement the cipher in your favorite programminglanguage (for example c/c++, Java, or Python). Check the obtained output from the cipher against the values
given in [2] (subsections 5.4, 5.5, and 5.6). (30 points)

3. Read carefully the analysis of the S-box of Grasshopper given in [1]. Write
a report about the analysis (max. 8 A4 pages). From the report, it should be
clear that you understand this analysis. Concentrate on the consequences for
Grasshopper (Kuznyechik), ignore Stribog and STRIBOBr1 that share the same
S-box. (30 points)

4. Modify the implementation of the Grasshopper cipher by replacing the S-box
given with the table in [2] by the decomposition of this S-box obtained in [1].
Check the new implementation in the same way as in Task 2. (30 points)

## 3 Handing in
This is individual work, do not collaborate with others. Put everything you produce in
a single ZIP file Grasshopper.zip. The handing in technology is Inspera, and the
submission is anonymous. The deadline is April 29th 2022 at 23.59, Oslo time

## References
[1] A. Biryukov, L. Perrin, and A. Udovenko, Reverse-engineering of the S-box of
Stribog, Kuznyechik and STRIBOBr1, in Proceedings of Eurocrypt 2016 M. Fischlin, J.-S. Coron (eds.), Part I, Lecture Notes in Computer Science, LNCS, Vol.
9665, pp. 372–402.

[2] https://datatracker.ietf.org/doc/html/rfc7801.html
