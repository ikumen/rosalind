#!/usr/bin/env python

'''
bs_prot.py: Translating RNA into Protein (http://rosalind.info/problems/prot/)

Problem: The 20 commonly occurring amino acids are abbreviated by using 20 letters 
from the English alphabet (all letters except for B, J, O, U, X, and Z). Protein 
strings are constructed from these 20 symbols. Henceforth, the term genetic string 
will incorporate protein strings along with DNA strings and RNA strings.

The RNA codon table dictates the details regarding the encoding of specific codons 
into the amino acid alphabet.


Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
Return: The protein string encoded by s.

Sample Dataset:
AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA

Sample Output:
MAMAPRTEINSTRING
'''
import os
import pytest

from helpers import output_path


## TODO: move to helpers. 
class GeneticCodesMap():
	'''Represents a genetic codon table.
	'''
	def __init__(self):
		with open(os.path.join(os.path.dirname(__file__), 'data/rna_codon_table.txt')) as input:
			self.table = dict([line.strip().split() for line in input])

	def get(self, codon):
		return self.table[codon]


def translate_to_protein(rna):
	'''Translates given rna string into protein string represented by encoded codons in rna.
	'''
	codesMap = GeneticCodesMap()
	protein = ''
	for i in range(int(len(rna)/3)):
		# each codon is three bases long
		codon = rna[i*3:(i*3)+3]
		if codon and codesMap.get(codon) != 'Stop':
			protein += codesMap.get(codon)
	return protein


def test_translate_to_protein():
	assert 'MAMAPRTEINSTRING' == translate_to_protein('AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA')


def main():
	'''Main runner, to read data, compute and saves output.'''
	with open(os.path.join(os.path.dirname(__file__), 'data/rosalind_prot.txt')) as input:
		rna = input.readline().strip()

	with open(output_path(__file__), 'w') as output:
		output.write(translate_to_protein(rna))


if __name__ == '__main__':
	main()