
# ---------------------------------------------------------------------------------------------------------------------------
# This code generates the obsolute proteins as per GO database whose GO hierarchy for any ontology does not exist. 

# Input - The GO hierarchies of the PLG proteins saved in 'GO/Individual_Clusters_GO_Hierarchies/'. 
# Output - The GO obsolute proteins saved in 'GO/Obsolute_Proteins/GO_Obsolute.txt'.
# ---------------------------------------------------------------------------------------------------------------------------

import re
import urllib,urllib2
import requests
import time 
import numpy as np
import pickle
import copy
import random
import os

def main():
	ReadFolder = '../Individual_Clusters_GO_Hierarchies/' # Input Folder
	# write_file = 'binary.tsv'
	check_file = '../Obsolute_Proteins/GO_Obsolute.txt' # Output File
	check_write = open(check_file,'w')
	# fp_write = open(write_file,'w')
	# fp_write.write('Protein_No' + '\t' + 'UniProt_Acc' + '\t' + 'Cluster_No' + '\t' + 'BP' + '\t' + 'MF' + '\t' + 'CC' + '\n')
	count_protein = 1
	start_count = 1
	end_count = 125 # Input the count of the clusters
	bp = 0
	mf = 0
	cc = 0

	while start_count <= end_count:
		filename = ReadFolder + str(start_count) + '.txt'
		with open(filename) as fp:
			for ln in fp:
				bp = 0
				mf = 0
				cc = 0
				ln = ln.replace('\n','')
				if ln != '':
					word = ln.split('\t')
					i = 1
					for i in range(len(word)):
						word1 = word[i].split(',')
						# print word1
						if word1[int(len(word1))-2] == 'GO:0008150':
							bp = 1
						elif word1[int(len(word1))-2] == 'GO:0003674':
							mf = 1
						elif word1[int(len(word1))-2] == 'GO:0005575':
							cc = 1
					if bp == 0 and mf == 0 and cc == 0:
						check_write.write(str(word[0])+'\n')
					# fp_write.write(str(count_protein) + '\t' + str(word[0]) + '\t' + str(start_count) + '\t' + str(bp) + '\t' + str(mf) + '\t' + str(cc) + '\n')
					count_protein += 1
		start_count += 1
	# fp_write.close()
	filename = ReadFolder + 'Single_Node.txt' # Input File - Single_Node Clusters
	with open(filename) as fp:
		for ln in fp:
				bp = 0
				mf = 0
				cc = 0
				ln = ln.replace('\n','')
				if ln != '':
					word = ln.split('\t')
					i = 1
					for i in range(len(word)):
						word1 = word[i].split(',')
						# print word1
						if word1[int(len(word1))-2] == 'GO:0008150':
							bp = 1
						elif word1[int(len(word1))-2] == 'GO:0003674':
							mf = 1
						elif word1[int(len(word1))-2] == 'GO:0005575':
							cc = 1
					if bp == 0 and mf == 0 and cc == 0:
						check_write.write(str(word[0])+'\n')
					# fp_write.write(str(count_protein) + '\t' + str(word[0]) + '\t' + str(start_count) + '\t' + str(bp) + '\t' + str(mf) + '\t' + str(cc) + '\n')
					count_protein += 1
		start_count += 1
	check_write.close()


#---------------------------------------------------------------------------------------

if __name__=='__main__':
	main()
