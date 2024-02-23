public class Fibonacci{

    //This is the normal recursive way
    public static int calcFib(int n){
        if(n==1 || n==2){
            return 1;
        }
        else{
            return calcFib(n-1) + calcFib(n-2);
        }
    }

    //This is the memoized way
    public static int dynFib(int n, int[] array){
        int result;
        if(array[n] != 0){
            return array[n];
        }
        if(n==1 || n==2){
            return 1;
        }
        else{
            result = dynFib(n-1,array) + dynFib(n-2,array);
        }
        array[n] = result;
        return result;
    }

    //This is tabulation way
    public static int bottomFib(int n) { 
        int array[] = new int[n+1]; 
        array[0] = 0; 
        array[1] = 1; 
        for (int i = 2; i <= n; i++) 
          array[i] = array[i-1] + array[i-2]; 
        return array[n]; 
    } 

    public static void main(String[] args) {
        System.out.println("This is the normal recursive way");
        System.out.println(calcFib(8));
        System.out.println("This is memoized");
        int n = 8;
        int [] fib = new int[n+1];
        System.out.println(dynFib(n,fib));
        System.out.println("This is with tabulation");
        int m = 8;
        System.out.println(bottomFib(m));
        


    }
}