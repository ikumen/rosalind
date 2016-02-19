#!/usr/bin/env python

""".py: """
import sys
import pytest


def test_():


def main():
	'''Main runner, to read data, compute and saves output.'''
	# rediret stdout to our output file
	#sys.stdout = open('output/.txt', 'w')

	with open('data/rosalind_ini.txt') as input:
		s = input.readline()		


	with open('output/.txt', 'w') as output:
		output.write()


if __name__ == '__main__':
	main()