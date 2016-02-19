#!/usr/bin/env python

'''
.py: http://rosalind.info/problems// 
'''
import os
import pytest


def test_():


def main():
	'''Main runner, to read data, compute and saves output.'''
	basepath = os.path.dirname(__file__)

	with open(os.path.join(basepath, 'data/rosalind_.txt')) as input:
		s = input.readline()		


	with open(os.path.join(basepath, 'output/.txt'), 'w') as output:
		output.write()


if __name__ == '__main__':
	main()