#!/usr/bin/env python

'''
.py: http://rosalind.info/problems// 
'''
import os
import pytest

from helpers import output_path


def test_():
	'''Test'''

def main():
	'''Main runner, to read data, compute and saves output.'''
	with open(os.path.join(os.path.dirname(__file__), 'data/rosalind_.txt')) as input:
		s = input.readline()		


	with open(output_path(__file__), 'w') as output:
		output.write()


if __name__ == '__main__':
	main()