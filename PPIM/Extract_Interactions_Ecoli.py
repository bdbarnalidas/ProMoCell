
# -------------------------------------------------------------------------------------------------------------------
# This code extracts the protein-protein interactions for E. coli from the reduced version of MINT database.

# Input - The reduced MINT database stored in 'PPIM/Reduced_MINT/Reduced_MINT.txt'.
# Output - PPIs for E. coli extracted from MINT stored in 'PPIM/Interactions_Ecoli/Ecoli_PPIs.txt'.
# -------------------------------------------------------------------------------------------------------------------

#!/usr/bin/env python

import re

def main():
	fp_write = open('../Interactions_Ecoli/Ecoli_PPIs.txt','w') # Output File
	fp_write1 = open('../Interactions_Ecoli/Ecoli_PPIs_Processing.txt','w') # Output File
	fp_write1.write('\n')
	with open('../Reduced_MINT/Reduced_MINT.txt') as fp: # Input File
		for ln in fp:
			word = re.split(r'\t+',ln)
			if 'taxid:83333' in word[2] or 'taxid:83333' in word[3]: # Provide the taxid of the organism
				fp_write.write(word[0])
				fp_write.write('\t')
				fp_write.write(word[1])
				fp_write.write('\n')
				fp_write1.write(word[0])
				fp_write1.write('\t')
				fp_write1.write(word[1])
				fp_write1.write('\n')
	fp_write.close()
	fp_write1.close()
	

#---------------------------------------------------------------------------------------

if __name__=='__main__':
	main()