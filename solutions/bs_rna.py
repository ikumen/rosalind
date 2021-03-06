#!/usr/bin/env python

'''
bs_rna.py: Transcribing DNA into RNA

Problem: An RNA string is a string formed from the alphabet containing 'A', 
'C', 'G', and 'U'. Given a DNA string tt corresponding to a coding strand, 
its transcribed RNA string uu is formed by replacing all occurrences of 
'T' in tt with 'U' in uu.

Given: A DNA string tt having length at most 1000 nt.
Return: The transcribed RNA string of tt.

Sample Dataset:
GATGGAACTTGACTACGTAAATT

Sample Output:
GAUGGAACUUGACUACGUAAAUU 
'''
import os
import pytest

from helpers import output_path


def transcribe_dna_to_rna(dna):
	return dna.replace('T', 'U')


def test_transcribe_dna_to_rna():
	'''Test for transcribe_dna_to_rna.'''
	assert 'GAUGGAACUUGACUACGUAAAUU' == transcribe_dna_to_rna('GATGGAACTTGACTACGTAAATT')


def main():
	'''Main runner, to read data, compute and saves output.'''
	with open(os.path.join(os.path.dirname(__file__), 'data/rosalind_rna.txt')) as input:
		dna = input.readline().strip()

	rna = transcribe_dna_to_rna(dna)
		
	with open(output_path(__file__), 'w') as output:
		output.write(rna)


if __name__ == '__main__':
	main()