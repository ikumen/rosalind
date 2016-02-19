#!/usr/bin/env python

'''
INI6.py: Dictionaries

Given: A string s of length at most 10000 letters.
Return: How many times any word occurred in string. Each letter case 
(upper or lower) in word matters. Lines in output can be in any order.

Sample Dataset:
We tried list and we tried dicts also we tried Zen

Sample Output:
and 1
We 1
tried 3
dicts 1
list 1
we 2
also 1
Zen 1
'''
import os
import pytest


def word_count(s):
	words = s.split(' ')
	counts = {}
	for w in words:
		if w not in counts:
			counts[w] = 0
		counts[w] = counts[w] + 1
	return counts


def test_word_count():
	'''Test for word_count.'''
	counts = word_count('We tried list and we tried dicts also we tried Zen')
	assert 1 == counts['and']
	assert 1 == counts['We']
	assert 2 == counts['we']
	assert 1 == counts['list']
	assert 3 == counts['tried']
	assert 1 == counts['Zen']


def main():
	'''Main runner, to read data, compute and saves output.'''
	basepath = os.path.dirname(__file__)
	
	# read in data
	with open(os.path.join(basepath, 'data/rosalind_ini6.txt')) as input:
		s = input.readline()
	
	counts = word_count(s)

	with open(os.path.join(basepath, 'output/ini6.txt'), 'w') as output:
		for key in counts.keys():
			output.write(key + ' ' + str(counts[key]) + '\n')


if __name__ == '__main__':
	main()



