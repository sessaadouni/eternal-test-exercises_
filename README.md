# Instructions

Des exercices de test. Objectif: quelques minutes par exercice, en faire le maximum.

Faisables dans n'importe quel ordre. Chaque exercice doit être suivi d'un commit Git de cet exercice uniquement avec description de ce qui a été fait.

Bien entendu, il faut faire un fork du projet dans ton propre GitHub et envoyer dedans.


A la fin on attend pour chacun des exercices réalisés:
- le fichier test-report.txt
- le fichier coverage.txt
- le fichier test_xyz.py
- le fichier xyz.py

## Comment cloner ce répertoire de façon persistente (sur ton compte de l'IUT) et initialiser l'environnement

Commencer par forker ce dépôt dans ton GitHub personnel.

Copier-coller cela dans un terminal:

```bash
cd /iutv/Mes_Montages/${LOGNAME}
git clone https://github.com/TON-COMPTE/eternal-test-exercises.git eternal-test-exercises
cd eternal-test-exercises
make venv
```

Ensuite, pour ouvrir dans ton logiciel de développement (aka IDE):

```bash
code /iutv/Mes_Montages/${LOGNAME}
```

Dans VS Code, pense à préciser que ton interpréteur python est le virtualenv
qu'on vient de créer (Commandes dans Code -> "Python: Select Interpreter")

Si tu préfères utiliser le terminal directement avec Emacs ou (n)vim ou un autre éditeur de texte, pense à charger le virtualenv dans ton shell:

```bash
. /iut/Mes_Montages/${LOGNAME}/eternal-test-exercises/.venv/bin/activate
```

## Recommendations

Utiliser VS Code pour développer avec la complétion de syntaxe et des facilités de test.

Lire le code: tout est dedans. Le fichier d'instructions redonne juste le nom de l'exercice et des rappels sur Git en cas de doute.

Créer les fonctions de test pour un fichier `machin.py` dans un fichier nommé `test_machin.py`. Le test unitaire de la fonction `bidule` doit s'appeler `test_bidule` si cette dernière est simple et sinon si il y a deux fonctionnalités différentes de bidule "truc" et "chose" on peut créer `test_bidule_truc` et `test_bidule_chose`. De même, si un fichier `test_trucmuche.py` existe, l'exercice veut certainement que tu crées un fichier `trucmuche.py`

Ne pas chercher compliqué: les exercices sont faits pour être simples.

## Utiliser Git

Rappel:

- `git add <répertoire>` pour préparer le commit
- `git commit` pour effectuer le commit
- `git push` pour envoyer le commit vers le serveur central.

# Un exemple

Dans le dossier exemple-0 tu trouves un exercice résolu:

- l'exercice a été créé dans un commit à part
- ensuite, j'ai proposé une solution:
    - écrire une fonction reponse(question=None) qui va avoir le comportement décrit par le test
- et je l'ai commit: c'est le commit "eb41df06" que tu peux voir avec la commande `git log`

Pour produire ce commit et le publier, j'ai fait les commandes suivantes:

```bash
cd exemple-0
make test coverage
git add .
git commit -m "exercice(exemple-0): create function reponse() to provide answers"
git push
```
