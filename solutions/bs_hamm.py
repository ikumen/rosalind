#!/usr/bin/env python

'''
bs_hamm.py: Counting Point Mutations (http://rosalind.info/problems/hamm/)

Problem: Given two strings s and t of equal length, the Hamming distance 
between s and t, denoted dH(s,t)dH(s,t), is the number of corresponding symbols 
that differ in s and t.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
Return: The Hamming distance dH(s,t)dH(s,t).

Sample Dataset:
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT

Sample Output:
7
'''
import os
import pytest

from helpers import output_path


def hamming_distance(dna1, dna2):
	distance = 0
	for i in range(0, len(dna1)):
		if dna1[i] != dna2[i]:
			distance += 1
	return distance


def test_hamming_distance():
	distance = hamming_distance('GAGCCTACTAACGGGAT', 'CATCGTAATGACGGCCT')
	assert 7 == distance


def main():
	'''Main runner, to read data, compute and saves output.'''
	with open(os.path.join(os.path.dirname(__file__), 'data/rosalind_hamm.txt')) as input:
		dna1, dna2 = [line.strip() for line in input.readlines()]

	distance = hamming_distance(dna1, dna2)

	with open(output_path(__file__), 'w') as output:
		output.write(str(distance))


if __name__ == '__main__':
	main()