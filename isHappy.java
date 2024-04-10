import java.util.*;
public class isHappy {
    public static void main(String [] args){
        Scanner input = new Scanner(System.in);
        happy(65);

    }
    public static boolean happy (int n ){
        if(n < 0 ){
            return false;
        }
        System.out.println(n + " n normal");
        while (n > 0) {
            System.out.println(n + " this is n before the calculation");
            System.out.println(n % 10);
            n = n / 10;

            
        }
        

        return true;
    }
}
