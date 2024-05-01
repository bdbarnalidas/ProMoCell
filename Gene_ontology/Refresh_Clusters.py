
# ---------------------------------------------------------------------------------------------------------------------------
# This code removes those clusters which have become empty after removing the obsolute proteins.

# Input - The modified cluster after removing obsolute proteins saved in 'GO/Clusters_After_Removing_Obsolute_Proteins'.
# Output - The blank clusters deleted and the same folder modified i.e., 'GO/Clusters_After_Removing_Obsolute_Proteins'.
# ---------------------------------------------------------------------------------------------------------------------------

import os

def main():
	ReadFolder = '../Clusters_After_Removing_Obsolute_Proteins/' # Input Folder
	ListOfFiles = os.listdir(ReadFolder)
	for i in range(0,len(ListOfFiles)):
		filename = ReadFolder + ListOfFiles[i]
		fp = open(filename, "r")
		lines = fp.readlines()
		if len(lines) == 0:
			os.system('cd ../Clusters_After_Removing_Obsolute_Proteins')
			command = 'rm ' + ReadFolder + ListOfFiles[i]
			os.system(command)

#---------------------------------------------------------------------------------------

if __name__=='__main__':
	main()