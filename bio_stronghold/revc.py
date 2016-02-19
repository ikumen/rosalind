#!/usr/bin/env python

"""
revc.py: Complementing a Strand of DNA

Problem: In DNA strings, symbols 'A' and 'T' are complements of each other, as 
are 'C' and 'G'. The reverse complement of a DNA string s is the string s^c 
formed by reversing the symbols of ss, then taking the complement of each 
symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.
Return: The reverse complement s^c of s.

Sample Dataset:
AAAACCCGGT

Sample Output:
ACCGGGTTTT
"""
import sys
import pytest


def reverse_compliment(dna):
	compliments = dna.maketrans('ACGT', 'TGCA')
	return dna.translate(compliments)[::-1]


def test_reverse_compliment():
	assert 'ACCGGGTTTT' == reverse_compliment('AAAACCCGGT')


def main():
	'''Main runner, to read data, compute and saves output.'''
	# rediret stdout to our output file
	#sys.stdout = open('output/.txt', 'w')

	with open('data/rosalind_revc.txt') as input:
		dna = input.readline().strip()
		
	with open('output/revc.txt', 'w') as output:
		output.write(reverse_compliment(dna))


if __name__ == '__main__':
	main()