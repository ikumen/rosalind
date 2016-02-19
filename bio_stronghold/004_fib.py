#!/usr/bin/env python

'''
004_fib.py: http://rosalind.info/problems/fib/

Given: Positive integers n≤40n≤40 and k≤5k≤5.
Return: The total number of rabbit pairs that will be present after nn months if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of kk rabbit pairs (instead of only 1 pair).

Sample Dataset:
5 3

Sample Output:
19
'''
import sys
import pytest

"""
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144

1: 1 - born
2: 1 - mate
3: 4   (1 -> 3a)
4: 7   (1 -> 3b) + 3a
5: 19  (1 -> 3c) + (3a -> 9a) + 3b
6: 40  (1 -> 3d) + (3a -> 9b) + (3b -> 9) + 9a + 3c
"""

def fib(n, k):
	if n == 0: 
		return 0
	elif n == 1 or n == 2:
		return 1
	else:
		return fib(n-1, k) + k * fib(n-2, k)


def test_fib():
	assert 19 == fib(5, 3)


def main():
	'''Main runner, to read data, compute and saves output.'''
	# rediret stdout to our output file
	#sys.stdout = open('output/.txt', 'w')

	with open('data/rosalind_fib.txt') as input:
		n, k = (input.readline().strip()).split()
		n, k = map(int, [n, k])
		
		#print(fib(n, k))

	with open('output/fib.txt', 'w') as output:
		output.write(str(fib(n, k)))


if __name__ == '__main__':
	main()