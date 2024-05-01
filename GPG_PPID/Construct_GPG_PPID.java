
// --------------------------------------------------------------------------------------------------------------
// This code combines GPG and PPID into one single graph.

// Input - GPG stored in 'GPG/GPG_Edges/GPG.txt'.
//         PPID stored in 'PPID/Nodes_Edges_PPID/Edges.txt'
// Output - GPG+PPID combined graph stored in 'GPG_And_PPID/GPG_PPID/GPG_PPID.txt'.
// --------------------------------------------------------------------------------------------------------------

import java.io.*;
import java.math.*;
import java.util.*;
public class Construct_GPG_PPID {

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
    	BufferedReader br = new BufferedReader(new FileReader("../../GPG/GPG_Edges/GPG.txt")); // Input File - GPG
    	String text = "";
    	
    	TreeSet<edge> ts = new TreeSet<edge>();
    	ArrayList<edge> ar = new ArrayList<edge>();
    	TreeSet<String> nCt = new TreeSet<String>();
    	
    	while((text = br.readLine())!= null)
    	{
    		String[] str = text.split(" ");
    		edge e1 = new edge();
    		e1.id1 = str[0];
    		e1.id2 = str[1];
    		nCt.add(e1.id1);
    		nCt.add(e1.id2);
    		System.out.println(str[0]);
    		System.out.println(str[1]);
    		if(!ts.contains(e1))
    		{
    			ts.add(e1);
    			ar.add(e1);
    		}
    	}
    	
    	System.out.println("Nodes  "+nCt.size());
    	System.out.println("Edges : "+ts.size());
    	
    	// for(int i=1;i<=13;i++)
    	// {
    		//br = new BufferedReader(new FileReader("../DIP_Data_Analysis2_d4/output/Edges_Full/Edge-Weights"+Integer.toString(i)+".txt"));
    		br = new BufferedReader(new FileReader("../../PPID/Nodes_Edges_PPID/Edges.txt")); // Input File - PPID
    		while((text = br.readLine())!= null)
    		{
    			String[] str = text.split("\t");
    			
    			edge e1 = new edge();
        		e1.id1 = str[0];
        		e1.id2 = str[1];
        		if(!ts.contains(e1))
        		{
        			ts.add(e1);
        			ar.add(e1);
        		}
    		}
    		br.close();
    	// }
    	
    	Collections.sort(ar);
    	double weight[] = new double[ar.size()];
    	Arrays.fill(weight, 0.0);
    	
    	br = new BufferedReader(new FileReader("../../GPG/GPG_Edges/GPG.txt")); // Input File - GPG
    	while((text = br.readLine())!= null)
    	{
    		String[] str = text.split(" ");
    		edge e1 = new edge();
    		e1.id1 = str[0];
    		e1.id2 = str[1];
    		int id = Collections.binarySearch(ar, e1);
    		// a = weight[id]
    		// b = Double.parseDouble(str[2]);
    		// weight[id] = Math.max(a,b);
    		weight[id] += Double.parseDouble(str[2]);
    	}
    	
    	br.close();
    	
    	
    	// for(int i=1;i<=13;i++)
    	// {
    	// 	br = new BufferedReader(new FileReader("../DIP_Data_Analysis2_d4/output/Edges_Full/Edge-Weights"+Integer.toString(i)+".txt"));
    		br = new BufferedReader(new FileReader("../../PPID/Nodes_Edges_PPID/Edges.txt")); // Input File - PPID
    		while((text = br.readLine())!= null)
    		{
    			String[] str = text.split("\t");
    			
    			edge e1 = new edge();
        		e1.id1 = str[0];
        		e1.id2 = str[1];
        		int id = Collections.binarySearch(ar, e1);
        		Double a = weight[id];
    			Double b = Double.parseDouble(str[2]);
    			weight[id] = Math.max(a,b);
        		// weight[id] += Double.parseDouble(str[2]);
    		}
    		br.close();
    	// }
    	
    	PrintWriter p1 = new PrintWriter("../GPG_PPID/GPG_PPID.txt"); // Output File
    	
    	for(int i=0;i<ar.size();i++)
    	{
    		nCt.add(ar.get(i).id1);
    		nCt.add(ar.get(i).id2);
    		p1.write(ar.get(i).id1+" "+ar.get(i).id2+" "+Double.toString(weight[i])+"\n");
    	}
    	p1.close();
    	
    	
    	System.out.println("Edges : "+ar.size());
    	System.out.println("Nodes : "+nCt.size());
    	pout.close();
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
			if(f2.compareTo(s2)<0)
				return -1;
			else if(f2.compareTo(s2)==0)
				return 0;
			else
				return 1;
		}
		else
		{
			return 1;
		}
	}
}