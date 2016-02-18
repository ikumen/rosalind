#!/usr/bin/env python

""".py: """
import sys
import pytest


def test_():
	'''Test for .'''


def main():
	'''Main runner, to read data, compute and saves output.'''
	# rediret stdout to our output file
	#sys.stdout = open('output/.txt', 'w')

	# read in data
	with open('data/rosalind_ini.txt') as input:
		s, indices = [line.strip() for line in input.readlines()]
		b1, e1, b2, e2 = [int(n) for n in indices.split()]
		

		
	with open('output/.txt', 'w') as output:
		output.write()


if __name__ == '__main__':
	main()