
# -------------------------------------------------------------------------------------------------------------------
# This code clusters PLG using Markov Cluster Algorithm.

# Input - The filtered PLG stored in 'PLG_Filtering/Filtered_PLG/Edges.txt'. 
# Output - The self-interacting single-node clusters saved in 'PLG_Clustering/MCL_Clusters/Single_Node_Clusters.txt'.
#		   The shared multi-node clusters saved in 'PLG_Clustering/MCL_Clusters/out.Shared_Edges.txt.I20'.
# -------------------------------------------------------------------------------------------------------------------

import numpy as np
import pickle
import os
def main():
	#load cluster data from pickle file
	fp = open("../Intermediate_Files/Edges_PLG.pickle") # Input File - Edges of PLG
	edges = pickle.load(fp)
	fp.close()
	mobile = []
	for i in edges:
		if edges[i] is None:
			mobile.append(i)
	fp = open("../../PLG_Filtering/Filtered_PLG/Edges.txt") # Input File - Filtered PLG
	#separated sigle node clusters
	fpMobile = open("../MCL_Clusters/Single_Node_Clusters.txt","w") # Output File
	fpNormal = open("../Intermediate_Files/Shared_Edges.txt","w") # Output File
	for i in fp.readlines():
		line = i.split('\t')
		if line[0] in mobile and line[1] in mobile and line[0]==line[1]:
			fpMobile.write(line[0]+"\n")
		else:
			fpNormal.write(i)
	fp.close()
	fpMobile.close()
	fpNormal.close()
	#calling MCL library
	os.system("mcl ../Intermediate_Files/Shared_Edges.txt --abc -I 1.969 -odir ../MCL_Clusters")
	fp = open("../MCL_Clusters/out.Shared_Edges.txt.I20")


	# make edge pickle
	newEdge = {}
	for i in edges:
		if edges[i] is not None:
			newEdge[i] = edges[i]
	# make node pickle
	newNode = set()
	for i in edges:
		if edges[i] is not None:
			newNode.add(i)
	# make nodeTocluster pickle	and cluster pickle
	clusters = {}
	nodeToCluster = {}
	lines = fp.readlines()
	for i in xrange(0,len(lines)):
		clArr = lines[i].split()
		clusters[i] = set(clArr)
		for j in clArr:
			nodeToCluster[j] = i
	#save pickle files
	with open('../MCL_Clusters/nodeToCluster.pickle', 'wb') as f: 
		pickle.dump(nodeToCluster, f)
	with open('../MCL_Clusters/clusters.pickle', 'wb') as f1: 
		pickle.dump(clusters, f1)
	with open('../MCL_Clusters/nodes.pickle', 'wb') as f: 
		pickle.dump(newNode, f)
	with open('../MCL_Clusters/edges.pickle', 'wb') as f1: 
		pickle.dump(newEdge, f1)
	return	
	
	
if __name__ == '__main__':
	main()
