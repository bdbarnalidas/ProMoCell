
# -------------------------------------------------------------------------------------------------------------------
# This code extracts the protein-protein interactions for E. coli from the BioGRID database.

# Input - The BioGRID database stored in 'PPIB/Input/BioGRID_Database.txt'.
# Output - PPIs for E. coli extracted from BioGRID stored in 'PPIB/Intermediate_Files/Ecoli_PPIs.txt'.
# -------------------------------------------------------------------------------------------------------------------

#!/usr/bin/env python

import re

def main():
	fp_write = open('../Intermediate_Files/Ecoli_PPIs.txt','w') # Output File
	count = 0
	with open('../Input/BioGRID_Database.txt') as fp: # Input File
		for ln in fp:
			word = re.split(r'\t+',ln)	
			if 'taxid:511145' in word[9] or 'taxid:511145' in word[10]: # Provide the taxid of the organism
				fp_write.write(word[0]+'\t'+word[1]+'\t'+word[9]+'\t'+word[10]+'\n')
				count += 1
				# print count
	fp_write.close()


#---------------------------------------------------------------------------------------

if __name__=='__main__':
	main()
