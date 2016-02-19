#!/usr/bin/env python

import os

def output_path(f):
	'''Builds output path based on path of calling script. Assumes there's
	and output directory at the same level. 

	Given: 		'a/b/c/somefile.py'
	Returns: 	'a/b/c/output/somefile.txt'
	'''
	return os.path.join(os.path.dirname(f), 'output/' + os.path.splitext(os.path.basename(f))[0] + '.txt')


def test_output_path():
	assert 'a/b/c/output/somefile.txt' == output_path('a/b/c/somefile.py')
	assert 'a/b/c/output/somefile.txt' == output_path('a/b/c/somefile')