---
title: Comment intégrer les IAG dans les compétences informationnelles des étudiants
---

# 1. Casser l'assimilation IA = ChatGPT

## une histoire ancienne mais non linéaire de l'intelligence artificielle

L'histoire des IA ne commence pas avec le lancement auprès du grand public du chatbot ChatGPT, elle remonte au lendemain de la seconde guerre mondiale et comporte des phases d'innovation et d'intense activité scientifique (années 50 et 60 puis année 80 et enfin année 2000 à nos jours) et des périodes de pause (financements en baisse, perte de visibilité de l'IA au profit de l'informatique "classique") qu'on appelle des "hivers de l'IA"

<iframe name="ngram_chart" src="https://books.google.com/ngrams/graph?content=artificial+intelligence&year_start=1945&year_end=2022&corpus=en&smoothing=3&case_insensitive=false#" width=900 height=500 marginwidth=0 marginheight=0 hspace=0 vspace=0 frameborder=0 scrolling=no></iframe>

## proposer aux étudiants de se tester sur les différentes phases de l'IA


<iframe width="900" src="https://damienbelveze.github.io/CFCB_IA/histoire_ia.html" frameBorder="0" scrolling="no" styles="width:100%"></iframe>

:note: Si l'activité h5P n'apparaît pas clairement à l'écran, afficher la [page correspondante](histoire_ia.html)


(dispositif pédagogique : timeline IA ?)
activité "drag the words" pour H5P constituée à partir du prompt suivant : 

```markdown

// utilisation du LLM Claude-3.5 Sonnet à partir du chatbot de poe (https://poe.com)

Voici un tableau avec une liste de dates et une liste d'événements. A partir de ces données, produis du texte qui intégré à H5P permette d'obtenir le résultat suivant :
une activité Drag the words pour H5P dans laquelle : les énoncés de la colonne événements sont proposés en ordre aléatoire, chacun sur une seule ligne.
Les dates de la première colonne constituent les mots à déplacer. l'espace où chaque date doit être placée suit la ligne relative à chaque événement

| date | événement |
| :---: | :---:|
| 1965 | Hubert Dreyfus publie une critique de la notion d'IA en contestant le fait que l'intelligence ne soit réduite qu'à une simple fonction de calcul |
| 1966 | Eliza, le premier chatbot voit le jour |
| 2009 | Fei Fei Li initie ImageNet, l'une des plus grandes bases ouvertes d'images du web |
| 2011 | Siri, l'assistant vocal d'Apple débarque dans les maison |
| 1950 | Un test voit le jour pour déterminer si on a affaire à une machine ou à un humain |
| 1956 | Le terme d'"intelligence artificielle" fait son apparition à la conférence de Dartmouth College
| 1957 | Frank Rosenblatt invente à l'Université Cornell le premier algorithme d'apprentissage supervisé au moyen d'un réseau de neurones, le Perceptron[^1]
| 1997 | Deep Blue bat Kasparov aux échecs
| 2012 | Suite à des plaintes, Facebook ferme son système de reconnaissance faciale qu'il avait ouvert l'année précédente |
| 2016 | Des IA traitent des données provenant de réseaux sociaux pour influencer le vote des électeurs |
| 2019 | Le Allen Institute fait paraître le premier article ("Green AI") qui mesure directement l'impact environnemental suscité par les IA 
| 2023 | Llama 2 un modèle de langage aussi puissant que GPT est mis à la disposition des internautes par Facebook |
```


## Commentaire de l'activité

| date | événement |
| :---: | :---:|
| 1965 | Hubert Dreyfus publie une critique de la notion d'IA en contestant le fait que l'intelligence ne soit réduite qu'à une simple fonction de calcul [^2] |
| 1966 | Eliza, le premier chatbot voit le jour [^3] |
| 2009 | Fei Fei Li initie ImageNet, l'une des plus grandes bases ouvertes d'images du web |
| 2011 | Siri, l'assistant vocal d'Apple débarque dans les maison |
| 1950 | Un test voit le jour pour déterminer si on a affaire à une machine ou à un humain [^4] |
| 1956 | Le terme d'"intelligence artificielle" fait son apparition à la conférence de Dartmouth College
| 1957 | Frank Rosenblatt invente à l'Université Cornell le premier algorithme d'apprentissage supervisé au moyen d'un réseau de neurones, le Perceptron[^1]
| 1997 | Deep Blue bat Kasparov aux échecs
| 2012 | Suite à des plaintes, Facebook ferme son système de reconnaissance faciale qu'il avait ouvert l'année précédente [^6]|
| 2016 | Des IA traitent des données provenant de réseaux sociaux pour influencer le vote des électeurs [^7] |
| 2019 | Le Allen Institute fait paraître le premier article ("Green AI") qui mesure directement l'impact environnemental suscité par les IA [^5] 
| 2023 | Llama 2 un modèle de langage aussi puissant que GPT est mis à la disposition des internautes par Facebook |

Cette série de dates a été sélectionnée à partir de deux sources : une activité de la Bataille de l'IA (association Latitudes), proposée aux futurs animateurs et de la [vidéo](https://youtu.be/qmwJx-r5vmw?si=6Ss2Ka3xD_EeuOZk) du CEA intégré dans le cours consacré par les bibliothécaires de Science Po Lyon à l'IA (@ceaHistoireSciencesLhistoire2018)  


# 2. distinguer le chatbot du modèle de langage. 

voir [définitions](definitions.md)

# 3. Utiliser chaque outil pour ce pour quoi il est vraiment fait

ChatGPT n'est pas fait pour faire de la traduction de texte. Deepl est fait pour de la traduction. 

_______________________

[^1]:  "les machines informatiques pensent avec un langage qui est celui des nombres ; nous transformons tout en chiffre pour les faire fonctionner. Elles sont nulles en matière de perception. Elles n'ont pas de langage naturel sous-jacent, comme nous ou les animaux. Lorsqu'on veut les faire développer un modèle de monde autour d'elles-mêmes, on s'aperçoit que ce n'est pas le bon dispositif.
Vous voulez qu'elles jouent aux échecs, très bien. Notre programme de jeux d'échec au MIT est déjà un joueur de 2e rang ; dans un an je pense qu'il sera de 1er rang ; ce sera pas un maitre au bout d'un an mais dans six ans environ. Dans six ans, il deviendra une technologie de 1er rang qu'aucun humain ne pourra dépasser.
Je souhaite que ca aille plus loin, et ça ira plus loin, car nous pouvons réduire ces choses là à des nombres"
(Warren McCulloch)

[^2]: On peut discuter en effet de la notion d'intelligence appliquée à une machine qui se livre à des calculs sur des mots ("calculette de mots", "perroquet stochastique"). On peut dire que le propre d'une IA est de simuler l'intelligence humaine, mais la comparaison entre un réseau de neurones biologique et son équivalent dans le champ de l'IA est très imparfaite. 

[^3]: On peut toujours discuter avec Eliza dans une interface un peu modernisée (http://eliza.botlibre.com/) on se rend assez vite compte qu'Eliza échoue au bout de peu de temps à passer le test de Turing. 

[^4]: Il s'agit bien sûr du fameux test de Turing qui permet de distinguer un humain d'une machine avec laquelle on joue pour la faire passer pour un humain ("imitation game")

[^5]: permet d'inclure les préoccupations reliées aux émissions de GES et à la consommation d'eau et de minéraux des outils d'IA (voir [enjeux environnementaux](enjeux_ethiques_environnementaux.md) )

[^6]: introduis les aspects éthiques de l'IA. L'IA capte les données personnelles, elle permet aussi dans bien des endroits de surveiller les salariés, voire des populations entières (cf. caméras à reconnaissance faciale installées dans certaines villes dont Paris depuis les Jeux Olympiques)

[^7]: il s'agit évidemment de l'affaire Cambridge Analytica. Les IA peuvent être déployées pour influencer le vote des électeurs dans des campagnes de PsyOps. (voir [enjeux environnementaux](enjeux_ethiques_environnementaux.md)
