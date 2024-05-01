
# ---------------------------------------------------------------------------------------------------------------------------
# This code removes the obsolute proteins from all the clusters.

# Input - Individual cluster information saved in 'GO/Individual_Clusters'.
# Output - The modified clusters saved in 'GO/Clusters_After_Removing_Obsolute_Proteins'.
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
	ReadFolder = '../Individual_Clusters' # Input Folder
	WriteFolder = '../Clusters_After_Removing_Obsolute_Proteins' # Output Folder
	start_count = 1
	end_count = 124
	ReadFile = '../Obsolute_Proteins/GO_Frela_Obsolute.txt' # Input File - Proteins to be removed from the clusters
	remove = []
	count_valid = 0
	count_total = 0
	with open(ReadFile) as fp:
		for ln in fp:
			ln = ln.replace('\n','')
			remove.append(ln)
	# print len(remove)
	while start_count <= end_count:
		# print start_count
		Read_filename = ReadFolder + '/' + str(start_count) + '.txt'
		Write_filename = WriteFolder + '/' + str(start_count) + '.txt'
		fp_write = open(Write_filename,'w')
		with open(Read_filename) as fp:
			for ln in fp:
				ln = ln.replace('\n','')
				if ln != '':
					count_total += 1
					if ln in remove:
						continue
					else:
						fp_write.write(ln + '\n')
						count_valid += 1
		fp_write.close()
		start_count += 1

	Read_filename = '../../PLG_Clustering/MCL_Clusters/Single_Node_Clusters.txt' # Input File - Single Node Clusters
	Write_filename = WriteFolder + '/' + 'Single_Node' + '.txt'
	fp_write = open(Write_filename,'w')
	with open(Read_filename) as fp:
		for ln in fp:
			ln = ln.replace('\n','')
			if ln != '':
				count_total += 1
				if ln in remove:
					continue
				else:
					fp_write.write(ln+'\n')
					count_valid += 1
	fp_write.close()
		
	# print count_total
	# print count_valid

#---------------------------------------------------------------------------------------

if __name__=='__main__':
	main()