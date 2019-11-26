# BioComputation Assignment

Report on attempts to solve classification problems using evolutionary AI.

Build upon the original GA developed in class.

Start by using a rule based scheme

Alter fitness function of your GA

Each individual is now a set of rules.

## What each dataset contains

### data1.txt

 Contains binary data each with six variables and one for the class. Hence each rule needs a condition containing five bits and an output of one bit, eg, IF <010001> THEN <1>. 
If each rule base consists of ten rules then each individual needs (6+1)x10 = 70 binary genes: the binary string is the rules concatenated together.

### data2.txt

## Adaptions from original GA

Create an object that contains:

* a binary array called condition that is 5 long.
* a binary value that is to mark the output of the condition.

