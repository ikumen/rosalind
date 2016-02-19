#!/usr/bin/env python

'''
001_dna.py: DNA

Problem: A string is simply an ordered collection of symbols selected from some 
alphabet and formed into a word; the length of a string is the number of symbols 
that it contains. An example of a length 21 DNA string (whose alphabet contains 
the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string s of length at most 1000 nt.
Return: Four integers (separated by spaces) counting the respective number of 
times that the symbols 'A', 'C', 'G', and 'T' occur in s.

Sample Dataset:
AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC

Sample Output:
20 12 17 21
'''
import os
import sys
import pytest

def count_symbols(dna):
	counts = {}
	for symbol in dna:
		if symbol not in counts:
			counts[symbol] = 0
		counts[symbol] = counts[symbol] + 1
	return counts 


def test_count_symbols():
	'''Test for count_symbols.'''
	counts = count_symbols('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC')
	assert 20 == counts['A']
	assert 12 == counts['C']
	assert 17 == counts['G']
	assert 21 == counts['T']


def main():
	'''Main runner, to read data, compute and saves output.'''
	basepath = os.path.dirname(__file__)

	with open(os.path.join(basepath, 'data/rosalind_dna.txt')) as input:
		dna = input.readline().strip()
		dict_counts = count_symbols(dna)
		counts = [dict_counts[base] for base in 'ACGT']

	with open(os.path.join(basepath, 'output/dna.txt'), 'w') as output:
		output.write(' '.join(map(str, counts)))


if __name__ == '__main__':
	main()