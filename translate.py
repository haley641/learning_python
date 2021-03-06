import sys
import mcb185
import argparse

#worked with Adrian



parser = argparse.ArgumentParser(description="FASTA FILE")

parser.add_argument("--file", required=True, type=str, default=None,
	metavar="<str>", help= 'file name')

arg = parser.parse_args()

for name, seq in mcb185.read_fasta(arg.file):
	print(f'>{name}') #w ill look like a fasta file
	print(mcb185.translate(seq))








#for the purpose of translation


"""





for seq in mcb185.read_fasta(sys.argv[1]):
	print(f'>{name}') #w ill look like a fasta file
	print(mcb185.translate(seq))


gcode = {
	'AAA' : 'K',	'AAC' : 'N',	'AAG' : 'K',	'AAT' : 'N',
	'ACA' : 'T',	'ACC' : 'T',	'ACG' : 'T',	'ACT' : 'T',
	'AGA' : 'R',	'AGC' : 'S',	'AGG' : 'R',	'AGT' : 'S',
	'ATA' : 'I',	'ATC' : 'I',	'ATG' : 'M',	'ATT' : 'I',
	'CAA' : 'Q',	'CAC' : 'H',	'CAG' : 'Q',	'CAT' : 'H',
	'CCA' : 'P',	'CCC' : 'P',	'CCG' : 'P',	'CCT' : 'P',
	'CGA' : 'R',	'CGC' : 'R',	'CGG' : 'R',	'CGT' : 'R',
	'CTA' : 'L',	'CTC' : 'L',	'CTG' : 'L',	'CTT' : 'L',
	'GAA' : 'E',	'GAC' : 'D',	'GAG' : 'E',	'GAT' : 'D',
	'GCA' : 'A',	'GCC' : 'A',	'GCG' : 'A',	'GCT' : 'A',
	'GGA' : 'G',	'GGC' : 'G',	'GGG' : 'G',	'GGT' : 'G',
	'GTA' : 'V',	'GTC' : 'V',	'GTG' : 'V',	'GTT' : 'V',
	'TAA' : '*',	'TAC' : 'Y',	'TAG' : '*',	'TAT' : 'Y',
	'TCA' : 'S',	'TCC' : 'S',	'TCG' : 'S',	'TCT' : 'S',
	'TGA' : '*',	'TGC' : 'C',	'TGG' : 'W',	'TGT' : 'C',
	'TTA' : 'L',	'TTC' : 'F',	'TTG' : 'L',	'TTT' : 'F',
}


for seq in sys.argv[1:]:
	print(mcb185.translate(seq))
	for i in range(0, len(seq), 3):
		prot += gcode[seq[i:i+3]]
	print(prot)

# You have been given the code above
# An example command line is
#	python3 translate.py ATGCGCCCGAACTAG ATGAAACCCGGGTTT

# Your task is to write a new program with the following features
# 1. Proper command line (argparse)
# 2. Reads sequences in from fasta format rather than sys.argv
# 3. Outputs sequences as fasta format
# 4. Accepts both uppercase and lowercase letters
# 5. Translates ambiguous amino acids as X (e.g. for weird codons)

# Hints
# 1. add functions and put them in your library
# 2. use string.upper() to normalize case


"""
