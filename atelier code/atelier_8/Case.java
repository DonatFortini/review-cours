package atelier_8;

public class Case {
    public final int GAIN;
    private Personnage perso=null;
    private Obstacle obs=null;

    public Case(int GAIN,Obstacle obs){
        this.GAIN=GAIN;
        this.obs=obs;
    }

    public Case(int GAIN){
        this(GAIN,null);
    }

    public int getPenalite(){
        if(obs!=null){
            return obs.getPenalite();
        }
        return 0;
    }

    public void placerPersonnage(Personnage perso){
        this.perso=perso;
    }

    public void placerObstacle(Obstacle obs){
        this.obs=obs;
    }

    public void enleverPersonnage(){
        this.perso=null;
    }

    public boolean estLibre(){
        return sansObstacle()&& sansPerso();
    }

    public boolean sansObstacle(){
        return this.obs==null;
    }

    public boolean sansPerso(){
        return this.perso==null;
    }

    public String toString(){
        if(estLibre()){
            return "Libre (gain= "+GAIN+")";
        }
        else if(!(sansObstacle())){
            return "Obstacle (penalité= "+obs.getPenalite()+")";
        }
        else{
            return perso+" (penalité= "+(-GAIN)+")";
        }
    }
    

}

