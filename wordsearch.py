#!/usr/bin/env python
import time
import argparse
import multiprocessing

#from multiprocessing.dummy import Pool as ThreadPool
from grid import Grid

#pool = ThreadPool(multiprocessing.cpu_count())
#results = pool.map(my_function, my_array)

"""
defines argument parser to take dimensions of the grid
"""
def get_user_input():
	parser = argparse.ArgumentParser(
		description='Please provide the dimensions of the grid')
	parser.add_argument(
		'x', metavar='int', type=int, default=10,
		help='x dimension')
	parser.add_argument(
		'y', metavar='int', type=int, default=10,
		help='y dimension')

	args = parser.parse_args()
	return args.x, args.y

if __name__ == '__main__':
	curtime = time.time()
	x, y = get_user_input()

	grid = Grid(x, y)
	# prints the grid to console.
	print('##### Word Grid #####')
	print(grid.to_text())

	print('##### Words #####')
	results = []
	for word in open('./words.txt'):
		word = word.strip('\n')
		if grid.search(word):
			results.append(word)

	print("Performed in {0} seconds".format(time.time() - curtime))
	print(results)




