package atelier_8;
import java.util.ArrayList;
import java.lang.Math;



public class Jeu {
    //j'ai modif certaine valeur pour equilibrer le jeu
    private String titre;
    public final int NB_JOUEUR_MAX=6;
    public final int NB_CASE=100;
    private ArrayList<Joueur> listJoueurs=new ArrayList<>();
    private Case cases[]=new Case[NB_CASE];
    private int nbEtapes;
    private int nbObstacles;
    private static int scoreMax=0;
    private boolean changer=false;
    private int ancien;

    public Jeu(String titre,int nbEtapes,int nbObstacles){
        this.titre=titre;
        this.nbEtapes=nbEtapes;
        this.nbObstacles=nbObstacles;
    }

    public void ajouterJoueur(Joueur j){
        if(!(listJoueurs.isEmpty())){
            if(listJoueurs.size()<6 && !(listJoueurs.contains(j))){
                listJoueurs.add(j);
            } 
        }else{listJoueurs.add(j);}
        
    }

    public ArrayList<Personnage> tousLesPerso(){
        ArrayList listeVar=new ArrayList<Personnage>();
        for(int i=0;i<listJoueurs.size();i++){
            for(int j=0;j<listJoueurs.get(i).getList().size();j++){
                listeVar.add(listJoueurs.get(i).getList().get(j));
            }
        } 
        return listeVar;  
    }

    public void initialiserCases(){
        int var=0;
        for(int i=0;i<NB_CASE;i++){
            int GAIN=(int)(Math.random()*NB_CASE);
            if(GAIN%5==0 &&  var< nbObstacles){
                var++;
                Obstacle obs=new Obstacle(GAIN/2);
                cases[i]=new Case(GAIN, obs);
            }
            else{
                cases[i]=new Case(GAIN);
            }
        }
    }

    public int[] gagnant(){
        int max=0;
        int[] gagnant=new int[2];
        for(int i=0;i<listJoueurs.size();i++){
            if(listJoueurs.get(i).getNbPoint()>max){
                max=listJoueurs.get(i).getNbPoint();
                gagnant[0]=i;
                gagnant[1]=max;
            }
        }
        return gagnant;
    }

    public void lancerJeu(){
        int deroulement=0;
        initialiserCases();

        for(int i=0;i<tousLesPerso().size();i++){
            int j=0;
            while (!(cases[j].estLibre())){
                j++;
            }
            tousLesPerso().get(i).deplacer(j,cases[j].GAIN);
            cases[j].placerPersonnage(tousLesPerso().get(i));
        }
        while (deroulement<nbEtapes){
            for(int i=0;i<tousLesPerso().size();i++){
                int pos=tousLesPerso().get(i).positionSouhaitee();
                if(tousLesPerso().get(i).getPosition()==NB_CASE-1){
                    cases[NB_CASE-1].enleverPersonnage();
                    tousLesPerso().get(i).deplacer(pos%NB_CASE, cases[pos%NB_CASE].GAIN);;
                }else{
                    if(tousLesPerso().get(i).getPosition()+pos>NB_CASE-1){
                        tousLesPerso().get(i).deplacer(NB_CASE-1,cases[NB_CASE-1].GAIN);
                        cases[NB_CASE-1].placerPersonnage(tousLesPerso().get(i));
                    }else{
                        if(cases[pos].estLibre()){
                            cases[tousLesPerso().get(i).getPosition()].enleverPersonnage();
                            tousLesPerso().get(i).deplacer(pos, cases[pos].GAIN);
                            cases[pos].placerPersonnage(tousLesPerso().get(i));
                        }
                        else{
                            if(!(cases[pos].sansObstacle())){
                                tousLesPerso().get(i).penaliser(cases[pos].getPenalite());
                            }
                            else if (!(cases[pos].sansPerso())){
                                tousLesPerso().get(i).penaliser(-(cases[pos].GAIN)/2);
                            }
                        }
                    }
                    
                }
            }
            deroulement++;
        }
        
        if (gagnant()[1]>scoreMax){
            ancien=scoreMax;
            scoreMax=gagnant()[1];
            changer=true;
            
        }
        afficherResultat();
    }

    public void afficherCases(){
        for(int i=0;i<NB_CASE-1;i++){
            System.out.println("Case "+i+" : "+cases[i]);
        }
    }

    public void afficherParticipants(){
        System.out.println("LISTE DES JOUEURS");
        for(int i=0;i<listJoueurs.size();i++){
            System.out.println("--------------------------------\n");
            System.out.println(listJoueurs.get(i));
        }
    }

    public void afficherResultat(){
        //afficherCases();
        afficherParticipants();
        System.out.println("JEU "+titre);
        System.out.println("*************************************");
        System.out.println("RESULATS");
        System.out.println("Le gagnant est "+listJoueurs.get(gagnant()[0]));
        if(changer){
            System.out.println("Record battu: Ancien score maximum "+ancien);
        }
        
    
        
    }


}


