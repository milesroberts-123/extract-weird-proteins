from Bio import SeqIO
from Bio.Seq import Seq
import sys

print("USAGE: python3 extract_weird_proteins.py <NAME OF FASTA FILE WITH PROTEINS> <NAME YOU WANT FOR OUTPUT FILE OF NORMAL PROTEINS> <NAME YOU WANT FOR OUTPUT FILE OF WEIRD PROTEINS>")
print("Loading weird sequences...")
#Remove werid sequences
normal = []
weirdos = []
for seqrecord in SeqIO.parse(sys.argv[1], "fasta"):
#Extract sequence
	seq = seqrecord.seq

#Check if sequence has more than one stop codon
	stops = seq.count("*")

#Check if sequence does not start with M
	start = str(seq[0])

#If sequence has more than one stop codon, exclude it.
#If a sequence has 1 stop codon, it must be at the end
#All sequences must start with M
	if stops == 1 and start == "M":
		seq = str(seq)
		if seq.find("*") == (len(seq) - 1):
			normal.append(seqrecord)
		else:
			weirdos.append(seqrecord)

	if stops == 0 and start == "M":
               	normal.append(seqrecord)

	if stops > 1 or start != "M":
		weirdos.append(seqrecord)

print("Found %i proteins that had at most one stop codon at the end of the sequence and began with methionine" % len(normal))
print("Writing normal proteins to %s ... " % sys.argv[2])
SeqIO.write(normal, sys.argv[2], "fasta")

print("Found %i proteins that had more than one stop codon and/or did not begin with methionine" % len(weirdos))
print("Writing weird proteins to %s ..." % sys.argv[3])
SeqIO.write(weirdos, sys.argv[3], "fasta")
print("Writing complete.")
