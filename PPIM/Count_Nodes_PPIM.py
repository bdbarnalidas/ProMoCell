
# -------------------------------------------------------------------------------------------------------------------
# This code counts the number of unique nodes present in PPIM.

# Input - The E. coli PPIs extracted from MINT stored in 'PPIM/Interactions_Ecoli/Ecoli_PPIs.txt'.
# Output - Count of nodes of PPIM stored in 'PPIM/Interactions_Ecoli/noOfNodes.txt'.
# -------------------------------------------------------------------------------------------------------------------

#!/usr/bin/env python

def main():
	fp_write = open('../Interactions_Ecoli/noOfNodes.txt','w') # Output File
	count_node = {}
	with open('../Interactions_Ecoli/Ecoli_PPIs.txt') as fp: # Input File
		for ln in fp:
			if '\n' in ln:
				ln = ln[:-1]
			word = ln.split('\t')
			# print word
			if not word[0] in count_node.keys():
				count_node.update({word[0]:1})
			if not word[1] in count_node.keys():
				count_node.update({word[1]:1})
	count = len(count_node.keys())
	fp_write.write(str(count))
	fp_write.close()

#---------------------------------------------------------------------------------------

if __name__=='__main__':
	main()