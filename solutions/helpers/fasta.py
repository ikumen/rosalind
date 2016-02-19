#!/usr/bin/env python

import os
import pytest

def parse_fasta(fasta_path):
	'''Parses a FASTA format file into list of sequence objects with id 
	and dna sequence, ie [{id: ..., dna: ...}, ...].
	'''
	sequences = [] 
	with open(fasta_path) as input:
		id = None,	# identifier of each sequence 
		dna = ''	# dna sequence string to build as we parse
		while True:
			line = input.readline().strip()

			# reached the file or end of current sequence, 
			# time to write it out the sequence
			if not line or line[0] == '>':
				# but only do so if there's something to write out
				if id and dna: 
					sequences.append({
						'id': id.lstrip('>'), # truncate leading '>'
						'dna': dna 
					})

				# after everything is written, and it's eof, lets stop
				if not line:
					break

				# reset set everything and get new id
				else:
					dna = ''
					id = line

			# still on current sequence
			else:
				dna += line

	return sequences 


def test_parse_fasta():
	fasta_path = os.path.join(os.path.dirname(__file__), 'data/fasta_test_data.txt')
	sequences = parse_fasta(fasta_path)
	print(sequences)
	assert sequences[0]['id'] == 'Rosalind_6404'
	assert sequences[0]['dna'] == 'CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG'
	assert sequences[1]['id'] == 'Rosalind_5959'
	assert sequences[1]['dna'] == 'CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC'
	assert sequences[2]['id'] == 'Rosalind_0808'
	assert sequences[2]['dna'] == 'CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT'

