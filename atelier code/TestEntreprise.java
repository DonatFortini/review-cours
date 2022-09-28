import atelier_7.Adresse;   
import atelier_7.Employe;
import atelier_7.Secretaire;
import atelier_7.Manager;
import java.util.GregorianCalendar;

public class TestEntreprise {
    public static void main(String[] args) {
        /*
         * pour des raison de test la date du jour est rentrable en parametre,mais,
         * dans des condition reeles on mettra directement la date 
         * (date du jour ou on instancit le constructeur)
         *  dans le constructeur pour eviter les fraudes
         */

        GregorianCalendar dateDuJour=new GregorianCalendar();
        
        GregorianCalendar greg=new GregorianCalendar(2010,7,20);
        Adresse add=new Adresse("20137", "5 rue jean pierre", "Porto-vecchio");

        GregorianCalendar greg1=new GregorianCalendar(2000,7,20);
        Adresse add1=new Adresse("20137", "5 rue jean pierre", "Porto-vecchio");

        GregorianCalendar greg2=new GregorianCalendar(1980,8,20);
        Adresse add2=new Adresse("20137", "5 rue jean pierre", "Porto-vecchio");
        



        Employe emp0=Employe.createEmploye("turlu", "tutu", greg, add,1200,dateDuJour);
        Employe emp1=Employe.createEmploye("mama", "mommo", greg1, add1,1200,dateDuJour);

        System.out.println(emp0);
        System.out.println(emp1);

        Secretaire secretaire=Secretaire.createSecretaire("tati", "toto", greg1, add1,1200,dateDuJour);
        Manager manager=Manager.createManager("fil", "depech", greg2, add2,1200,greg1);

        System.out.println(secretaire);
        System.out.println(manager);

        manager.ajouterSecretaire(secretaire);
        secretaire.affichListeManager();

        manager.supprimerSecretaire(secretaire);
        secretaire.affichListeManager();

        secretaire.ajouterManager(manager);
        System.out.println(manager.getSecretaire());
        secretaire.affichListeManager();

        secretaire.augmenterLeSalaire(10);
        manager.augmenterLeSalaire(10);
        emp1.augmenterLeSalaire(10);

        System.out.println(secretaire);
        System.out.println(manager);
        System.out.println(emp1);
    }
}
