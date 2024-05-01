
# -------------------------------------------------------------------------------------------------------------------
# This code counts the number of files present in 'GPG/Nodes_GPG' i.e., it counts the number of nodes in GPG.

# Input - The GPG node information stored in 'GPG/Nodes_GPG'.
# Output - Count of the no of nodes in GPG saved in 'GPG/Nodes_GPG/noOfFiles.txt'.
# -------------------------------------------------------------------------------------------------------------------

import os, os.path

def main():
	DIR = '../Nodes_GPG/' # Input folder
	WriteFile = DIR + 'noOfFiles.txt' # Output file
	a = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
	print a
	fp_write = open(WriteFile,'w')
	fp_write.write(str(a))
	fp_write.close()

#---------------------------------------------------------------------------------------

if __name__=='__main__':
	main()