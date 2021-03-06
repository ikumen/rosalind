#!/usr/bin/env python

'''
pv_ini4.py: Conditions and Loops

Given: Two positive integers a and b (a<b<10000).
Return: The sum of all odd integers from a through b, inclusively.

Sample Dataset:
100 200

Sample Output:
7500
'''
import os
import pytest

from helpers import output_path


def sum_all_odds(a, b):
	'''sums all odd integers from a to b.'''
	sum = 0
	for i in range(a, b+1):
		sum = sum + ((i % 2) * i)
	return sum


def test_sum_all_odds():
	'''Test for sum_all_odds.'''
	assert 7500 == sum_all_odds(100, 200)


def main():
	'''Main runner, to read data, compute and saves output.'''
	# read in data
	with open(os.path.join(os.path.dirname(__file__), 'data/rosalind_ini4.txt')) as input:
		a, b = [int(n) for n in input.read().split()]

	with open(output_path(__file__), 'w') as output:
		output.write(str(sum_all_odds(a, b)))


if __name__ == '__main__':
	main()