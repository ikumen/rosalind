#!/usr/bin/env python

'''
HAMM.py: Counting Point Mutations (http://rosalind.info/problems/hamm/)

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
	basepath = os.path.dirname(__file__)

	with open(os.path.join(basepath, 'data/rosalind_hamm.txt')) as input:
		dna1 = input.readline().strip()
		dna2 = input.readline().strip()		

	distance = hamming_distance(dna1, dna2)

	with open(os.path.join(basepath, 'output/hamm.txt'), 'w') as output:
		output.write(str(distance))


if __name__ == '__main__':
	main()