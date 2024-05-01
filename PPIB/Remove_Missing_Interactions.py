
# -------------------------------------------------------------------------------------------------------------------
# This code removes the missing PPIs from the BioGRID database.

# Input - The E. coli PPIs after replacing genes by proteins stored in 'PPIB/Intermediate_Files/Genes_Exchanged_Proteins.txt'.
# Output - Valid PPIs for E. coli extracted from BioGRID stored in 'PPIB/Interactions_Ecoli/Ecoli_PPIs.txt'.
# -------------------------------------------------------------------------------------------------------------------

#!/usr/bin/env python

import re

def main():
	fp_write = open('../Interactions_Ecoli/Ecoli_PPIs.txt','w') # Output File
	fp_write1 = open('../Interactions_Ecoli/Ecoli_PPIs_Processing.txt','w') # Output File
	fp_write1.write('\n')
	with open('../Intermediate_Files/Genes_Exchanged_Proteins.txt', 'r') as fp: # Input File
		for ln in fp:
			if '\n' in ln:
				ln = ln[:-1]
			word = re.split(r'\t+',ln)
			if len(word[1]) > 1:
				fp_write.write('uniprotkb:'+word[0]+'\t'+'uniprotkb:'+word[1]+'\n')
				fp_write1.write('uniprotkb:'+word[0]+'\t'+'uniprotkb:'+word[1]+'\n')
	fp_write.close()
	fp_write1.close()

#---------------------------------------------------------------------------------------

if __name__=='__main__':
	main()
