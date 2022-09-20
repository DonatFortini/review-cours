package atelier_5.exo_2;
import java.lang.Math;

public class Vecteur3d {
    private double x,y,z;
    private String nom;


    public Vecteur3d(String nom,double x,double  y,double z){
        this.nom=nom;
        this.x=x;
        this.y=y;
        this.z=z;
    }

    public Vecteur3d(String nom){
        this.nom=nom;
        this.x=0;
        this.y=0;
        this.z=0;
    }

    public String toString(){
        return "vecteur"+this.nom+" <"+this.x+","+this.y+","+this.z+">";
    }

    public double norme(){
        return Math.sqrt(((this.x*this.x)+(this.y*this.y)+(this.z*this.z)));
    }

    public double scalaire(Vecteur3d vect2){
        return (this.x*vect2.x+this.y*vect2.y+this.z*vect2.z);
    }

    public String somme(Vecteur3d vect2){
        return "<"+(this.x+vect2.x)+","+(this.y+vect2.y)+","+(this.z+vect2.z)+">";
    }

    public static String somme2(Vecteur3d vect1,Vecteur3d vect2){
        return "<"+(vect1.x+vect2.x)+","+(vect1.y+vect2.y)+","+(vect1.z+vect2.z)+">";
    }

    public static double scalaire2(Vecteur3d vect1,Vecteur3d vect2){
        return (vect1.x*vect2.x+vect1.y*vect2.y+vect1.z*vect2.z);
    }
}
