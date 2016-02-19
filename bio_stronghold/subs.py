#!/usr/bin/env python

"""
subs.py: Finding a Motif in DNA (http://rosalind.info/problems/subs/)

Problem: Given two strings s and t, t is a substring of s if t is contained as a 
contiguous collection of symbols in s (as a result, t must be no longer than s).
The position of a symbol in a string is the total number of symbols found to its 
left, including itself (e.g., the positions of all occurrences of 'U' in 
"AUGCUUCAGAAAGGUCUUACG" are 2, 5, 6, 15, 17, and 18). The symbol at position i of 
s is denoted by s[i]s[i].

A substring of s can be represented as s[j:k]s[j:k], where j and k represent the 
starting and ending positions of the substring in ss; for example, 
if s = "AUGCUUCAGAAAGGUCUUACG", then s[2:5]s[2:5] = "UGCU". The location of a 
substring s[j:k]s[j:k] is its beginning position j; note that t will have multiple 
locations in ss if it occurs more than once as a substring of ss (see the Sample below).

Given: Two DNA strings s and t (each of length at most 1 kbp).
Return: All locations of t as a substring of s.

Sample Dataset:
GATATATGCATATACTT
ATAT

Sample Output:
2 4 10
"""
import sys
import pytest


def find_motifs(dna, motif):
	'''Find all locations of motif as substring of dna.'''
	locations = []
	for i in range(0, len(dna)-len(motif)+1):
		if dna[i:i+len(motif)] == motif:
			locations.append(i+1) # account for 0 based index
	return locations


def test_find_motifs():
	locs = find_motifs('GATATATGCATATACTT', 'ATAT')
	assert [2, 4, 10] == locs


def main():
	'''Main runner, to read data, compute and saves output.'''
	with open('data/rosalind_subs.txt') as input:
		dna = input.readline().strip()
		motif = input.readline().strip()
		
	locs = find_motifs(dna, motif)

	with open('output/subs.txt', 'w') as output:
		output.write(' '.join(map(str, locs)))


if __name__ == '__main__':
	main()