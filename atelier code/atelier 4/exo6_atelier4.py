##question 1
# application de l'algorithme de tri a bulle
def sort_list(liste_a_trie:list)->list:
    liste_copy=liste_a_trie.copy()
    for element in liste_a_trie:
        for i in range(len(liste_a_trie)-1):
            if liste_copy[i]>liste_copy[i+1]:
                liste_copy[i],liste_copy[i+1]=liste_copy[i+1],liste_copy[i]
    return liste_copy

##question 2