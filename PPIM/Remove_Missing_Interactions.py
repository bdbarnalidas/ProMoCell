
# -------------------------------------------------------------------------------------------------------------------
# This code removes the missing interactions from the MINT database and extracts only the binary interaction 
# information along with their taxids.

# Input - The MINT database stored in 'PPIM/Input/MINT_Database.txt'.
# Output - The reduced MINT database stored in 'PPIM/Reduced_MINT/Reduced_MINT.txt'.
# -------------------------------------------------------------------------------------------------------------------

#!/usr/bin/env python
import re

def main():
	fp_write = open('../Reduced_MINT/Reduced_MINT.txt','w') # Output File

	with open('../Input/MINT_Database.txt') as fp: # Input File
		for ln in fp:
			word = re.split(r'\t+',ln)	
			if 'uniprotkb' in word[0] and 'uniprotkb' in word[1]:
				fp_write.write(word[0])
				fp_write.write('\t')
				fp_write.write(word[1])
				fp_write.write('\t')
				fp_write.write(word[9])
				fp_write.write('\t')
				fp_write.write(word[10])
				fp_write.write('\n')
	fp_write.close()

#---------------------------------------------------------------------------------------

if __name__=='__main__':
	main()