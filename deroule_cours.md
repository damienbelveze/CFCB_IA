<!--

title: "Aider les étudiants à prendre du recul par rapport à leurs usages des outils d'IA "  

author: Damien Belvèze

date: Décembre 2024

email: damien.belveze@univ-rennes.fr 

language: fr 

link: lia.css

comment: ce support s'adresse à des personnels de bibliothèque, formateurs et professionnels de la documentation. 

import: https://raw.githubusercontent.com/LiaTemplates/citations/main/README.md

@onload
// this shall load an entire file at starttime that can be referenced
setTimeout(() => { window.bibliographyLoad("https://raw.githubusercontent.com/LiaTemplates/citations/main/bibtex.bib")}, 100)
@end

-->



# 1. Bienvenue

<img src="images/jorgi.jpg" alt="jorgi, un personnage de Papers, please" width="100px">

<div class="prez">
Damien belvèze, Service Commun de Documentation, Université de Rennes
</div>

## 1.1 Présentation du formateur

<div class="prez">

                    {{0}}
  Formations en bibliothèque universitaire  

                    {{1}}
  Culture numérique (Dominique Cardon / Marcelo Vitali-Rosati)  

                    {{2}}
  Logiciel libre (et émancipateur)  

                    {{3}}
  biais anticapitaliste et environnementaliste  


</div>

## 1.2 Enjeux


<div class="prez">
                    {{0}}

- Formations en bibliothèque universitaire 

        <span class="blue">On ne peut pas interdire aux étudiant.e.s d'utiliser des IAG</span>

                    {{1}}

- Culture numérique (Dominique Cardon / Marcelo Vitali-Rosati)

        <span class="blue"> Le recours massif aux IAG comporte un risque d'appauvrir les pratiques numériques des étudiants et de substituer une IAG à plusieurs services existants qui font mieux le travail</span>

                    {{2}}

- Logiciel libre (et émancipateur)

        <span class="blue"> Les IAG grand public à visée commerciale exploitent nos données et constituent des boîtes noires. Elles amplifient les biais et les préjugés déjà présents dans la société</span>

                    {{3}}

- biais anticapitaliste et environnementaliste

        <span class="blue">Les IAG se développent principalement aux USA, en Europe et en Chine, laissant les autres pays loin derrière. Elles agrandissent la fracture Nord / Sud. Elles sont promues par des entreprises capitalistes qui n'ont aucun souci de leur empreinte carbone. Le développement des IAG accroît la dette carbone de notre planête de manière drastique </span>

</div>

## 1.3 Réponses au questionnaire

                    {{0}}

votre établissement a t-il une politique ou une charte en matière d'usage des outils d'Intelligence Artificielle Générative (IAG) ? tels ChatGPT

![](charts/question1.png)

                    {{1}}

A quel point les notions ci-dessous vous sont familières : valeurs de 1 à 5 : 1 = Je n'en ai pas entendu parler 5 = Je saurais expliquer en quoi cela consiste à un.e étudiant.e

**Grand Modèle de Langage (LLM)**

![](charts/question2.png)

**Vectorisation**

![](charts/question3.png)

**tokenisation**

![](charts/question4.png)


## 1.4 premiers retours sur les usages des IAG par les étudiants dans le cadre de leurs études

### Enquête Pôle De Vinci (avril 2024)

<div class="prez">

                {{0}}

Etude auprès de 1600 étudiants du Pôle Léonard de Vinci (3 écoles privées du Supérieur)

```bibtex @cite
@book{massiasEtude2024LImpact2024,
        title = {Etude 2024 : L'Impact Des IA Génératives Sur Les Etudiants},
        author = {Massias, Joachim},
        year = {2024},
        url = {https://open.devinci.fr/ressource/etude-2024-impact-ia-generatives-etudiants/}
}
```

        - usage régulier : 92%  
        - usage quotidien : 30%  
        - **usage d'outils payants (GPT4) : 30%**  

                {{1}}

        - 52% constatent que ChatGPT les influence dans leurs choix  
        - 66% des répondants sont sensibles au fait que ChatGPT charrie des références culturelles et des biais nord-américains  
        - 59% constatent que ChatGPT fait des erreurs  

        - 65% estiment que le fait que l'employeur mette à disposition des IAG aux employés fait partie de leurs critères de choix pour leur futur emploi 

                {{2}}

        - 49% des étudiants considèrent que les IAG peuvent constituer un risque pour la démocratie

        - <div class="blue">51% des étudiants admettent qu'ils ont du mal à se passer de ChatGPT</div>

                {{3}}

        L'échantillon n'est peut-être pas représentatif : certaines disciplines, une certaine aisance des étudiants qui ont pu faire le choix d'écoles privées coûteuses.

</div>

### Enquête Gresec

<div class="prez">

                {{0}}

Résultats présentés par Zhuoran Ma, Gresec, à la 9ème conférence Doc&Soc de septembre 2024 à Grenoble.

```bibtex @cite
@book{maLintegrationOutilsDintelligence2024,
	address = {Genève},
	title = {L’intégration des outils d’intelligence artificielle dans la production académique étudiante : dynamiques, perspectives et enjeux},
	author = {Ma, Zhuoran},
	month = sep,
	year = {2024},
        url = {https://docsoc2024.sciencesconf.org/}
}
```



                {{1}}

usage selon l'avancée dans les études

| Fréquentation | premier cycle | deuxième cycle |
|:--:|:--:|:--:|
|presque jamais | 48% | 35%  |
| au moins la moitié des travaux |  17%  |  33%  |


                {{2}}

Intensité des usages dans les travaux fournis par disciplines
![](images/zhuoran2.png)


                {{3}}

Arguments apportés par les non utilisateurs : <br>
- 63% préoccupations éthiques "ne veut pas tricher" <br> 
- 52% faible confiance dans les résultats  <br>
- 20% difficulté à maîtriser les outils  <br>
- 16% interdiction explicite de l'enseignant.e ou de l'établissement <br> 

Utilisation écrasante des générateurs de textes et parmi ceux-ci de ChatGPT


                {{4}}

Principaux usages et bénéfices rapportés : <br>
- Aide à écrire du code informatique  <br>
- Pour les non-francophones, améliorer le français, aide à rédiger en anglais  <br>
- Permet de mieux comprendre un sujet <br>  
- Permet de trouver de l'inspiration sur un thème particulier <br>  

           
                 {{5}}

![](images/zhuoran1.png)

</div>

### conséquences sur les enseignements 

![](images/memoires.png)

# 2. replacer les IAG dans l'Histoire de l'IA et dans le paysage de la Culture Numérique 

une histoire ancienne mais non linéaire de l'intelligence artificielle

L'histoire des IA ne commence pas avec le lancement auprès du grand public du chatbot ChatGPT, elle remonte au lendemain de la seconde guerre mondiale et comporte des phases d'innovation et d'intense activité scientifique (années 50 et 60 puis année 80 et enfin année 2000 à nos jours) et des périodes de pause (financements en baisse, perte de visibilité de l'IA au profit de l'informatique "classique") qu'on appelle des "hivers de l'IA".

<iframe name="ngram_chart" src="https://books.google.com/ngrams/graph?content=artificial+intelligence&year_start=1945&year_end=2022&corpus=en&smoothing=3&case_insensitive=false#" width=900 height=500 marginwidth=0 marginheight=0 hspace=0 vspace=0 frameborder=0 scrolling=no></iframe>

## 2.1 proposer aux étudiants de se tester sur les différentes phases de l'IA

Les deux activités qui suivent reposent sur le même principe : représenter les différentes étapes de l'évolution de l'intelligence artificielle en remontant de 1950 à nos jours. 
Si une activité ne fonctionne pas, vous pouvez tenter l'autre 

### Chronoquiz

<div class="prez">
[timeline de l'IA](https://www.chronoquiz.net/game/36)
</div>

![](images/chronoquiz.png)

### Drag and drop histoire de l'IA

<iframe width="800" height="1500" src="https://damienbelveze.github.io/CFCB_IA/histoire_ia.html" frameBorder="0" scrolling="no" styles="width:100%"></iframe>

Si l'activité h5P n'apparaît pas clairement à l'écran, afficher la <a href="activite_histoire_ia.html" target="_blank">page correspondante au quiz</a>)

## 2.2 IAG : le nouveau couteau suisse ? 

>avec un moteur à explosion, on peut faire des voitures (le moteur sert à faire tourner des roues) ou des tronçonneuses. Mais il n’est pas recommandé d’essayer de rentrer chez soi en utilisant une tronçonneuse. Mieux vaudrait utiliser une voiture. Or l’approche d’openIA – et des utilisateurs – semble consister à adopter la tronçonneuse pour faire aussi l’office de voiture: on ajoute des pneus autour de la chaîne, on construit des routes qui s’adaptent à des tronçonneuses

```bibtex @cite
@article{vitali-rosatiChatGPTTronconneuse2024,
  title = {ChatGPT et La Tronçonneuse},
  author = {Vitali-Rosati, Marcello},
  year = {2024},
  month = sep,
  journal = {Culture numérique. Pour une philosophie du numérique},
  urldate = {2024-09-24},
  abstract = {Blogue de Marcello Vitali-Rosati},
  howpublished = {http://blog.sens-public.org/marcellovitalirosati/chatgpttronconneuse.html},
  langid = {english},
  keywords = {IA}
}
```

```txt Question

Un étudiant entre des liens dans ChatGPT et demande au chatbot de lui restituer 
des références dans le style biblio de Nature. Que lui conseillez-vous ?

```

# 3 Maîtriser quelques concepts essentiels de l'IA avec Vittascience

                                {{0}}
Les activités suivantes seront proposées à partir du [site Vittascience](https://fr.vittascience.com/ia/)

![](images/vittascience.png)


## 3.1 Tokenisation  


                                {{0}}

La tokenisation consiste à débiter une phrase en unités de sens. 

longtemps je me suis couché de bonne heure

d'une certaine manière on pourrait découper la phrase de cette manière

| longtemps | je | me | suis | couché | de | bonne | heure |

Mais "de" ne constitue pas une unité de sens, c'est plutôt "de bonne heure" qui a une signification particulière dans la phrase. 

Pour autant "de bonne heure" est constitué de deux termes qui peuvent être utilisés dans d'autres textes de manière différente : "heure" et "bonne"

- une *bonne* pâtisserie  
- c'est l'*heure* de se réveiller  

par conséquent si le corpus contient plusieurs textes, on a tout intérêt à faire de ces mots des tokens. 

                                {{1}}

La numérisation du texte passe par les tokens, mais pas seulement. Si dans un corpus volumineux, tous les mots font l'objet de token, cette numérisation va prendre un temps considérable. Il convient donc de réduire le nombre de tokens pour faciliter ces calculs. Pour réduire les tokens, les systèmes vont assez souvent repérer les termes les plus utilisés, leur attribuer un token en particulier et conserver ce token dans des mots qui les contient. 

ainsi *bon* constituera un token, la terminaison de cet adjectif au féminin (-ne) un autre token. Cet autre token pourra aussi être attribué au terme *patron* -> | patron | ne |

Le fait d'associer deux tokens en fonction d'un contexte est ce qu'on appelle la vectorisation. 

```txt Activité

Avec combien de tokens, le chatbot répond t-il à la question "qui a tué le roi Henri IV" ?

```

## 3.2 vectorisation  

                                {{0}}

numériser le langage, ce n'est pas seulement numériser des mots, c'est aussi numériser le rapport qu'entretiennent ces mots dans un corpus de documents donné. 
Les mots transformés en vecteurs sont plus ou moins proches les uns des autres sous un certain rapport. 

Par exemple, le mot Apple est proche de Windows sous le rapport de l'informatique
le mot Apple est proche de banana sous le rapport de la nourriture
les mots Windows et banana sont distants l'un de l'autre dans un grand nombre de rapports. 

                                {{1}}

Pour passer d'un mot à un autre, le LLM est formé à faire des substitutions : 

royauté + homme = roi 
roi - homme + femme = reine

                                {{2}}

![](images/vectors.png)

```bibtex @cite
@misc{metzgerWhatAreTokens2022,
        title = {What Are Tokens, Vectors, and Embeddings \& How Do You Create Them?},
        author = {Metzger, Sascha},
        year = {2022},
        month = dec,
        journal = {Medium},
        urldate = {2024-11-24},
        abstract = {Understand the core concepts of each NLP project.},
        langid = {english},
        url = {https://medium.com/@saschametzger/what-are-tokens-vectors-and-embeddings-how-do-you-create-them-e2a3e698e037}
}

```


## 3.3 Température  

> Pour le cas de l’originalité: il est complètement débile de se demander si chatGPT, ou une autre application basée sur un LLM, est ou pas “créatif” ou “original”. Il faut d’abord se demander “qu’est-ce que j’entends exactement par “originalité”?” Si la réponse est bien formalisée, elle pourra être implémentée dans une approche algorithmique. 
La “température” utilisée dans une softmax me semble être une excellente définition d’originalité. Je ne dis pas que c’est la seule possible, loin de là, mais c’est une “bonne” définition, car elle est claire et non ambigüe.

```bibtex @cite
@misc{vitali-rosatiCreativiteLLM2024,
        type = {Blog de Marcello Vitali-Rosati},
        title = {La Créativité Des LLM},
        author = {{Vitali-Rosati}, Marcello},
        year = {2024},
        month = nov,
        journal = {Culture numérique. Pour une philosophie du numérique},
        urldate = {2024-11-27},
        abstract = {Blogue de Marcello Vitali-Rosati},
        langid = {english},
        file = {/home/dbelveze/Zotero/storage/HGXFXP44/creativitellm.html},
        url = {http://blog.sens-public.org/marcellovitalirosati/creativitellm.html}
}
```

*Softmax* = algorithme permettant d'introduire une part d'aléatoire plus ou moins grande et souvent paramétrable pour l'usager dans la succession des tokens. Plus l'aléatoire est faible et plus la suite de caractères est déterministe et s'éloigne
très peu des cas majoritaires dans les données d'entraînement. (Dans
Vittascience, les jetons les plus déterministes sont en vert foncé).
Plus cet aléatoire est grand et plus le résultat sera éloigné de ce
déterminisme. On aura des textes plus "créatifs" souvent illisibles
quand la température est poussée à son maximum.

```text Question

Dans le chatbot que vous utilisez, savez-vous si vous pouvez changer la température ? 
et si oui, comment ?

``` 

<p><img src="images/haikus.png" class="img-fluid figure-img" /></p>
<figcaption>haikus réalisés par Mixtral</figcaption>

```text Activité

Dans Vittascience, faire un haïku sur un sujet de votre choix (par
exemple la pluie en Bretagne) avec une température faible (20%) et
envoyez la même instruction avec une température élevée (75%) ; comparez
les résultats. Lequel préférez-vous ?

Les token verts manifestent les probabilités les plus hautes, les tokens
rouges, les probabilités les plus basses (le vert clair et le rose
correspondent à des valeurs médianes entre ces deux extrêmes). Plus la
température est haute, plus le rose et le rouge abondent.

```

Question : si je souhaite publier ces haïkus, est-ce que je peux le
faire et toucher des droits d'auteur sur ma publication ? Qui est auteur
dans ce cas :

-   moi en tant qu'auteur du prompt ?

-   vittascience en tant que concepteur du site ?

-   Mistral en tant que concepteur du LLM Mixtral avec lequel j'ai généré le prompt ?

Un LLM est une "calculette de mots" qui fonctionne sur la base de
rapprochements statistiques entre des mots qui se retrouvent dans des
contextes identiques. Cela implique que tous les [tokens](#jetons)
soient convertissables en nombres.

Par exemple, ce prompt généré par Mistral avec le Chatbot de
[Vittascience](https://fr.vittascience.com/) :

<img src="images/mistral1.png" width="300%">

correspond dans le LLM Mistral à cette suite de nombres :

<img src="images/mistral2.png" width="300%">

Le terme "la" correspond à deux tokens différents : 

- l'adjectif ou le pronom la avec un l minuscule (token id = 1675) 
- l'adjectif (plus rarement le pronom) La avec un L majuscule (token id = 2486) 

Le point correspond au token id 13. Après le token ID 13 (le point), la probabilité que survienne le la minuscule est bien plus réduite que
celle que survienne le La majuscule. Comme tenu que la question posée
était : "quelle est la première femme à avoir été dans l'espace ?" La
probabilité que la réponse commence par "La première femmme, etc." est
importante, mais plus forte encore que la réponse commence par un *L*
majuscule après un point. En l'occurrence, le modèle statistiquement ne
permettait pas de débuter la réponse autrement que par un *La*, un *Le*
ou un *L'*


<p><img src="images/mistral3.png" class="img-fluid figure-img" alt="en jaune, le tokenID de *, en orange, le tokeID
de -La-"/></p>

## 3.4 Renforcement  

cf. question d'Apostolos Gerasoulis à propos du moteur de recherche Ask Jeeves : 

> Qu'adviendra t-il si nous répondons mal à des requêtes comme "amour" et "ouragan"  

> Qu'advient-il lorsque ChatGPT répond à une personne qui lui soumet ses symptomes que sa meilleure option est de se suicider ?

```bibtex @cite
@book{ertzscheidIALassautCyberespace2024,
        title = {Les IA à l'assaut Du Cyberespace},
        author = {Ertzscheid, Olivier},
        date = {2024-06-09},
        edition = {Édition standard},
        publisher = {C\&F éditions},
        location = {Caen},
        abstract = {« Le projet des grands capitaines d’industrie de la Tech, de Zuckerberg à Musk, n’est plus de permettre à l’humanité de se parler ni même de dialoguer avec des robots, mais de permettre à des robots de nous indiquer quoi faire, que dire et où regarder. » À l’heure de ChatGPT, la langue elle-même est devenue une production industrielle, accompagnant l’émergence d’un capitalisme linguistique. Olivier Ertzscheid part des usages de ce qu’on appelle abusivement « intelligence artificielle » pour en démonter les mécanismes. Il s’agit avant tout d’artefacts remplaçant le sens par la statistique, industrialisant la production documentaire et développant un Web synthétique. Sommes-nous à l’aube d’une nouvelle « lutte de classes linguistique » ?},
        isbn = {978-2-37662-085-3},
        pagetotal = {142},
        url = {https://cfeditions.com/ia-cyberespace/}
}
```

# 4. Comparer les modèles de langage entre eux



# 5. approches pédagogiques

## Testez, discutez, commentez, améliorez les propositions d'activités suivantes :

critères : 

- l'activité permet-elle d'atteindre l'objectif pédagogique ?
- l'activité sera t-elle encore efficace dans quelques mois ?
- l'activité est t-elle simple à mettre en place ? 
- les outils choisis pour l'activité sont-ils simples à utiliser ? 
- les outils choisis pour l'activité sont-ils représentatifs ? 
- les contenus choisis sont-ils intéressants, pertinents ?  
- l'activité met-elle en jeu les données personnelles de l'utilisateur / utilisatrice ?

reconnaissance d'images générées par IA (ou pas)

<iframe width=":w" height=":h" src="https://damienbelveze.github.io/CFCB_IA/reconnaissance_image.html" frameBorder="0" scrolling="no" styles="width:100%"></iframe>

Mesure des biais dans la génération d'images 


Demander à l'IA d'écrire une histoire pour Twine 



# 6. Enjeux environnementaux et sociaux

Si l'entraînement d'une IA est une opération très énergivore et très émettrice de gaz à effets de serre, la majeure partie de ces émissions provient de l'usage que nous faisons de ces modèles (= inférences)

L'activité suivante a pour objet de faire prendre conscience de certains ordres de grandeur en matière de consommation d'énergie et en fonction des types d'intelligence artificielle.

[ordres de grandeur dans la consommation](https://damienbelveze.github.io/ai_environnement/ai_consommation.html)


# 7 Quel positionnement pour les bibliothécaires / formateurs ?

êtes-vous d'accord avec ces principes : 

- les IAG sont capables d'hallucination, autant que possible on doit inciter à utiliser des outils sur lesquels on a le contrôle

- Le pire à propos des IAG, serait de ne rien faire et de continuer comme si ça n'existait pas

- On ne devrait pas permettre à un étudiant de faire avec une IAG quelque chose qu'il n'a pas encore appris à faire sans. 

- Les établissements devraient payer des licences aux versions payantes des IAG afin de mettre tous les étudiants sur un pied d'égalité

- La venue des IAG grand public est pour nous une motivation supplémentaire pour développer nos activités dans deux sens : la culture numérique et l'EMI



# 7. crédits logiciels

- Le cours a été réalisé à partir du logiciel libre [**Liascript**](https://github.com/liaScript), un interpréteur permettant de lire du markdown dans le navigateur et de le convertir automatiquement en html.    
- L'activité Timeline a été réalisée à partir du logiciel libre [**Chronoquiz**](https://www.chronoquiz.net/about) réalisé par Andrew A. Kashner et mis à disposition sur son propre serveur. Le fichier JSON qui a servi à ce jeu est disponible <a href="dans ce dossier" download>dans ce répertoire</a>     
- Les activités H5P ont été réalisées avec le logiciel libre [**logiquiz**](https://ladigitale.dev/logiquiz/) maintenu et mis à disposition par La Digitale. On peut les récupérer pour les adapter en cliquant sur "reuse".



# Bibliographie

@[bibliography.link.style(vancouver)](./biblio.bib)