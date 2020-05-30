public class growthPopulation{
    /*p0, percent, aug (inhabitants coming or leaving each year), p (population to surpass)
the function nb_year should return n number of entire years needed to get a population greater or equal to p.
aug is an integer, percent a positive or null number, p0 and p are positive integers (> 0)*/

    public static int nbYear(int p0, double percent, int aug, int p){
        int years = 0;
        while(p0 < p){
            p0 = (int)(p0 + (p0*(float)(percent/100))+ aug);
            years++;
        }
        return years;
    }
    public static void main(String[] args) {
        int result = nbYear(1000,2,50,1200);
        System.out.println(result);
    }
}
