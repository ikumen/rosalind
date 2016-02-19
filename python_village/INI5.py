#!/usr/bin/env python

'''
INI5.py: Working with Files

Given: A file containing at most 1000 lines.
Return: A file containing all the even-numbered lines from the original file. 
Assume 1-based numbering of lines.

Sample Dataset:
Bravely bold Sir Robin rode forth from Camelot
Yes, brave Sir Robin turned about
He was not afraid to die, O brave Sir Robin
And gallantly he chickened out
He was not at all afraid to be killed in nasty ways
Bravely talking to his feet
Brave, brave, brave, brave Sir Robin
He beat a very brave retreat

Sample Output:
Yes, brave Sir Robin turned about
And gallantly he chickened out
Bravely talking to his feet
He beat a very brave retreat
'''
import os

def main():
	'''Main runner, to read data, compute and saves output.'''
	basepath = os.path.dirname(__file__)
	
	# read in data
	with open(os.path.join(basepath, 'data/rosalind_ini5.txt')) as input:
		lines = input.readlines()
				
	with open(os.path.join(basepath, 'output/ini5.txt'), 'w') as output:
		i = 0
		for line in lines:
			if i % 2 == 1:
				output.write(line)
			i += 1


if __name__ == '__main__':
	main()