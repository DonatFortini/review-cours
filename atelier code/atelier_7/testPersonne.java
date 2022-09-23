package atelier_7;
import java.util.GregorianCalendar;

public class testPersonne {
    public static void main(String[] args) {
        GregorianCalendar greg=new GregorianCalendar(2000,7,20);
        Adresse add=new Adresse("20137", "5 rue jean pierre", "Porto-vecchio");

        GregorianCalendar greg1=new GregorianCalendar(2000,7,20);
        Adresse add1=new Adresse("20250", "5 rue jean pierre", "Corte");

        GregorianCalendar greg2=new GregorianCalendar(1920,8,20);
        Adresse add2=new Adresse("20137", "5 rue jean pierre", "Porto-vecchio");

        Personne p1=new Personne("turlu", "tutu",greg, add);
        Personne p2=new Personne("turlu", "tutu",greg1, add1);
        Personne p3=new Personne("turlu", "toto",greg2, add2);

        System.out.println(p1.plusAgee(p3));

        System.out.println(Personne.plusAgee(p1, p3));

        System.out.println(p1.equals(p2));

        System.out.println(p1.equals(p3));

        System.out.println(Personne.quelAge(p1));
    }
}
