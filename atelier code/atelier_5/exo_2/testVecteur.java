package atelier_5.exo_2;

public class testVecteur {
    public static void main(String[] args) {
        Vecteur3d v1=new Vecteur3d("v1");
        Vecteur3d v2=new Vecteur3d("v2", 3, 2, 5);
        Vecteur3d v3=new Vecteur3d("v3", 1, 2, 3);
        System.out.println(v1);
        System.out.println(v2);
        System.out.println(v3);
        System.out.println("v2+v3= "+v2.somme(v3));
        System.out.println("v2.v3= "+v2.scalaire(v3));
        System.out.println("norme v2= "+v2.norme());
    }
}
