import java.util.Iterator;
import java.util.LinkedList;

public class DecreaseConquer {
    //DECREASE BY CONSTANT
    //Graphs
    private int V;   // No. of vertices 
    private LinkedList<Integer> adj[];

    public DecreaseConquer(int v) {
        V = v;
        adj = new LinkedList[v]; 
        for (int i=0; i<v; ++i) 
            adj[i] = new LinkedList(); 
    }

    public void addEdge(int v, int w){
        adj[v].add(w);
    }

     void DFSUtil(int v,boolean visited[]) 
    { 
        // Mark the current node as visited and print it 
        visited[v] = true; 
        System.out.print(v+" "); 
  
        // Recur for all the vertices adjacent to this vertex 
        Iterator<Integer> i = adj[v].listIterator(); 
        while (i.hasNext()) 
        { 
            int n = i.next(); 
            if (!visited[n]) 
                DFSUtil(n, visited); 
        } 
    } 

    void DFS(int v) { 
        // Mark all the vertices as not visited(set as 
        // false by default in java) 
        boolean visited[] = new boolean[V]; 
  
        // Call the recursive helper function to print DFS traversal 
        DFSUtil(v, visited); 
    } 

    public static void main(String[] args) {
        DecreaseConquer dc = new DecreaseConquer(4);
        dc.addEdge(0, 1); 
        dc.addEdge(0, 2); 
        dc.addEdge(1, 2); 
        dc.addEdge(2, 0); 
        dc.addEdge(2, 3); 
        dc.addEdge(3, 3); 

        System.out.println("Following is Depth First Traversal " + "(starting from vertex 2)"); 
        dc.DFS(2);

    }
}