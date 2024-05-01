
# -------------------------------------------------------------------------------------------------------------------
# This code constructs the GPG by identifying all the direct and indirect edges. The final edge-weight is the
# maximum of the constituent edge-weights.

# Input - The direct edges of GPG stored in 'GPG/GPG_Direct_Edges/GPG_DiEdges.txt'.
# Output - The final GPG stored in 'GPG/GPG_Edges/GPG.txt'.
# -------------------------------------------------------------------------------------------------------------------

from __future__ import division
from operator import itemgetter
from collections import defaultdict

def main():
	#read direct edges
	fp = open("../GPG_Direct_Edges/GPG_DiEdges.txt") # Input File - Direct edges of GPG
	edges = []
	for line in fp:
		line = line.split()
		if line[0] < line[1]:
			edges.append((line[0],line[1],float(line[2])))
		else:
			edges.append((line[1],line[0],float(line[2])))
	edges.sort(key=lambda tup: tup[0]+tup[1])
	fp.close()

	# fp_b = open("../GPG_Edges/GPG.txt","w")
	# for i in edges: fp_b.write(i[0]+" "+i[1]+" "+str(i[2])+"\n" )
	# fp_b.close()


	
	nodes = []
	for i in edges: nodes.extend([i[0],i[1]])
	nodes = list(set(nodes))
	print len(nodes),"total nodes"
	fp_node = open("../GPG_Edges/Nodes.txt", "w") # Output File
	fp_node.write(nodes[0])
	for i in range(1,len(nodes)):
		fp_node.write('\n'+nodes[i])
	fp_node.close()

	#find out all indirect edges of length 2
	edges2 = []
	for node1 in nodes:

		node2 = []	
		for j in edges:
			if j[0] == node1:
				node2.append(j[1])
			if j[1] == node1:
				node2.append(j[0])
		node2 = [x for x in node2 if node2!=node1]
		node2 = list(set(node2))

		node3 = []
		for j in node2:
			for k in edges:
				if k[0] == j:
					node3.append(k[1])
				if k[1] == j:
					node3.append(k[0])
		node3 = [x for x in node3 if x not in node2 and x!=node1]
		node3 = list(set(node3))

		for k in node3:
			if node1 < k:
				edges2.append((node1,k,0.5))
			else:
				edges2.append((k,node1,0.5))	
	print "0.5 done"
	#find out all indirect edges of length 3
	edges3 = []
	for node1 in nodes:

		node2 = []	
		for j in edges:
			if j[0] == node1:
				node2.append(j[1])
			if j[1] == node1:
				node2.append(j[0])
		node2 = [x for x in node2 if node2!=node1]
		node2 = list(set(node2))

		node3 = []
		for j in node2:
			for k in edges:
				if k[0] == j:
					node3.append(k[1])
				if k[1] == j:
					node3.append(k[0])
		#node3 = [x for x in node3 if x not in node2 and x!=node1]
		node3 = list(set(node3))

		node4 = []
		for j in node3:
			for k in edges:
				if k[0] == j:
					node4.append(k[1])
				if k[1] == j:
					node4.append(k[0])
		#node4 = [x for x in node4 if x not in node2 and x not in node3 and x!=node1]
		node4 = list(set(node4))

		for k in node4:
			if node1 < k:
				edges3.append((node1,k,1/3))
			else:
				edges3.append((k,node1,1/3))


	all_edges = edges + edges2 + edges3

	# # edges2_mod = []

	# # print "In 0.5"
	# # flag = 0
	# # count = 0 
	# # all_edges = edges # Put all direct interactions into the list first----FIRST PRIORITY
	# # for j in edges2:
	# # 	flag = 0 
	# # 	for i in all_edges:
	# # 		if i[0] == j[0] and i[1] == j[1]:
	# # 			print count
	# # 			count += 1
	# # 			flag = 1
	# # 			break
	# # 		else:
	# # 			flag = 0
	# # 			print count
	# # 			count += 1
	# # 	if flag == 0:
	# # 		edges2_mod.append((j[0],j[1],0.5))
	# # 	else:
	# # 		continue

	# # del all_edges[:]
	# # all_edges = edges + edges2_mod
	# # edges3_mod =[]
	# # print "In 0.33"
	# # count = 0 
	# # for j in edges3:
	# # 	flag = 0
	# # 	for i in all_edges:
	# # 		if i[0] == j[0] and i[1] == j[1]:
	# # 			print count
	# # 			count += 1
	# # 			flag = 1
	# # 			break
	# # 		else:
	# # 			flag = 0
	# # 			print count
	# # 			count += 1
	# # 	if flag == 0:
	# # 		edges3_mod.append((j[0],j[1],1/3))
	# # 	else:
	# # 		continue
	# # del all_edges[:]
	# # all_edges = edges + edges2_mod + edges3_mod




	print len(all_edges)
	all_edges.sort(key=lambda tup: tup[0]+tup[1])
	fp1 = open("../GPG_Edges/Direct_Indirect_Edges.txt", "w") # Output File (all direct & indirect edges of GPG)
	for i in all_edges: fp1.write(i[0]+" "+i[1]+" "+str(i[2])+"\n" )
	fp1.close()

	# fp_b = open("./output_eco/ambd.txt","w")
	# with open("./output_eco/all_edges.txt") as fp:
	# 	temp_line = 'PUPI'
	# 	for ln in fp:
	# 		if temp_line not in ln:
	# 			# ln = ln.replace('\n','')
	# 			word = ln.split(' ')
	# 			temp_line = word[0] + ' ' + word[1]
				
	# 			# Write to file
	# 			fp_b.write(ln)

	# fp_b.close()
#save final edge output in PathWay_edges.txt

def main1():
	fp = open("../GPG_Edges/Direct_Indirect_Edges.txt")
	res = defaultdict(list)
	for line in fp:
		line = line.split()
		res[(line[0],line[1])].append(float(line[2]))
	fp.close()
	fp1 = open("../GPG_Edges/GPG.txt","w") # Output File - Final GPG 
	for i in res: fp1.write(i[0]+" "+i[1]+" "+str(max(res[i]))+"\n")
	for i in res: print len(set(res[i]))

if __name__ == '__main__':
	main()
	main1()
