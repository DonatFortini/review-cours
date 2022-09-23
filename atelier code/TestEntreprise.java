import atelier_7.Adresse;
import atelier_7.Personne;
import atelier_7.Employe;
import atelier_7.Secretaire;
import atelier_7.Manager;
import java.util.GregorianCalendar;

public class TestEntreprise {
    public static void main(String[] args) {
        
        GregorianCalendar greg=new GregorianCalendar(2010,7,20);
        Adresse add=new Adresse("20137", "5 rue jean pierre", "Porto-vecchio");

        GregorianCalendar greg1=new GregorianCalendar(2000,7,20);
        Adresse add1=new Adresse("20137", "5 rue jean pierre", "Porto-vecchio");

        GregorianCalendar greg2=new GregorianCalendar(1980,8,20);
        Adresse add2=new Adresse("20137", "5 rue jean pierre", "Porto-vecchio");
        
        Personne p1=new Personne("turlu", "tutu", greg, add);
        Personne p2=new Personne("turlu", "toto", greg1, add1);
        Personne p3=new Personne("turlu", "tata", greg2, add2);
        p1=Employe.createEmploye(p1);
        p2=Employe.createEmploye(p2);

        System.out.println(p1);
        System.out.println(p2);

        Secretaire ed=Secretaire.createSecretaire(p2);
        Manager de=Manager.createManager(p3);

        System.out.println(ed);
        System.out.println(de);

        Manager.ajouterSecretaire(de, ed);
        ed.affichListeManager();

        Manager.supprimerSecretaire(de, ed);
        ed.affichListeManager();
    }
}
