package atelier_5.exo_3;
import java.lang.Math;
import java.util.Random;


public class TestApi {
    public static void main(String[] args) {
        System.out.println(Math.PI);
        Random rand=new Random();
        System.out.println(rand.nextDouble(0,1));
        System.out.println(rand.nextInt(1,3));
        int x1=3;
        int x2=5;
        System.out.println(Math.max(x1, x2));
        String n1="c";
        String n2="a";
        System.out.println(n1.compareTo(n2));

    }
}
