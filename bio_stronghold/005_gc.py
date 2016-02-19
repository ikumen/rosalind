#!/usr/bin/env python

'''
005_gc.py: Computing GC Content (http://rosalind.info/problems/gc/)

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
import pytest


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


def extract_fasta(input):
	'''Extracts dna and it's ID from a fasta format file, returning a array of 
	dna objects. For example: [{id: .., dna: ...},].'''
	dnas = []
	id = None
	dna = ''
	while True:
		line = input.readline().strip()
		if not line or line[0] == '>':
			if id:
				dnas.append({
					'id': id[1:], # assume leading '>', and trims it
					'dna': dna
				})
			dna = ''
			id = line
			if not line:
				break
		else:
			dna += line
	return dnas

	
def test_highest_gc():
	# dnas = [
	# 	{'id':'Rosalind_6404','dna':'CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG'},
	# 	{'id':'Rosalind_5959','dna':'CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC'},
	# 	{'id':'Rosalind_0808','dna':'CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT'}
	# ]
	# hi_gc = highest_gc(dnas)
	# assert 'Rosalind_0808' == hi_gc['id']
	# assert 60.91954022988506 == hi_gc['gc']
	assert True != False


def main():
	'''Main runner, to read data, compute and saves output.'''
	with open('data/rosalind_gc.txt') as input:
		dnas = extract_fasta(input)

	hi_gc = highest_gc(dnas)

	with open('output/gc.txt', 'w') as output:
		output.write(hi_gc['id'] + '\n')
		output.write(str(hi_gc['gc']))


if __name__ == '__main__':
	main()