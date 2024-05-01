
# -------------------------------------------------------------------------------------------------------------------
# This code generates the pickle files for nodes and edges of PLG.

# Input - The PLG stored in 'PLG/PLG.txt'. 
# Output - The pickle file for nodes saved in 'PLG_Clustering/Intermediate_Files/Nodes_PLG.pickle'.
#		   The pickle file for edges saved in 'PLG_Clustering/Intermediate_Files/Edges_PLG.pickle'.
# -------------------------------------------------------------------------------------------------------------------

from __future__ import division
import random
import Queue
from operator import itemgetter
from copy import deepcopy
import math

def main():
	fp = open("../../PLG_Filtering/Filtered_PLG/Edges.txt") # Input File
	nodes = set() # node bookkeeping
	for i in fp.readlines():
		i = i.replace('\n','')
		line = i.split('\t')
		nodes.add(line[0])
		nodes.add(line[1])
	fp.close()

	edges = dict.fromkeys(list(nodes)) # edge bookkeeping
	fp = open("../../PLG_Filtering/Filtered_PLG/Edges.txt") # Input File
	for i in fp.readlines():
		line = i.split('\t')
		if line[0] == line[1]:
			continue
		if edges[line[0]] == None :
			edges[line[0]] = [(line[1],float(line[2].strip("\n")))]
		else:
			edges[line[0]].append((line[1],float(line[2].strip("\n"))))
		
		if edges[line[1]] == None :
			edges[line[1]] = [(line[0],float(line[2].strip("\n")))]
		else:
			edges[line[1]].append((line[0],float(line[2].strip("\n"))))
	fp.close()

	# store data as object
	import pickle
	with open('../Intermediate_Files/Nodes_PLG.pickle', 'wb') as f: # Output File 
		pickle.dump(nodes, f)
	with open('../Intermediate_Files/Edges_PLG.pickle', 'wb') as f1: # Output File 
		pickle.dump(edges, f1)

	return
if __name__ == '__main__':
	main()
