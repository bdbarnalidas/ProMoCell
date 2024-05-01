
# -------------------------------------------------------------------------------------------------------------------
# This code extracts the unweighted edges of PPIM of E. coli.

# Input - The E. coli PPIs extracted from MINT stored in 'PPIM/Interactions_Ecoli/Ecoli_PPIs.txt'.
# Output - Unweighted edges of PPIM stored in 'PPIM/Nodes_Edges_PPIM/Unweighted_Edges.txt'.
# -------------------------------------------------------------------------------------------------------------------

#!/usr/bin/env python

def main():
	fp_write = open('../Nodes_Edges_PPIM/Unweighted_Edges.txt','w') # Output File
	with open('../Interactions_Ecoli/Ecoli_PPIs.txt') as fp: # Input File
		for ln in fp:
			if '\n' in ln:
				ln = ln[:-1]
			word = ln.split('\t')
			word1 = word[0].split(':')
			word2 = word[1].split(':')
			fp_write.write(word1[1]+'\t'+word2[1]+'\n')
	fp_write.close()

#---------------------------------------------------------------------------------------

if __name__=='__main__':
	main()