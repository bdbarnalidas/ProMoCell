
// --------------------------------------------------------------------------------------------------------------
// This code extracts the weighted edges of PPII.

// Input - The PPIs of E. coli stored in 'PPII/Interactions_Ecoli/Ecoli_PPIs_Processing.txt'.
//         The nodes of PPII stored in 'PPII/Nodes_Edges_PPII/Nodes.txt'.
//         Nodecount of PPII stored in 'PPII/Interactions_Ecoli/noOfNodes.txt'.
// Output - The weighted edges of PPII stored in 'PPII/Nodes_Edges_PPII/Edges.txt'.
// --------------------------------------------------------------------------------------------------------------

import java.io.*;
import java.math.*;
import java.util.*;
@SuppressWarnings("unchecked")
public class Extract_Edges {
    

    ArrayList<node>[] arr ;
    public static int V = -1;
    public static void main(String[] args) throws IOException
    {
        BufferedReader br1 = new BufferedReader(new FileReader("../Interactions_Ecoli/noOfNodes.txt")); // Input File
        String cntStr = br1.readLine();
        V = Integer.parseInt(cntStr);
        br1.close();
        Extract_Edges m1 = new Extract_Edges();
        m1.main1();
    }
    public void main1() throws IOException
    {
        BufferedReader br = new BufferedReader(new FileReader("../Interactions_Ecoli/Ecoli_PPIs_Processing.txt")); // Input File
        PrintWriter pout = new PrintWriter("../Nodes_Edges_PPII/Edges.txt"); // Output File
        
        TreeSet<String> nodes = new TreeSet<String>();
        ArrayList<String> ar = new ArrayList<String>();
        
        int edges = 0;
        
        String name = "";
        while((name = br.readLine())!= null)
        {
            if(edges==0)
            {
                edges = 1;
                continue;
            }

            String[] str = name.split("\t");
            
            str[0] = str[0].substring(str[0].indexOf("kb:")+3);
            str[1] = str[1].substring(str[1].indexOf("kb:")+3);
            
            if(!nodes.contains(str[0]))
            {
                nodes.add(str[0]);
                ar.add(str[0]);
            }

            if(!nodes.contains(str[1]))
            {
                nodes.add(str[1]);
                ar.add(str[1]);
            }
            
            pout.println(str[0]+"\tedge\t"+str[1]);
        }
        //System.out.println(ar);
        Collections.sort(ar);
        arr = new ArrayList[nodes.size()];

        for(int i=0;i<nodes.size(); i++)
            arr[i] = new ArrayList<node>();
        
        br.close();
        pout.close();

        br = new BufferedReader(new FileReader("../Interactions_Ecoli/Ecoli_PPIs_Processing.txt")); // Input File
        
        TreeSet<Edge> edges_set = new TreeSet<Edge>();
        int count = 0;
        name = br.readLine();
        while((name = br.readLine())!= null)
        {
            String[] str = name.split("\t");

            str[0] = str[0].substring(str[0].indexOf("kb:")+3);
            str[1] = str[1].substring(str[1].indexOf("kb:")+3);
                
            int id0 = Collections.binarySearch(ar,str[0]);
            int id1 = Collections.binarySearch(ar,str[1]);
            //System.out.println(str[0]);
            //System.out.println(str[1]);
            //System.out.println(id0);
            //System.out.println(id1);
            if(id0 < id1)
            {
                Edge e1 = new Edge();
                e1.id1 = id0;
                e1.id2 = id1;
                
                if(edges_set.contains(e1))
                {
                    count++;
                    
                    for(int i=0 ; i< arr[id1].size(); i++)
                    {
                        if(arr[id1].get(i).id == id0)
                        {
                            node n1 = arr[id1].get(i);
                            n1.weight += 1;
                            break;
                        }
                    }
                    
                    for(int i=0 ; i< arr[id0].size(); i++)
                    {
                        if(arr[id0].get(i).id == id1)
                        {
                            node n1 = arr[id0].get(i);
                            n1.weight += 1;
                            break;
                        }
                    }
                    
                    continue;
                }
                edges_set.add(e1);
            }
            else
            {
                Edge e1 = new Edge();
                e1.id1 = id1;
                e1.id2 = id0;
                if(edges_set.contains(e1))
                {
                    count++;
                    
                    for(int i=0 ; i< arr[id1].size(); i++)
                    {
                        if(arr[id1].get(i).id == id0)
                        {
                            node n1 = arr[id1].get(i);
                            n1.weight += 1;
                            break;
                        }
                    }
                    
                    for(int i=0 ; i< arr[id0].size(); i++)
                    {
                        if(arr[id0].get(i).id == id1)
                        {
                            node n1 = arr[id0].get(i);
                            n1.weight += 1;
                            break;
                        }
                    }
                    
                    continue;
                }
                edges_set.add(e1);
            }
            
            node n1 = new node();
            n1.id = id1;
            n1.weight = 1;
            arr[id0].add(n1);
            
            node n2 = new node();
            n2.id = id0;
            n2.weight = 1;
            
            arr[id1].add(n2);
        }
        
        br.close();
        PrintWriter pr1 = new PrintWriter("../Nodes_Edges_PPII/Nodes.txt"); // Input File
        for(int i=0;i<ar.size();i++)
        {
            pr1.write(ar.get(i)+"\n");
        }
        pr1.close();

        br = new BufferedReader(new FileReader("../Interactions_Ecoli/Ecoli_PPIs_Processing.txt")); // Input File
        //PrintWriter pr = new PrintWriter("Dummy.txt");
        name = br.readLine();
        int ctt = 0;
        edges = 0;
        //pr.close();
        String filename = "../Nodes_Edges_PPII/Edges.txt"; // Output File
        PrintWriter pr = new PrintWriter(filename);
        while((name = br.readLine())!= null)
        {
            ctt++;
            String[] str = name.split("\t");
            edges++;
            
            str[0] = str[0].substring(str[0].indexOf("kb:")+3);
            str[1] = str[1].substring(str[1].indexOf("kb:")+3);
            
            int id0 = Collections.binarySearch(ar,str[0]);
            int id1 = Collections.binarySearch(ar,str[1]);
            
            int wt = 1;
            if(id0 != id1)
                wt = fordFulkerson(id0,id1);
            
            pr.write(str[0]);
            pr.write("\t");
            pr.write(str[1]);
            pr.write("\t");
            pr.write(Integer.toString(wt));
            pr.write("\n");
        }
        
        pr.close();
        System.out.println("CTT : "+ctt);
        System.out.println("Count : "+count);
        System.out.println("Edges : "+edges);
        System.out.println("Nodes : "+nodes.size());
        br.close();  
    }
    public boolean bfs(ArrayList<node>[] rGraph, int s, int t, int parent[])
    {
        boolean visited[] = new boolean[V];
        Arrays.fill(visited, false);
        Queue<queueNode> q = new LinkedList<queueNode>();
        
        queueNode start = new queueNode();
        start.id = s;
        start.depth = 0;
        q.add(start);

        visited[s] = true;
        parent[s] = -1;
        
        while (!q.isEmpty())
        {
            queueNode u1 = q.remove();
            int u = u1.id;
            
            for(int v = 0;v < arr[u].size(); v++)
            {
                queueNode toAdd = new queueNode();
                toAdd.id = rGraph[u].get(v).id ;
                toAdd.depth = u1.depth + 1;
                if ( (visited[ rGraph[u].get(v).id ]==false) && (rGraph[u].get(v).weight > 0)  && (toAdd.depth < 4) ) // We can restrict the depth to 4 in case required.
                {
                    
                    
                    q.add(toAdd);
                    
                    parent[ rGraph[u].get(v).id ] = u;
                    visited[ rGraph[u].get(v).id ] = true;
                }
            }
        }
        return (visited[t] == true);
    }
    
    int rGraph[][];
    
    int fordFulkerson(int s, int t)
    {
        int u, v;
        
        ArrayList<node>[] rGraph = new ArrayList[V];
        
        // Graph copied
        for(int i=0;i < V; i++)
        {
            rGraph[i] = new ArrayList<node>();
            for(int j=0;j<arr[i].size();j++)
            {
                node n1 = new node();
                n1.id = arr[i].get(j).id;
                n1.weight = arr[i].get(j).weight;
                rGraph[i].add(n1);
            }
        }
        
        int parent[]= new int[V];

        int max_flow = 0;
        
        while (bfs(rGraph, s, t, parent))
        {
            int path_flow = Integer.MAX_VALUE;
            
            for (v=t; v!=s; v=parent[v])
            {
                u = parent[v];
                
                int val = 0;
                int ct = 0;
                for(int i=0;i<rGraph[u].size();i++)
                {
                    if(rGraph[u].get(i).id == v)
                    {
                        val = Math.max(val, rGraph[u].get(i).weight);
                        ct++;
                        //break;
                    }
                }
                path_flow = Math.min(path_flow, val);
            }
            for (v=t; v != s; v=parent[v])
            {
                u = parent[v];
                for(int i=0;i<rGraph[u].size();i++)
                {
                    if( rGraph[u].get(i).id == v)
                    {
                        node n1 = rGraph[u].get(i);
                        n1.weight -= path_flow;
                        break;
                    }
                }
                
                for(int i=0;i<rGraph[v].size();i++)
                {
                    if( rGraph[v].get(i).id == v)
                    {
                        node n1 = rGraph[v].get(i);
                        n1.weight += path_flow;
                        break;
                    }
                }
            }
            max_flow += path_flow;
        }
        return max_flow;
    }
}

class node {
    int id;
    int weight;
}

class queueNode {
    int id;
    int depth;
}

class Edge implements Comparable<Edge>{
    int id1;
    int id2;
    public int compareTo(Edge t)
    {
        if(this.id1 == t.id1 && this.id2 == t.id2)
            return 0;
        if(this.id1 < t.id1)
        {
            return -1;
        }
        else if(this.id1 == t.id1)
        {
            if(this.id2 < t.id2)
                return -1;
            else
                return 1;
        }
        return 1;
    }
}
