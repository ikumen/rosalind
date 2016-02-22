#!/usr/bin/env python

'''
bs_fibd.py: Mortal Fibonacci Rabbits (http://rosalind.info/problems/fibd/) 

Problem: Recall the definition of the Fibonacci numbers from “Rabbits and 
Recurrence Relations”, which followed the recurrence relation Fn=Fn−1+Fn−2 
and assumed that each pair of rabbits reaches maturity in one month and 
produces a single pair of offspring (one male, one female) each subsequent month.

Our aim is to somehow modify this recurrence relation to achieve a dynamic programming 
solution in the case that all rabbits die out after a fixed number of months. See 
Figure 4 for a depiction of a rabbit tree in which rabbits live for three months 
(meaning that they reproduce only twice before dying).

Given: Positive integers n≤100 and m≤20.
Return: The total number of pairs of rabbits that will remain after the n-th 
month if all rabbits live for m months.

Sample Dataset: 
6 3

Sample Output:
4

3 months life cycle
1: 1a(born)
2: 1a(mate:1b)
3: 2 -> 1a(mate:1c) + 1b(born)
4: 2 -> 1b(mate:1d) + 1c(born) [-1a]
5: 3 -> 1b(mate:1e) + 1c(mate:1f) + 1d (born)
6: 4 -> 1c(mate:1g) + 1d(mate:1h) + 1e (born) + 1f (born) [-1b]
7: 5 -> 1d(mate:1i) + 1e(mate:1j) + 1f (mate:1k) + 1g (born) + 1h (born)
8: 7 -> 1e(mate:1L) + 1f(mate:1m) + 1g(mate:1n) + 1h(mate:1o) + 1i(born) + 1j(born) + 1k(born)

'''
import os
import pytest

from helpers import output_path


def fibd(n, m):
	pairs = [1]+[0] * (m-1)
	for i in range(n-1):
		# all pairs not in the last month (m) will be alive next month, basically
		# we end up shifting them right 1 index in the pairs array
		alive = pairs[:-1]
		# all pairs not in first month are mature, and mate
		matings = sum(pairs[1:])
		# pairs for the next month are: [new babies] + [alive]
		pairs = [matings] + alive
	return sum(pairs)


def test_fibd():
	# alive for only 1 month
	assert 1 == fibd(1, 2)
	# alive for 2 months
	assert 0 == fibd(3, 1)
	assert 1 == fibd(1, 4)
	assert 2 == fibd(3, 4)
	assert 3 == fibd(4, 4)
	assert 4 == fibd(5, 4)
	assert 9 == fibd(7, 4)
	# alive for 3 months
	assert 1 == fibd(2, 3)
	assert 4 == fibd(6, 3)
	assert 7 == fibd(8, 3)


def main():
	'''Main runner, to read data, compute and saves output.'''
	with open(os.path.join(os.path.dirname(__file__), 'data/rosalind_fibd.txt')) as input:
		n, m = map(int, input.readline().split())

	results = fibd(n, m)

	with open(output_path(__file__), 'w') as output:
		output.write(str(results))


if __name__ == '__main__':
	main()