## journal de bord
#### 31 mars 2023
- exploration des données sur pandas + nettoyage (on a du se débarrasser de quelques colonnes vides/inutiles)
    - ajout du notebook jupyter `explore_data.ipynb` avec nos débuts.
- seulement 1239 questions sont annotées : on considère l'annotation manuelle pour compléter notre corpus
    autres statistiques : 
    - 1239 questions annotées
    - 554 questions "poubelle" ou "non-question"
<<<<<<< HEAD
    
#### 14 avril 2023
Premier essai algo k-means clustering :
- à partir du git : https://github.com/lucas-de-sa/national-anthems-clustering
	- méthode : pré-process, plongement de mot, kmeans
	- résultat : deux clusters, fréq mots (un cluster + intéressant que l'autre ?). pas très pertinents. graphs : most common words, word cloud.
- TXM : peut potentiellement remplacer IRAMUTEQ, mais produit des graphes moins intéressants. à voir + tard.
À tester : 
- n-grammes : travailler les questions en séquences de mots (vectorisation des mots fait qu'on perd la structure des questions qu'on cherche à étudier)
- algo kmeans sur chacun des sous corpus (séparer les résultats ?)
- jouer avec les paramètres du kmeans (cf. sklearn)
=======

#### 6 Avril 2023
- re-origanisation des corpus et nettoyage
- Essai des annotations morpho-syntaxique des corpus 


#### 13 Avril 2023
- Prétraitement des données pour être adaptable à l'entraînement
- test en Python les clustering par le biais de la méthode de `kmeans`
-
>>>>>>> xinhao-km
