
# -------------------------------------------------------------------------------------------------------------------
# This code places UniProt IDs in place of the gene IDs in Ecoli PPIs from BioGRID.

# Input - Nodecount of PPIB stored in 'PPIB/Intermediate_Files/noOfNodes.txt'.
#		  Nodes of PPIB stored in 'PPIB/Nodes_BioGRID'.
# Output - Genes replaced by proteins in the PPIs and saved in 'PPIB/Intermediate_Files/Genes_Exchanged_Proteins.txt'.
# -------------------------------------------------------------------------------------------------------------------

#!/usr/bin/env python

import re

def main():
	count = 0
	with open('../Intermediate_Files/noOfNodes.txt', 'r') as f: # Input File
		first_line = f.readline()
	print first_line
	fp_write = open('../Intermediate_Files/Genes_Exchanged_Proteins.txt','w') # Output File
	while count<int(first_line):	
		filename = '../Nodes_BioGRID/'+str(count)+'.txt' # Input Folder
		with open(filename) as fp:
			flag = 0
			for ln in fp:
				if 'entryID' in ln:
					word = ln.split('=')
					word1 = word[1].split(' ')
					word2 = word1[0]
					word2 = word2[1:-1]
					fp_write.write(word2+'\t')
					flag =1
			if flag == 0:
				fp_write.write('\t')
		count += 1
		filename = '../Nodes_BioGRID/'+str(count)+'.txt' # Input Folder
		with open(filename) as fp1:
			flag1 = 0
			for ln1 in fp1:
				if 'entryID' in ln1:
					word = ln1.split('=')
					word1 = word[1].split(' ')
					word2 = word1[0]
					word2 = word2[1:-1]
					fp_write.write(word2+'\n')
					flag1 = 1
			if flag1 == 0:
				fp_write.write('\n')
		count += 1
			
	fp_write.close


#---------------------------------------------------------------------------------------

if __name__=='__main__':
	main()