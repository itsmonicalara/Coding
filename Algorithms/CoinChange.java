public class CoinChange{

    //This is brute force
    public static int change(int[] denom, int n, int money) {
        if(money == 0){
            return 0;
        }else if(n < 0){
            return 10008000;
        }else{
            return Math.min(change(denom, n-1, money),
            change(denom, n-1, money%denom[n]) + money/denom[n]);
        }
    }
    
    //The backtracking way
    public static int changeBack(int[] denom, int n, int money) {
        if(money == 0){
            return 0;
        }else if(n == 0){
            return -1;
        }else if(money < denom[n]){
            return change(denom, n-1, money);
        }else{
            return Math.min(change(denom, n-1, money), 
            change(denom, n-1, money%denom[n]) + money/denom[n]);
        }
    }

    public static void main(String[] args) {
        int[] denom = {1,2,8,10};
        int n = denom.length;
        int money = 17;
        System.out.println(change(denom, n-1, money));
        System.out.println(changeBack(denom, n-1, money));
    }
}