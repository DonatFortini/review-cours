package atelier_6.exo_1;

public class TestDe {
    public static void main(String[] args) {
        De d1=new De();
        De d2=new De("deufaces");
        De d3=new De("neufaces",9);
        System.out.println(d3);
        System.out.println(d1);
        d2.setNbFaces(2);
        d2.setNbFaces(8);
        System.out.println(d2);
        d1.setNbFaces(4);
        System.out.println("--------------------------------------------\n");
        System.out.println(d1.lancer());
        System.out.println(d2.lancer());
        System.out.println(d3.lancer());
        System.out.println("--------------------------------------------\n");
        De d4=new De();
        System.out.println(d4);
        System.out.println("--------------------------------------------\n");
        System.out.println(d3.lancer(5));
        System.out.println("--------------------------------------------\n");
        De d5=new De("neufaces",9);
        System.out.println(d3.equals(d5));
        System.out.println(d3.equals(d4));
        System.out.println("--------------------------------------------\n");
        DeMemoire d6 =new DeMemoire("demem",9);
        for(int i=0;i<5;i++){
            System.out.println(d6.lancer());
        }
        System.out.println("--------------------------------------------\n");
        DePipe pipe=new DePipe("pipe",10,4);
        System.out.println(pipe);
        for(int i=0;i<5;i++){
            System.out.println(pipe.lancer());
        }
        System.out.println("--------------------------------------------\n");
        DeFaceAutre demot=new DeFaceAutre("dé_mot");
        System.out.println(demot);
        System.out.println("--------------------------------------------\n");
        DeImpaire deimp=new DeImpaire("deImp", 9);
        System.out.println(deimp);
        for(int i=0;i<4;i++){
            System.out.println(deimp.lancer());
        }
    }
}
