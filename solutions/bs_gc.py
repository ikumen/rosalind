#!/usr/bin/env python

'''
bs_gc.py: Computing GC Content (http://rosalind.info/problems/gc/)

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
Return: The ID of the string having the highest GC-content, followed by the 
GC-content of that string. Rosalind allows for a default error of 0.001 in all 
decimal answers unless otherwise stated; please see the note on absolute error below.

Sample Dataset:
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT

Sample Output:
Rosalind_0808
60.919540
'''
import sys
import os
import pytest

from collections import Counter
from helpers import parse_fasta, output_path


def compute_gc_content(dna):
	'''Computes the gc content of a given dna string.'''
	cntr = Counter(dna)
	gc = sum([cntr[base] for base in ['G','C']])
	return (gc / len(dna)) * 100


def highest_gc(dnas):
	'''Computes the GC for each dna item from dnas list, and returns the 
	highest GC and id of dna item it came from.'''
	hi_gc = None
	for dna in dnas:
		gc = compute_gc_content(dna['dna'])
		if not hi_gc or hi_gc['gc'] < gc:
			hi_gc = {
				'id': dna['id'],
				'gc': gc
			}
	return hi_gc


def test_highest_gc():
	'''Only tests the highest_gc and compute_gc_content methods, 
	does not test loading the fasta file.
	'''
	dnas = [
		{'id':'Rosalind_6404','dna':'CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG'},
		{'id':'Rosalind_5959','dna':'CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC'},
		{'id':'Rosalind_0808','dna':'CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT'}
	]
	hi_gc = highest_gc(dnas)
	assert 'Rosalind_0808' == hi_gc['id']
	assert 60.91954022988506 == hi_gc['gc']



def main():
	'''Main runner, to read data, compute and saves output.'''
	sequences = parse_fasta(os.path.join(os.path.dirname(__file__), 'data/rosalind_gc.txt'))
	hi_gc = highest_gc(sequences)

	with open(output_path(__file__), 'w') as output:
		output.write(hi_gc['id'] + '\n')
		output.write(str(hi_gc['gc']))


if __name__ == '__main__':
	main()
	
	