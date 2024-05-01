
# -------------------------------------------------------------------------------------------------------------------
# This code extracts the interacting proteins along with their corresponding taxids from the IntAct database.

# Input - The IntAct database stored in 'PPII/Input/IntAct_Database.txt'.
# Output - The reduced IntAct database stored in 'PPII/Reduced_IntAct/Reduced_IntAct.txt'.
# -------------------------------------------------------------------------------------------------------------------

#!/usr/bin/env python
import re

def main():
	fp_write = open('../Reduced_IntAct/Reduced_IntAct.txt','w') # Output File

	with open('../Input/IntAct_Database.txt') as fp: # Input File
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