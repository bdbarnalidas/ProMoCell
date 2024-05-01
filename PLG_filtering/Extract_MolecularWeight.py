
# -------------------------------------------------------------------------------------------------------------------
# This code downloads the UniProt files for the proteins (nodes) of the PLG.

# Input - The PLG stored in 'PLG/PLG.txt'.
# Output - The UniProt files for the proteins of PLG stored in 'MolecularWeight_From_UniProt/'.
# -------------------------------------------------------------------------------------------------------------------

from __future__ import division
from lxml import html
import requests
import time
import math
import sys

http_proxy  = "http://172.16.2.30:8080"
https_proxy = "https://172.16.2.30:8080"
ftp_proxy   = "ftp://172.16.2.30:8080"

proxyDict = { 
              "http"  : http_proxy, 
              "https" : https_proxy, 
              "ftp"   : ftp_proxy
            }

def main():
	count = 0
	# fp_node = open('../MolecularWeight_From_UniProt/noOfFiles.txt','w') # Output File
	fp = open("../../PLG/PLG.txt") # Input File - PLG
	allIds = []
	for line in fp.readlines():
		ids = line.split()
		allIds.append(ids[0])
		allIds.append(ids[1])
	allIdsUnique = list(set(allIds))
	fp.close()

	for i in allIdsUnique:
		filename = '../MolecularWeight_From_UniProt/'+str(i)+'.txt' # Output Folder
		fp_write = open(filename,'w')
		url = """http://www.uniprot.org/uniprot/"""+i
		response = ''
		while response == '':
			try:
				response = requests.get(url,proxies = proxyDict)
			except:
				print("Connection refused by the server..")
				print("Let me sleep for 5 seconds")
				print("ZZzzzz...")
				time.sleep(5)
				print("Was a nice sleep, now let me continue...")
				continue
			page=response.text
			page=page.encode('ascii', 'ignore').decode('ascii')
			fp_write.write(page)
			fp_write.close()
			count += 1
			print count
	# fp_node.write(str(count))

#---------------------------------------------------------------------------------------

if __name__=='__main__':
	main()

