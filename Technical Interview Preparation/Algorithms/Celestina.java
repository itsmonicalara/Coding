public class Celestina{
    public static int celesRec(int n){
        if(n == 0){
            return 0;
        }else if(n == 1){
            return 1;
        }else if(n == 2){
            return 2;
        }else{
            return celesRec(n-1)+(n-1)*celesRec(n-2);
        }
    }
    public static int celesTab(int n){
        int array[] = new int[n+1];
        array[0] = 0;
        array[1] = 1;
        array[2] = 2;
        for(int i = 3; i <= n; i++){
            array[i] = array[i-1] + (i-1) * array[i-2];
        }
        return array[n];
    }
    public static int celesMemo(int n, int[] array){
        if(array[n] != 0){
            return array[n];
        }else if(n == 1){
            return 1;
        }else if(n == 2){
            return 2;
        }else{
            return celesMemo(n-1,array) + (n-1) *  celesMemo(n-2,array);
        }
    }

    public static void main(String[] args) {
        System.out.println(celesRec(3));
        System.out.println(celesTab(3));
        int n = 3;
        int array[] = new int[n+1];
        System.out.println(celesMemo(n, array));
    }
}