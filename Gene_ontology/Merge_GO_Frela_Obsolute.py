
# ---------------------------------------------------------------------------------------------------------------------------
# This code merges the obsolute information of GO and Frela into one single file for future processing.

# Input - The list of obsolute proteins as per Frela stored in 'GO/Obsolute_Proteins/Frela_Obsolute.txt'.
#		  The list of obsolute proteins as per GO stored in 'GO/Obsolute_Proteins/GO_Obsolute.txt'.
# Output - The final list of obsolute proteins as per GO and Frela saved in 'GO/Obsolute_Proteins/GO_Frela_Obsolute.txt'.
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
	file1 = '../Obsolute_Proteins/Frela_Obsolute.txt' # Data not available in Frela for any ontology
	file2 = '../Obsolute_Proteins/GO_Obsolute.txt' # Data not available in GO database for any ontology
	file3 = '../Obsolute_Proteins/GO_Frela_Obsolute.txt' # Data of those proteins which has to be removed from further analysis
	fp_write = open(file3,'w')
	visited = []
	with open(file1) as fp:
		for ln in fp:
			ln = ln.replace('\n','')
			if ln not in visited:
				visited.append(ln)
	with open(file2) as fp:
		for ln in fp:
			ln = ln.replace('\n','')
			if ln not in visited:
				visited.append(ln)
	for i in range(len(visited)):
		fp_write.write(str(visited[i]) + '\n')
	fp_write.close()

#---------------------------------------------------------------------------------------

if __name__=='__main__':
	main()