package atelier_6.exo_2;

public class Entier {
    public final int INF,SUP;
    private int valeur;
    
    public Entier(int INF ,int SUP,int valeur){
        this.INF=INF;
        this.SUP=SUP;
        this.valeur=valeur;
    }

    public Entier(int INF ,int SUP){
        this(INF,SUP,0);
    }

    public void setValeur(int val){
        if(val<INF || val>SUP ){
            System.err.println("valeur pas dans les bornes");
        }
        else{
            this.valeur=val;
        }
    }

    public int[] getBorne(){
        int[] results={this.INF,this.SUP};
        return results;
    } 

    public void incremente(){
        incremente(1);
    }

    public void incremente(int n){
        if((this.valeur+n)<=SUP){
            this.valeur+=n;
        }
    }

    public String toString(){
        return "Borne: INF = "+this.INF+" SUP = "+this.SUP+" valeur = "+this.valeur;
    }

    public boolean equals(Object autre){
        if(autre!=null && autre instanceof Entier){
            Entier objectDe=(Entier)autre;
            return (this.valeur==objectDe.valeur && this.getBorne()==objectDe.getBorne());
        }
        return false;
        
    }
}
