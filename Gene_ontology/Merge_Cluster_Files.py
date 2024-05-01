
# ---------------------------------------------------------------------------------------------------------------------------
# This code merges the Frela output of the split cluster files into a single output file.

# Input -  Frela output of split cluster files saved in 'GO/Frela_Output/'.
# Output - Merged Frela output files of the split clusters saved in 'GO/Frela_Output/'.
# ---------------------------------------------------------------------------------------------------------------------------

import os
from subprocess import Popen, PIPE

def main1():
	filename1 = '1' # Input Filename
	os.chdir('../Frela_Output/')
	command = 'ls -l | grep ' + str(filename1) + '_ | wc -l'
	stdout = Popen(command, shell=True, stdout=PIPE).stdout
	count_file = stdout.read()
	os.chdir('../Code/')
	return count_file,filename1

def main(filename1,count_file):
	input_dir = '../Frela_Output/' # Input Folder
	path = input_dir + filename1 + '.tsv'
	fp_write = open(path,"w") # Output File
	count = 1
	filename = filename1 + '_'
	tot_count = int(count_file)
	fp_write.write('UniProt1	AnnCorp1	UniProt2	AnnCorp2	BP.fsBMA	z.BP.fsBMA	MF.fsBMA	z.MF.fsBMA	CC.fsBMA	z.CC.fsBMA	comb.BP.MF.CC\n')
	while count <= tot_count:
		filename2 = input_dir + filename + str(count) + '.tsv'
		with open(filename2) as fp:
			next(fp)
			for ln in fp:
				fp_write.write(ln)
		count += 1
	fp_write.close()

#---------------------------------------------------------------------------------------

if __name__=='__main__':
	count_file,filename1 = main1()
	main(filename1,count_file)


