package atelier_6.exo_1;

import java.util.Random;

public class De {
    private String nom;
    private int nb_faces;
    private static final int INF=3;
    private static final int SUP=120;
    private static int nb_de=0;
    private int memoire;

    public De(String nom,int nb_faces){
        this.nom=nom;
        memoire=0;
        if (nb_faces>SUP || nb_faces<INF){
            System.err.println("nombre pas entre les borne");
        }
        else{
            this.nb_faces=nb_faces;
            nb_de+=1;
        }
    }

    public De(){
        nb_de+=1;
        memoire=0;
        this.nom="De"+nb_de;
        this.nb_faces=6;
    }

    public De(String nom){
        nb_de+=1;
        memoire=0;
        this.nom=nom;
    }

    public int GetNbfaces(){
        return this.nb_faces;
    }

    public void SetNbfaces(int modif){
        if (modif>INF && modif<SUP){
            this.nb_faces=modif;
        }
        else{
            System.err.println("nombre pas entre les borne");
        }
    }

    public String GetNom(){
        return this.nom;
    }

    public int lancer(){
        Random rand =new Random();
        return rand.nextInt(0,this.GetNbfaces());
    }

    public int lancer(int nb){
        int max=0;
        Random rand =new Random();
        for(int i=0;i<nb;i++){
            int r=rand.nextInt(3,this.GetNbfaces());
            if (r>max){
                max=r;
            }
        }
        return max;
    }

    public String toString(){
        return "Dé : "+GetNom()+" nombre de faces: "+GetNbfaces();
    }

    public boolean equals(De autre){
        return (GetNom()==autre.GetNom() && GetNbfaces()==autre.GetNbfaces());
    }

    public int lancerM(){
        int a=lancer();
        while (a == this.memoire){
            a=lancer();
        }
        this.memoire=a;
        return a;
    }
}

