package atelier_8;
import java.util.ArrayList;

public class Joueur {
    private String nom;
    private String code="J";
    private static int nbJoueur=0;
    private int nbPoint=0;
    private  ArrayList <Personnage> listePerso;

    public Joueur(String nom){
        nbJoueur+=1;
        this.nom=nom;
        code+=nbJoueur;
        ArrayList listePerso=new ArrayList<Personnage>();
    }

    public void ajouterPersonnage(Personnage p){
        if (!(this.listePerso.contains(p))){
            this.listePerso.add(p);
        }
    }

    public ArrayList<Personnage> getList(){
        return listePerso;
    }

    public int getNbPoint(){
        return nbPoint;
    }

    public void modifPoint(int nb){
        if(this.nbPoint+nb<0){
            nbPoint=0;
        }
        else{
            nbPoint+=nb;
        }
    }

    public boolean peutJouer(){
        return listePerso.size()>=1;
    }
    
    public String toString(){
        if(peutJouer()){
            return code+" "+nom+" ( "+nbPoint+" points) avec "+listePerso.size()+" personnage"; 
        }
        return code+" "+nom+" ( "+nbPoint+" points) aucun personnage";
    }
}
