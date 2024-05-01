
# ---------------------------------------------------------------------------------------------------------------------------
# This code counts the number of validated clusters.

# Input - The statistical analysis output files saved in 'GO/Analysis_Output/'.
# Output - The validated clusters are saved in 'GO/Analysis_Output/Analysis.tsv'.
# ---------------------------------------------------------------------------------------------------------------------------

#!/usr/bin/env python
import sys, os, warnings
import numpy as np
from itertools import izip, izip_longest

def main():
	folder1 = '../Clusters_After_Removing_Obsolute_Proteins' # Input Folder
	list_of_files = []
	length_of_files = []
	for filename in os.listdir(folder1):
		alla = folder1 + '/' + filename
		with open(alla) as f:
			lines = f.read().splitlines()
		length_of_files.append(len(lines))
		barn = filename.split('.')
		list_of_files.append(barn[0])

	# print len(list_of_files)
	# print list_of_files
	ReadFile1 = '../Analysis_Output/InClusterAnalysis.csv' # Input File
	ReadFile2 = '../Analysis_Output/OutClusterAnalysis.csv' # Input File

	WriteFile = '../Analysis_Output/Analysis.tsv' # Output File
	fp_write = open(WriteFile,'w')
	fp_write.write('Cluster_no' + '\t' + 'BP' + '\t' + 'MF' + '\t' + 'CC' + '\t' + 'Validated?' + '\n')

	count = 1
	flag_BP = 0
	flag_MF = 0
	flag_CC = 0
	count_validate = 0
	count_protein = 0
	line_count = 0

	for ln1, ln2 in izip(open(ReadFile1), open(ReadFile2)):
	# with open(ReadFile1) as fp1, open(ReadFile2) as fp2:
	# 	for ln1,ln2 in izip(fp1,fp2):
		if count == 1:
			# print count
			line_count = 0
			count += 1
			continue
		else:
			flag_BP = 0
			flag_MF = 0
			flag_CC = 0
			# print count
			count += 1
			word1 = ln1.split(',')
			word2 = ln2.split(',')
			fp_write.write(str(word1[0]) + '\t')
			if float(word1[3]) >= float(word2[3]): # BP_Mean of in-group higher than out-group
				fp_write.write('H' + '\t')
				flag_BP = 1
			else:
				fp_write.write('L' + '\t')
			if float(word1[7]) >= float(word2[7]): # MF_Mean of in-group higher than out-group
				fp_write.write('H' + '\t')
				flag_MF = 1
			else:
				fp_write.write('L' + '\t')
			if float(word1[11]) >= float(word2[11]): # CC_Mean of in-group higher than out-group
				fp_write.write('H' + '\t')
				flag_CC = 1
			else:
				fp_write.write('L' + '\t')
			if flag_BP == 1 or flag_CC == 1:
				fp_write.write('Y' + '\n')
				count_protein += length_of_files[line_count]
				count_validate += 1
			else:
				fp_write.write('' + '\n')
			line_count += 1
 
	fp_write.close()
	print 'Count_validate', count_validate
	print 'Count_protein', count_protein


#---------------------------------------------------------------------------------------

if __name__=='__main__':
	main()