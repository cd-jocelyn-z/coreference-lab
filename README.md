# Tester les LLMs
## Un petit guide pour lancer les annotations à partir des fichiers disponibles

> **Note :** Les prompts simples sont conçus pour tester comment combiner les textes à annoter, les LLMs utilisés pour l’annotation, et la gestion des fichiers.  
Cela permet d’accéder facilement aux informations nécessaires pour comparer les sorties générées par différents modèles.

L’intégration de **Langfuse** sera introduite prochainement.

### Les scripts :

- **parse_xml.py** : Ce script permet d’extraire des informations à partir d’un fichier XML contenant les données, puis de les mettre au format JSON.

- **prompts.json** :  
  - Chaque élément possède un champ `"id"` et un champ `"prompt"`.  
  - La sortie est enregistrée dans `data.json`.

- **main.py** : Ce script permet de lancer l’annotation effectuée par les modèles.  
  Actuellement, seuls les modèles suivants sont utilisés :
  1. mistral-7b-instruct  
  2. llama3.2  


Lors de l’exécution de `main.py`, le script lit l’`id` et le `prompt` disponibles dans `prompts.json`, ainsi que le `source_id` et le `text` provenant du fichier `data.json`.  
Il est conçu pour permettre de filtrer et sauvegarder ces informations au format JSON, afin de pouvoir ensuite les convertir en fichier CSV. Cela permet par exemple :
1. d’identifier quel prompt a été utilisé pour un texte donné avec un modèle donné,  
2. de voir quels résultats un modèle a produits pour un texte spécifique, etc.

### Résultat :
Lien pour accéder au dépôt des résultats : [*llm annotations*](https://drive.google.com/drive/folders/1iOgjbJre12ZkowCvpwESD0PqgGQCzF0q?usp=drive_link)

Un exemple du contenu du fichier `coref_annotations.json` :


```python
[
    {
    "prompt_id": 1,
    "prompt": "List the coreferences in this text.",
    "source_id": "text_000",
    "text": " La discrimination positive est-elle nécessaire pour réduire les inégalités ?...",
    "model": "mistral:7b-instruct",
    "result": "1. \"Il\" refers to the cannabis plant in the first sentence.\n2. \"Lui\" (the latter) also refers to the cannabis in the sixth sentence.\n3...
    }

]
```

