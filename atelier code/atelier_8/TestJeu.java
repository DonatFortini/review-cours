package atelier_8;

public class TestJeu {
    public static void main(String[] args) {
        for(int i=0;i<5;i++){
            Jeu at8 =new Jeu("AtelierPOO", 4, 10);
            Joueur paul=new Joueur("paul");
            Joueur lucien=new Joueur("lucien");
            paul.ajouterPersonnage(new Tauren("Hector",15,10));
            paul.ajouterPersonnage(new Humain("Jean", 10));
            lucien.ajouterPersonnage(new Humain("marie", 10));
            lucien.ajouterPersonnage(new Tauren("Hercule",20, 5));
            at8.ajouterJoueur(paul);
            at8.ajouterJoueur(lucien);
            at8.lancerJeu();
        }
    }
    
    
}
