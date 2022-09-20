package atelier_5.exo_1;

public class testRobot {
    public static void main(String[] args) {
        Robot t=new Robot("titi");
        Robot t2=new Robot("toto", 10, 20, 3);
        System.out.println(t.affiche_toi());
        System.out.println(t2.affiche_toi());
        System.out.println(t2);
        t.change_dir(3);
        t.deplacement();
        System.out.println(t);
        t.change_dir(1);
        t.deplacement();
        System.out.println(t.affiche_toi());
        t2.deplacement();
        System.out.println(t2.affiche_toi());

    }
}
