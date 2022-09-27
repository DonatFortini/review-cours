package atelier_8;

public class Obstacle {
    public final int PENALITE;

    Obstacle(int valeur){
        if(valeur>0){
           PENALITE=-valeur; 
        }else{
            PENALITE=-1;
        }
    }

    public int getPenalite(){
        return PENALITE;
    }
}
