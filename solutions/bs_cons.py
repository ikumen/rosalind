
#!/usr/bin/env python

'''
bs_cons.py: Consensus and Profile (http://rosalind.info/problems/cons/)

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
Return: A consensus string and profile matrix for the collection. (If several possible 
consensus strings exist, then you may return any one of them.)
'''
import os
import pytest


#def test_():


def main():
	'''Main runner, to read data, compute and saves output.'''
	basepath = os.path.dirname(__file__)

#	with open(os.path.join(basepath, 'data/rosalind_.txt')) as input:
#		s = input.readline()		


#	with open(os.path.join(basepath, 'output/.txt'), 'w') as output:
#		output.write()


if __name__ == '__main__':
	main()