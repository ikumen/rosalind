
#!/usr/bin/env python

'''
bs_cons.py: Consensus and Profile (http://rosalind.info/problems/cons/)

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
Return: A consensus string and profile matrix for the collection. (If several possible 
consensus strings exist, then you may return any one of them.)
'''
import os
import pytest

from helpers import output_path, parse_fasta


# maps of symbols and their corresponding index in profile matrix
sym_map = {'A':0, 'C':1, 'G':2, 'T':3}
profile_map = {0:'A', 1:'C', 2:'G', 3:'T'}

def concensus_string(matrix):
	'''Given a profile matrix, return the corresponding consensus string.
	Notes: each row of the matrix represents a symbols profile, with cols
	representing the counts. We need to scan each row, only taking the symbol
	with highest count.
	'''
	# dict holding sym+count info, to help us keep track of current highest
	# count and it's corresponding symbol. Initialize with 'A' profile to start
	consensus = [{'sym':'A','cnt':i} for i in matrix[0]]
	for r in range(1,4):
		for c in range(len(matrix[0])):
			if consensus[c]['cnt'] < matrix[r][c]:
				consensus[c]['sym'] = profile_map[r]
				consensus[c]['cnt'] = matrix[r][c]
	# ultimately we only want the symbol associated with each high count
	return ''.join([c['sym'] for c in consensus])

def profile_matrix(sequences):
	'''Given a list of dna sequences of equal lengths, return the profile matrix
	in the following format:
		[5, 1, 0, ..]
		[0, 0, 1, ..]
		...
	Each row corresponds to a symbol in the following order: ACGT
	'''
	rows = len(sequences)
	cols = len(sequences[0]['dna'])
	# initialize a 4xN matrix to hold the profile
	# where matrix[n] = n profile for ACGT 
	matrix = [[0] * cols for i in range(4)]
	for r in range(rows):
		for c in range(cols):
			sym = sequences[r]['dna'][c]
			matrix[sym_map[sym]][c] += 1
	return matrix
	


@pytest.fixture
def sample_matrix():
	return [[5, 1, 0, 0, 5, 5, 0, 0], [0, 0, 1, 4, 2, 0, 6, 1], 
		[1, 1, 6, 3, 0, 1, 0, 0], [1, 5, 0, 0, 0, 1, 1, 6]]


def test_profile_matrix(sample_matrix):
	sequences = [{'id':'Rosalind_1', 'dna':'ATCCAGCT'},
		{'id':'Rosalind_2', 'dna':'GGGCAACT'}, {'id':'Rosalind_3', 'dna':'ATGGATCT'},
		{'id':'Rosalind_4', 'dna':'AAGCAACC'}, {'id':'Rosalind_5', 'dna':'TTGGAACT'},
		{'id':'Rosalind_6', 'dna':'ATGCCATT'}, {'id':'Rosalind_7', 'dna':'ATGGCACT'}]
	matrix = profile_matrix(sequences)
	assert sample_matrix == matrix


def test_consensus_string(sample_matrix):
	consensus = concensus_string(sample_matrix)
	assert 'ATGCAACT' == consensus


def main():
	'''Main runner, to read data, compute and saves output.'''
	sequences = [{'id':'Rosalind_1', 'dna':'ATCCAGCT'},
		{'id':'Rosalind_2', 'dna':'GGGCAACT'}, {'id':'Rosalind_3', 'dna':'ATGGATCT'},
		{'id':'Rosalind_4', 'dna':'AAGCAACC'}, {'id':'Rosalind_5', 'dna':'TTGGAACT'},
		{'id':'Rosalind_6', 'dna':'ATGCCATT'}, {'id':'Rosalind_7', 'dna':'ATGGCACT'}]
	matrix = profile_matrix(sequences)
	print(matrix)

	sequences = parse_fasta(os.path.join(os.path.dirname(__file__), 'data/rosalind_cons.txt'))
	matrix = profile_matrix(sequences)
	consensus = concensus_string(matrix)
	# add symbol labels to the profile matrix for printing
	labeled_matrix = ['A:','C:','G:','T:']
	for i, row in enumerate(matrix):
		for col in row:
			labeled_matrix[i] += ' ' + str(col)

	with open(output_path(__file__), 'w') as output:
		output.write(consensus + '\n')
		output.write('\n'.join(labeled_matrix))


if __name__ == '__main__':
	main()