package atelier_5.exo_1;


public class Robot {
    private String reference="ROB";
    private String nom;
    private int x,y;
    private int cardinaux;
    private static int nb_robot=0;

    public Robot(String nom,int x,int y,int cardinaux){
        nb_robot+=1;
        this.reference+=nb_robot;
        this.cardinaux=cardinaux;
        this.x=x;
        this.y=y;
        this.nom=nom;
    }

    public Robot(String nom){
        this.x=0;
        this.y=0;
        this.nom=nom;
        this.cardinaux=1;
        nb_robot+=1;
        this.reference+=nb_robot;

    }

    public void change_dir(int nouvelle_dir){
        this.cardinaux=nouvelle_dir;
    }

    public void deplacement(){
        switch(this.cardinaux){
            case 1:
                this.y+=1;
                break;
            case 2:
                this.x+=1;
                break;
            case 3:
                if (this.y!=0){
                    this.y-=1;
                    break;
                }
                break;
            case 4:
                if (this.x!=0){
                    this.x-=1;
                    break;
                }
                break;
        }
    }

    public String dir(int direction){
        if (direction==1){
            return "nord";
        }
        else if (direction==2){
            return "est";
        }
        else if (direction==3){
            return "sud";
        }
        else{
            return "ouest";
        }
    }

    public String affiche_toi(){
        return "ref: "+this.reference+" nom: "+this.nom+" direction: "+dir(this.cardinaux)+" coord: ( x:"+this.x+" y:"+this.y+" )";
    }

    public String toString(){
        return "ref: "+this.reference+" nom: "+this.nom+" direction: "+dir(this.cardinaux)+" coord: ( x:"+this.x+" y:"+this.y+" )";
    }
}

