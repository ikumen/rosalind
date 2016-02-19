#!/usr/bin/env python

'''
pv_ini3.py: Strings and Lists

Given: A string s of length at most 200 letters and four integers a, b, c and d.
Return: The slice of this string from indices a through b and c through d 
(with space in between), inclusively.

Sample Dataset:
HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.
22 27 97 102

Sample Output:
Humpty Dumpty
'''
import os
import pytest

from helpers import output_path


def slices(s, begin1, end1, begin2, end2):
	'''Rerturns slices of 's' at begin1-end1 and begin2-end2.'''
	return [s[begin1:end1+1], s[begin2:end2+1]]


def test_slices():
	'''Test for slices function.'''
	results = slices('HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain',
		22, 27, 97, 102)
	assert 'Humpty Dumpty' == ' '.join(results)


def main():
	'''Main runner, to read data, compute and saves output.'''
	# read in data
	with open(os.path.join(os.path.dirname(__file__), 'data/rosalind_ini3.txt')) as input:
		s, indices = [line.strip() for line in input.readlines()]
		b1, e1, b2, e2 = [int(n) for n in indices.split()]
		
	with open(output_path(__file__), 'w') as output:
		output.write(' '.join(slices(s, b1, e1, b2, e2)))


if __name__ == '__main__':
	main()