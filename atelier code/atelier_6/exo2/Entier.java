package atelier_6.exo2;

public class Entier {
    public final int inf,sup;
    private int valeur;
    
    public Entier(int inf ,int sup,int valeur){
        this.inf=inf;
        this.sup=sup;
        this.valeur=valeur;
    }

    public Entier(int inf ,int sup){
        this.inf=inf;
        this.sup=sup;
        valeur=0;
    }

    public void setValeur(int val){
        if(val<getBorne()[0] || val>getBorne()[1] ){
            System.err.println("valeur pas dans les bornes");
        }
        else{
            this.valeur=val;
        }
    }

    public int[] getBorne(){
        int[] results={this.inf,this.sup};
        return results;
    } 

    public void incremente(){
        if((this.valeur + 1)<=getBorne()[1]){
            this.valeur+=1;
        }
    }

    public void incremente(int n){
        if((this.valeur+n)<=getBorne()[1]){
            this.valeur+=n;
        }
    }

    public String toString(){
        return "Borne: inf = "+this.inf+" sup = "+this.sup+" valeur = "+this.valeur;
    }

    public boolean equals(Entier autre){
        return this.valeur==autre.valeur;
    }
}
