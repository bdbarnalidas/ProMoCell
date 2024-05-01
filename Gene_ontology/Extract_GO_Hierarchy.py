
# ---------------------------------------------------------------------------------------------------------------------------
# This code extracts the GO hierarchies of the PLG proteins from GO database.

# Input - The GO database stored in 'GO/Input/go.obo'.
#		  The GO information of PLG proteins extracted from the UniProt dump stored in 'GO/Input/Ecoli_GO.txt'.
# Output - The GO hierarchies of the PLG proteins saved in 'GO/Individual_Clusters_GO_Hierarchies'.
# ---------------------------------------------------------------------------------------------------------------------------

from collections import defaultdict
  
# Globally declared a dictionary to store the vertex and the integer number as its representative
VERTEX_DICT = {}
REVERSE_VERTEX_DICT = {}

#This class represents a directed graph 
# using adjacency list representation
class Graph:
  
    def __init__(self,vertices):
        #No. of vertices
        self.V= vertices 
         
        # default dictionary to store graph
        self.graph = defaultdict(list) 
  
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
  
    '''A recursive function to print all paths from 'u' to 'd'.
    visited[] keeps track of vertices in current path.
    path[] stores actual vertices and path_index is current
    index in path[]'''
    def printAllPathsUtil(self, u, d, visited, path,fp_write):
    	# print 'u:', u
    	# print 'd:', d
        # Mark the current node as visited and store in path
        visited[u]= True
        path.append(u)
		
        # If current vertex is same as destination, then print
        # current path[]
        if u == d:
            # print path
            GO_path = []
            for i in path:
            	GO_path.append(REVERSE_VERTEX_DICT[i])
            # print GO_path
            for j in range(len(GO_path)):
            	fp_write.write(GO_path[j]+',')
            fp_write.write('\t')
        	# print path[u]
        else:
            # If current vertex is not destination
            #Recur for all the vertices adjacent to this vertex
            for i in self.graph[u]:
                if visited[i]==False:
                    self.printAllPathsUtil(i, d, visited, path,fp_write)
                     
        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[u]= False


  
  
    # Prints all paths from 's' to 'd'
    def printAllPaths(self,s, d,fp_write):
 
        # Mark all the vertices as not visited
        visited =[False]*(self.V)
 
        # Create an array to store paths
        path = []
 
        # Call the recursive helper function to print all paths
        self.printAllPathsUtil(s, d,visited, path,fp_write)



def getTerm(stream):
  block = []
  for line in stream:
    if line.strip() == "[Term]" or line.strip() == "[Typedef]":
      break
    else:
      if line.strip() != "":
        block.append(line.strip())
  return block

def parseTagValue(term):
  data = {}
  for line in term:
    tag = line.split(': ',1)[0]
    # print tag
    value = line.split(': ',1)[1]
    # print value
    if not data.has_key(tag):
      data[tag] = []
    data[tag].append(value)
  return data

def getDescendents(goid):
  recursiveArray = [goid]
  if terms.has_key(goid):
    children = terms[goid]['c']
    if len(children) > 0:
      for child in children:
        recursiveArray.extend(getDescendents(child))
  return set(recursiveArray)

def getAncestors(goid,terms):
  recursiveArray = [goid]
  if terms.has_key(goid):
    parents = terms[goid]['p']
    if len(parents) > 0:
      for parent in parents:
        recursiveArray.extend(getAncestors(parent,terms))
  return set(recursiveArray)

def Found_go(accession):
	go_list = []
	with open('../Input/Ecoli_GO.txt') as fp1: # Input File
		for ln1 in fp1:
			word = ln1.split('\t')
			if word[1] == accession:
				go_list.append(word[3])
			elif accession in word[6]:
				go_list.append(word[3])
	return go_list

def main():
	oboFile = open('../Input/go.obo','r') # Input File - GO database

	#declare a blank dictionary
	#keys are the goids
	terms = {}

	#skip the file header lines
	getTerm(oboFile)

	#infinite loop to go through the obo file.
	#Breaks when the term returned is empty, indicating end of file
	while 1:
	  #get the term using the two parsing functions
	  term = parseTagValue(getTerm(oboFile))
	  if len(term) != 0:
	    termID = term['id'][0]
	    # print termID
	    #only add to the structure if the term has a is_a tag
	    #the is_a value contain GOID and term definition
	    #we only want the GOID

	    if term.has_key('is_a'):
	      termParents = [p.split()[0] for p in term['is_a']]
	      if not terms.has_key(termID):
	        #each goid will have two arrays of parents and children
	        terms[termID] = {'p':[],'c':[],'d':[]}

	      #append parents of the current term
	      terms[termID]['p'] = termParents

	      #for every parent term, add this current term as children
	      for termParent in termParents:
	        if not terms.has_key(termParent):
	          terms[termParent] = {'p':[],'c':[]}
	        terms[termParent]['c'].append(termID)
	    if term.has_key('relationship'):
	    	termPart = []
	    	for d in term['relationship']:
	    		termPart.append([d.split(' ')[0]])
	    		termPart.append([d.split(' ')[1]])
	    	terms[termID]['d'] = termPart
	  else:
	    break
	# parent = terms['GO:0005930']['p']
	# children = terms['GO:0005930']['c']
	# parts = terms['GO:0005930']['d']
	# print parent
	# print children
	# print parts
	# ab = getAncestors('GO:0050779',terms)
	# print ab
	return terms

def write_path(goid,size,terms,list_of_vertex,fp_write):
	g = Graph(size)
	flag1 = 0
	flag2 = 0
	flag3 = 0
	
	for elem in list_of_vertex:
		if elem == 'GO:0008150': # Biological Process
			flag1 = 1
		elif elem == 'GO:0003674': # Molecular Function
			flag2 = 1
		elif elem == 'GO:0005575': # Cellular Component
			flag3 = 1
		
		# cd = []
		# if elem in terms.keys():
		cd = terms[elem]['p']
		for j in range(len(cd)):
			g.addEdge(VERTEX_DICT[elem],VERTEX_DICT[cd[j]])
	if flag1:
		g.printAllPaths(VERTEX_DICT[goid],VERTEX_DICT['GO:0008150'],fp_write)	
	elif flag2:
		g.printAllPaths(VERTEX_DICT[goid],VERTEX_DICT['GO:0003674'],fp_write)	
	elif flag3:
		g.printAllPaths(VERTEX_DICT[goid],VERTEX_DICT['GO:0005575'],fp_write)



terms = main()
folder = '../Individual_Clusters_GO_Hierarchies/' # Output Folder
read_folder = '../Individual_Clusters/' # Input Folder
count = 1
count_protein = 0
cluster_count = 125 # Input the total count of clusters
while count <= cluster_count:
	print "Cluster No "+str(count)
	filename = folder+str(count)+'.txt'
	fp_write = open(filename,"w")
	filename1 = read_folder+str(count)+'.txt'
	with open(filename1) as fp:
		for ln in fp:
			ln = ln.replace('\n','')
			if ln != '':
					fp_write.write(ln+'\t')
					count_protein += 1
					print count_protein
					go_list = Found_go(ln)
					if len(go_list) == 0:
						print "GO not available"
					else:
						for i in range(len(go_list)):
							if go_list[i] not in terms.keys():
								print 'Obsolute  ', go_list[i]
							else:
								VERTEX_DICT = {}
								REVERSE_VERTEX_DICT = {}

								ab = getAncestors(go_list[i],terms)
								size = len(ab)
								list_of_vertex = []
								no_of_vertex = 0
								while len(ab) > 0:
									list_of_vertex.append(ab.pop())
									VERTEX_DICT.update({list_of_vertex[-1] : no_of_vertex})
									REVERSE_VERTEX_DICT.update({no_of_vertex : list_of_vertex[-1]})
									no_of_vertex += 1

								write_path(go_list[i],size,terms,list_of_vertex,fp_write)
			fp_write.write('\n')
	fp_write.close()
	count += 1

filename = folder + 'Single_Node.txt' # Output File 
fp_write = open(filename,"w")
filename1 = '../../PLG_Clustering/MCL_Clusters/Single_Node_Clusters.txt' # Input File - Single_Node Clusters
with open(filename1) as fp:
	for ln in fp:
		ln = ln.replace('\n','')
		if ln != '':
				fp_write.write(ln+'\t')
				count_protein += 1
				print count_protein
				go_list = Found_go(ln)
				if len(go_list) == 0:
					print "GO not available"
				else:
					for i in range(len(go_list)):
						if go_list[i] not in terms.keys():
							print 'Obsolute  ', go_list[i]
						else:
							VERTEX_DICT = {}
							REVERSE_VERTEX_DICT = {}

							ab = getAncestors(go_list[i],terms)
							size = len(ab)
							list_of_vertex = []
							no_of_vertex = 0
							while len(ab) > 0:
								list_of_vertex.append(ab.pop())
								VERTEX_DICT.update({list_of_vertex[-1] : no_of_vertex})
								REVERSE_VERTEX_DICT.update({no_of_vertex : list_of_vertex[-1]})
								no_of_vertex += 1

							write_path(go_list[i],size,terms,list_of_vertex,fp_write)
		fp_write.write('\n')
fp_write.close()
count += 1



