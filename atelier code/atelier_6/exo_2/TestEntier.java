package atelier_6.exo_2;

public class TestEntier {
    public static void main(String[] args) {
        Entier e1=new Entier(5, 15);
        Entier e2=new Entier(9, 13,10);
        Entier e3=new Entier(10, 20,15);
        Entier e4=new Entier(10, 20,20);
        e1.setValeur(21);
        e1.setValeur(15);
        System.out.println(e1);
        e3.incremente(5);
        e3.incremente();
        System.out.println(e3);
        System.out.println(e2);
        System.out.println(e3.equals(e4));
        System.out.println(e3.equals(e2));
        EntierFou ef=new EntierFou(5, 10, 3, 5);
        ef.incremente(4);
        System.out.println(ef);
    }
    
}
