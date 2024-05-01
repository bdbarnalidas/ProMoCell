
# ---------------------------------------------------------------------------------------------------------------------------
# This code breaks big cluster files into smaller counterparts.

# Input - Identify the big clusters containing more than 60 proteins present in 'GO/Individual_Clusters/'. 
# Output - Smaller cluster files numbered as *_1,*_2.... where * is the cluster no and saved in 'GO/Individual_Clusters/'. 
# ---------------------------------------------------------------------------------------------------------------------------

import numpy as np
import pickle
import copy
import random
import os

def main():
	count_lines = 1
	count_files = 1
	Input_filename = '1' # Input File - The file that you want to split
	output_dir = '../Individual_Clusters/' # Output Folder
	Path = output_dir + Input_filename + '.txt'
	
	fp = open(Path)  
	lines = fp.readlines()
	lines = lines[:-1]
	# print len(lines)

	write_file = output_dir + Input_filename + '_' + str(count_files) + '.txt'
	fp_write = open(write_file,"w")
	fp_write.write(lines[0])

	for i in range(1, len(lines)):
		if count_lines % 60 == 0:
			fp_write.close()
			count_lines = 1
			count_files = count_files + 1
			write_file = output_dir + Input_filename + '_' + str(count_files) + '.txt'
			fp_write = open(write_file,"w")
			fp_write.write(lines[i])
		else:
			fp_write.write(lines[i])
			count_lines += 1
	fp_write.close()

#----------------------------------------------------------------
if __name__ == '__main__':
	main()
