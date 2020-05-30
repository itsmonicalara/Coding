public class CoinRow{

    public static int coinRowTab(int[] coins, int n) {
        int[] table = new int[n + 1];

        table[0] = 0;
        table[1] = coins[0];

        for(int i=2; i<=n; i++){
            table[i] = Math.max(table[i-1], table[i-2] + coins[i]);
        }
        return table[table.length-1]; //Imprimir el último elemento de la tabla
    }   

    public static int coinRowRec(int[] coins, int n){
		if(n==0){
			return 0;
		}else if(n==1){
			return coins[0];
		}else{
			return Math.max(coinRowRec(coins, n-1), coinRowRec(coins, n-2) + coins[n]);
		}
		
    }
    
    public static void main(String[] args) {
        //double [] coins = {1,0.5,0.2,2,0.5,1,2,0.5,1,0.1};
        int[] coins = {5,1,2,10,5,2};
        int n = coins.length-1;
        System.out.println(coinRowTab(coins,n));
        System.out.println(coinRowRec(coins,n));
    }
}