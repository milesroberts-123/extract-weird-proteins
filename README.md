# extract-weird-proteins
Remove proteins that have internal stop codons and/or do not begin with methionine from a fasta file. 

This script will take a fasta file of protein sequences as input and partition the sequences into two seperate files: one containing weird proteins and another containing normal proteins.

A normal protein:
- has only one stop codon ("*")
- and the stop codon is the last character in the sequence
- and the first character is methionine ("M")
- or has no stop codon but begins with methioinine

A weird protein, on the other hand:
- does not begin with methionine
- and/or has an internal stop codon (i.e. a stop codon that is not the last character in the sequence)
- and/or has more than one stop codon

## USAGE

`python3 extract_weird_proteins.py <NAME OF FASTA FILE WITH PROTEINS> <NAME YOU WANT FOR OUTPUT FILE OF NORMAL PROTEINS> <NAME YOU WANT FOR OUTPUT FILE OF WEIRD PROTEINS>`

For example this code:

`python3 extract_weird_proteins.py example_proteins.fasta example_normal_proteins.fasta example_weird_proteins.fasta`

will take the sequences stored in example_proteins.fasta then output the normal proteins to example_normal_proteins.fast and the weird proteins to example_weird_proteins.fasta.

## DEPENDENCIES

1. Biopython - Installation instructions [here](https://biopython.org/wiki/Download). Usually you just type:

`pip install biopython`

2. Python3 and the `sys` python module, which usually ships with python installations.

