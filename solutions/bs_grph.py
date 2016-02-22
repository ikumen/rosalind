#!/usr/bin/env python

'''
bs_grph.py: Overlap Graphs (http://rosalind.info/problems/grph/)

Problem: A graph whose nodes have all been labeled can be represented by an 
adjacency list, in which each row of the list contains the two node labels 
corresponding to a unique edge. A directed graph (or digraph) is a graph 
containing directed edges, each of which has an orientation. That is, a 
directed edge is represented by an arrow instead of a line segment; the 
starting and ending nodes of an edge form its tail and head, respectively. 
The directed edge with tail v and head w is represented by (v,w)(v,w) (but 
not by (w,v)(w,v)). A directed loop is a directed edge of the form (v,v)(v,v).

For a collection of strings and a positive integer kk, the overlap graph for 
the strings is a directed graph OkOk in which each string is represented by 
a node, and string ss is connected to string tt with a directed edge when there 
is a length k suffix of s that matches a length kk prefix of tt, as long as s≠t; 
we demand s≠ts≠t to prevent directed loops in the overlap graph (although 
directed cycles may be present).

Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.
Return: The adjacency list corresponding to O3. You may return edges in any order.

Sample Dataset:
>Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG

Sample Output:
Rosalind_0498 Rosalind_2391
Rosalind_0498 Rosalind_0442
Rosalind_2391 Rosalind_2323
'''
import os
import pytest

from helpers import output_path, parse_fasta


def adjaceny_list(sequences, k):
	adj_list = []
	for s in sequences:
		for t in sequences:
			if s != t and s['dna'][-k:] == t['dna'][:k]:
				adj_list.append(s['id'] + ' ' + t['id'])
	return adj_list

def test_adj_list():
	sequences = [
		{'id': 'Rosalind_0498', 'dna':'AAATAAA'}, 
		{'id': 'Rosalind_2391', 'dna':'AAATTTT'},
		{'id': 'Rosalind_2323', 'dna':'TTTTCCC'},
		{'id': 'Rosalind_0442', 'dna':'AAATCCC'},
		{'id': 'Rosalind_5013', 'dna':'GGGTGGG'}]
	
	adj_list = adjaceny_list(sequences, 3)

	assert 'Rosalind_0498 Rosalind_2391' in adj_list 
	assert 'Rosalind_0498 Rosalind_0442' in adj_list 
	assert 'Rosalind_2391 Rosalind_2323' in adj_list 


def main():
	'''Main runner, to read data, compute and saves output.'''
	sequences = parse_fasta(os.path.join(os.path.dirname(__file__), 'data/rosalind_grph.txt'))
	adj_list = adjaceny_list(sequences, 3)

	with open(output_path(__file__), 'w') as output:
	 	output.write('\n'.join(adj_list))


if __name__ == '__main__':
	main()