public class Knapsack{
    public static int knapRec(int capacity, int[] weight, int[] value, int n){
    	//El objeto no pesa nada
        if(n == 0 || capacity == 0){
            return 0;
        }
        if(weight[n-1] > capacity){ //El objeto pesa más que la mochila
            return knapRec(capacity, weight, value, n-1);
        }
        else{
            return Math.max(value[n-1] + knapRec(capacity-weight[n-1],weight,value,n-1),
            knapRec(capacity, weight, value, n-1));
        }
    }
    public static int knapTab(int capacity, int[] weight, int[] value, int n){
        int[][] table = new int[n+1][capacity+1];
        for(int i=0;i<=n;i++){
            for(int j=0;j<=capacity;j++){
                if(i==0 || j==0){
                table[i][j] = 0;
                }else if(weight[i-1] <= j){
                    table[i][j] = Math.max(value[i-1] + table[i-1][j-weight[i-1]],table[i-1][j]);
                }else{
                    table[i][j] = table[i-1][j];
                }
            }           
        }
        return table[n][capacity];
    }
    public static int knapMemo(int capacity, int[] weight, int[] value, int n, int[][] array){
        if(n == 0 || capacity == 0){
            return 0;
        }else if(weight[n-1] > capacity){
            return knapMemo(capacity, weight, value, n-1, array);
        }else{
            return Math.max(value[n-1] + knapMemo(capacity-weight[n-1],weight,value,n-1,array),
            knapMemo(capacity, weight, value, n-1,array));
        }
    }
    //The motherfucking backtracking way *it has to be a tree*
    public static int knapBack(int capacity, int[] weight, int[] value, int n){
        int something = capacity;
        return something; 
    }

    //Branch and bound *This works better when the weights are not integers*
    public static int knapBranch(int capacity, int[] weight, int[] value, int n){
        int something = capacity;
        return something;
    }

    //Greedy - Technique *We can break the items in fractions*
    public static int knapGreedy(int capacity, int[] weight, int[] value, int n){
        int something = capacity;
        return something;
    }

    public static void main(String[] args) {    
        int value[] = new int[]{1,4,5,7}; 
        int weight[] = new int[]{1,3,4,5};
        int capacity = 7;
        int n = value.length;
        System.out.println(knapRec(capacity, weight, value, n));
        System.out.println(knapTab(capacity, weight, value, n));
        int[][] array = new int[n+1][capacity+1];
        System.out.println(knapMemo(capacity, weight, value, n, array));
    }
}