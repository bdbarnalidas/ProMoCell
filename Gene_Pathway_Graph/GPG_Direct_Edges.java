
// -------------------------------------------------------------------------------------------------------------------
// This code identifies the direct edges of the GPG.

// Input - The GPG node information stored in 'GPG/Nodes_Edges_GPG/Nodes_Pathway_Maps.txt'.
//         The GPG edge information stored in 'GPG/Nodes_Edges_GPG/Edges_Pathway_Maps.txt'.
//         The UniProt Ids of the GPG nodes stored in 'GPG/Uniprot_Ids_GPG/IDs.txt'.
// Output - The DiEdges of GPG saved in 'GPG/GPG_Direct_Edges/GPG_DiEdges.txt'.
// -------------------------------------------------------------------------------------------------------------------

import java.io.*;
import java.math.*;
import java.util.*;
public class GPG_Direct_Edges {

    public static void main(String[] args) throws IOException
    {	
        mysolver mysol = new mysolver();
        mysol.solve();
    }

}

class mysolver {
	
    void solve() throws IOException
    {
    	PrintWriter pout = new PrintWriter(new BufferedOutputStream(System.out));	
    	BufferedReader br1 = new BufferedReader(new FileReader("../Nodes_Edges_GPG/Nodes_Pathway_Maps.txt"));
    	BufferedReader br2 = new BufferedReader(new FileReader("../Nodes_Edges_GPG/Edges_Pathway_Maps.txt"));
    	BufferedReader br3 = new BufferedReader(new FileReader("../Uniprot_Ids_GPG/IDs.txt"));
    	
    	ArrayList<node> nodes = new ArrayList<node>();
    	String text = "";
    	int count = 0;
    	
    	int size = 0;
    	
    	while((text = br1.readLine()) != null)
    	{
    		if(count%2 == 0)
    		{
    			node t1  = new node();
    			t1.pathway_id = text;
    			nodes.add(t1);
    		}
    		count++;
    	}
    	
    	count = 0;
    	while((text = br3.readLine())!= null)
    	{
    		node t1 = nodes.get(count++);
    		t1.uni_id = text;
    	}
    	
    	Collections.sort(nodes);
    	
    	TreeSet<String> count_nodes = new TreeSet<String>();
    	HashMap<edge,Integer> hmap = new HashMap<edge,Integer>();
    	
    	while((text = br2.readLine())!= null)
    	{
    		String text2 = br2.readLine();
    		node n1 = new node();
    		n1.pathway_id = text;
    		
    		node n2 = new node();
    		n2.pathway_id = text2;
    		
    		int id0 = Collections.binarySearch(nodes, n1);
    		int id1 = Collections.binarySearch(nodes, n2);
    		//System.out.println(id0+" "+id1);
    		if(id0 >= 0 && id0 < nodes.size() && id1 >= 0 && id1 < nodes.size())
    		{
    			if(nodes.get(id0).uni_id.compareTo("")!=0 && nodes.get(id1).uni_id.compareTo("")!=0)
    			{
    				String str1 = nodes.get(id0).uni_id;
    				String str2 = nodes.get(id1).uni_id;
    				String st1[] = str1.split(" ");
    				String st2[] = str2.split(" ");
    				
    				for(int i=1;i<st1.length;i++)
    				{
    					for(int j=1;j<st2.length;j++)
    					{
    						edge e1 = new edge();
    						e1.id1 = st1[i];
    						e1.id2 = st2[j];
    						count_nodes.add(st1[i]);
    						count_nodes.add(st2[j]);
    						if(hmap.containsKey(e1))
    						{
    							hmap.put(e1, hmap.get(e1)+1);
    							//System.out.println("HI++++++++");
    						}
    						else
    						{
    							hmap.put(e1,1);
    							//System.out.println("YO++++++");
    						}
    					}
    				}
    				//System.out.println(st1[1]+" "+st2[1]);
    			}	
    		}
    	}
    	
    	Iterator it = hmap.entrySet().iterator();
    	int ct=0;
    	PrintWriter p1 = new PrintWriter("../GPG_Direct_Edges/GPG_DiEdges.txt");
    	while(it.hasNext())
    	{
    		ct++;
    		Map.Entry mp = (Map.Entry)it.next();
    		edge e1  = (edge)mp.getKey();
    		int wt = (int)mp.getValue();
    		p1.write(e1.id1+" "+e1.id2+" "+Integer.toString(wt)+"\n");
    	}
    	p1.close();
    	System.out.println("DiEdge Count : "+ct);
    	System.out.println("Node Count : "+count_nodes.size());
    	br1.close();
    	br2.close();
    	br3.close();
        pout.close();
    }    
}

class node implements Comparable<node>{
	String pathway_id;
	String uni_id;
	public int compareTo(node t)
	{
		return this.pathway_id.compareTo(t.pathway_id);
	}
}



class edge implements Comparable<edge>{
	String id1;
	String id2;
	public int compareTo(edge t)
	{
		String f1 = "";
		String f2 = "";
		if(id1.compareTo(id2)<0)
		{
			f1 = id1;
			f2 = id2;
		}
		else
		{
			f1 = id2;
			f2 = id1;
		}
		
		
		String s1 = "";
		String s2 = "";
		
		if(t.id1.compareTo(t.id2)<0)
		{
			s1 = t.id1;
			s2 = t.id2;
		}
		else
		{
			s1 = t.id2;
			s2 = t.id1;
		}
		
		if(f1.compareTo(s1)<0)
		{
			return -1;
		}
		else if(f1.compareTo(s1)==0)
		{
			return f2.compareTo(s2);
		}
		else
		{
			return 1;
		}
	}
}
