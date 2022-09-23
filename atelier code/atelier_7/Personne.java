package atelier_7;

import java.util.*;

public class Personne{
    private static final Adresse ADRESSE_INCONNUE = null;
    private String nom;
    private String prenom;
    private final GregorianCalendar dateNaissance;
    private Adresse adresse=ADRESSE_INCONNUE;
	private static int nombrePersonne=0;
		
	/**
	 * Constructeur de Personne
	 * @param leNom le nom de la personne
	 * @param lePrenom le pr�nom de la personne
	 * @param laDate la date de naissance de la personne
	 * @param lAdresse l'adresse de la personne
	 */
	public Personne(String leNom,String lePrenom, GregorianCalendar laDate, Adresse lAdresse){
		nom = leNom.toUpperCase();
		prenom=lePrenom;
		dateNaissance=laDate;
		adresse=lAdresse;
		nombrePersonne+=1;
	}
	
	/** 
	 * Constructeur de Personne
	 * @param leNom le nom de la personne
	 * @param lePrenom le pr�nom de la personne
	 * @param j le jour de naissance
	 * @param m le mois de naissance
	 * @param a l'ann�e de naissance
	 * @param numero le n� de la rue
	 * @param rue la rue
	 * @param code_postal le code postal de l'adresse
	 * @param ville la ville ou la personne habite
	 */
	public Personne(String leNom,String lePrenom, int j, int m, int a, int numero, String rue, String code_postal, String ville){
		this(leNom, lePrenom, new GregorianCalendar(a,m,j),new Adresse(numero,rue,code_postal,ville));
	}

	/**
	 * Accesseur
	 * @return retourne le nom
	 */
	public String getNom(){
		return nom;
	}
	/**
	 * Accesseur
	 * @return retourne le pr�nom
	 */
	public String getPrenom(){
		return prenom;
	}
	/**
	 * Accesseur
	 * @return retourne la date de naissance	 
	 */
	public GregorianCalendar getDateNaissance() {
		return dateNaissance;
	}
	/**
	 * Accesseur
	 * @return retourne l'adresse	 
	 */
	public Adresse getAdresse() {
		return adresse;
	}
	/**
	 * Modificateur
	 * @param retourne l'adresse	 
	 */
	public void setAdresse(Adresse a) {
		adresse=a;
	}
		
	/* (non-Javadoc)
	 * @see java.lang.Object#toString()
	 */
	public String toString(){
		String result="\nNom : "+nom+"\n"
		+"Prénom : "+prenom+"\n"+
		"Né(e) le : "+dateNaissance.get(Calendar.DAY_OF_MONTH)+
		"-"+dateNaissance.get(Calendar.MONTH)+
		"-"+dateNaissance.get(Calendar.YEAR)+"\n"+
		"Adresse : "+
		adresse.toString();
		return result;
	}

	public static boolean plusAgee(Personne p1,Personne p2){
		return p1.dateNaissance.before(p2.dateNaissance);
	}

	public boolean plusAgee(Personne p2){
		return this.dateNaissance.before(p2.dateNaissance);
	}

	public boolean equals(Object personne){
		if(personne instanceof Personne){
			Personne test= (Personne)personne;
			return this.nom.equals(test.nom) && this.dateNaissance.equals(test.dateNaissance) && this.prenom.equals(test.prenom);
		}
		return false;
	}

	public static int quelAge(Personne perso){
		GregorianCalendar dateDuJour=new GregorianCalendar();
		int depart =perso.dateNaissance.get(perso.dateNaissance.YEAR);
		int arrive= dateDuJour.get(dateDuJour.YEAR);
		int age=arrive-depart-1;
		if (perso.dateNaissance.get(perso.dateNaissance.MONTH)==dateDuJour.get(dateDuJour.MONTH)){
			if(perso.dateNaissance.get(perso.dateNaissance.DAY_OF_MONTH)>=dateDuJour.get(dateDuJour.DAY_OF_MONTH)){
				age+=1;
			}
		}
		else if(perso.dateNaissance.get(perso.dateNaissance.MONTH)<dateDuJour.get(dateDuJour.MONTH)){
			age+=1;
		}

		return age;
	}
}


    
   
   