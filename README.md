# Projet Outils
Ce projet a pour objectif de tester et évaluer différents outils de résolution de coréférences appliqués au français, allant des modèles traditionnels aux LLM modernes. Il vise à comprendre les performances, les limites, et les possibilités de correction/annotation semi-automatique.

## 🎯 Objectifs du projet 

1. Tester un ou plusieurs outils de coréférence sur un corpus brut :
- Outils testés :
  - Coreferee (extension spaCy)
  - CorefUD → recommandé par Loïc Grobol, créateur de DeCOFre

2. Segmenter le corpus si le traitement est trop long (par exemple en phrases ou paragraphes).

3. Corriger manuellement les résultats de l'outil pour créer un corpus de référence (gold standard).

4. Évaluer automatiquement les performances des outils par rapport au corpus de référence.

5. Tester des modèles génératifs de type LLM pour la résolution de coréférences :
  - Exemples : LLaMA, GPT, etc.
  - Comparer leurs sorties avec les outils traditionnels.

6. Évaluer à nouveau les performances des LLM et comparer aux approches précédentes.


### Outil de coréférence utilisant des LLMs

Ce projet vise à enrichir des données textuelles avec une analyse de coréférence.
La stratégie de *zero-shot prompting* a été utilisée afin de comprendre le comportement de deux modèles open source.

Les modèles **Gemma 3:4b** et **DeepSeek-R1:14b** ont été testés pour cette tâche.

[![Screenshot-2025-05-15-at-00-05-24.png](https://i.postimg.cc/V6XHLV7M/Screenshot-2025-05-15-at-00-05-24.png)](https://postimg.cc/mz2Sm8W2)

---

**Scripts principaux :**

- `parse_xml.py`
- `run_llm_lab.py`
- `run_llm_annotator.py`

Le flux de traitement est le suivant :
`data.xml` → `data.json` → `data_enriched-deepseek.json` / `data_enriched-gemma.json`

---

1. **Sortie non structurée** : le comportement du modèle face à une sortie libre.
   Liens vers les sorties :

   - DeepSeek : [Drive](https://drive.google.com/drive/folders/16OVy3AKgNdiCduqr_eUobk_FhoomeMgz?usp=sharing)
   - Gemma : [Drive](https://drive.google.com/drive/folders/1bYt4hNPmkHsZ79XEdO4L19HR7HrJNUSd?usp=sharing)

2. **Sortie semi-structurée** : on analyse la capacité du modèle à comprendre une structure partiellement définie.
   Liens vers les sorties :

   - DeepSeek : [Drive](https://drive.google.com/drive/folders/16r4J5tDH8X2oj3fdvYc7ZR9Bx3ylV9n7?usp=sharing)
   - Gemma : [Drive](https://drive.google.com/drive/folders/19sjHiPG9Sws-qfV8IrhWa1JGSwu_E6U5?usp=sharing)

3. **Sortie structurée** : on applique le prompt ayant généré la structure la plus pertinente. Cette structure est ensuite ajoutée dans un champ `corefs`, destiné à stocker l’analyse produite par le LLM.
   Liens vers les sorties :

   - DeepSeek : [Drive](https://drive.google.com/drive/folders/1P-x7Xj3OPt0d6CFoGuGISz_hmclV4Rrg?usp=sharing)
   - Gemma : [Drive](https://drive.google.com/drive/folders/1otDT6AtdFPi2ICboqfVW8Oq1Lh0JsM64?usp=sharing)

Cette implémentation expérimentale illustre comment les LLMs peuvent être utilisés comme outil d’enrichissement du corpus.
Bien que certaines sorties présentent encore des imprécisions, le projet ouvre la voie à de nombreuses améliorations possibles, notamment en matière de sélection de modèles, d’optimisation des prompts et de post-traitement des résultats.

## Informations sur les branches
## Branches disponibles

Ce dépôt est structuré en plusieurs branches thématiques :

- **`coreferee-spacy`**  
  - Contient tous les scripts de conversion et d’évaluation basés sur spaCy + Coreferee.  
  - Statut : scripts stables pour la conversion (XML/texte → CoNLL-2012) et l’évaluation (`evaluate.py`, `evaluate_all_metrics.py`).

- **`corefud`**  
  - Regroupe nos tentatives d’intégration de **CorefUD** pour la coréférence UD/CoNLL-U.  
  - Statut : installation non aboutie (dépendances obsolètes), mais lien vers le **CorefUD Scorer** :  
    https://github.com/ufal/corefud-scorer

- **`docsdev`**  
  - Documentation et guides d’annotation manuelle (outil Decofre).  
  - Fichiers clés :  
    - `Coreference-Annotation-Setup.md` (guide d’installation/config)  
    - `README.md` (présentation de la branche)

- **`prompts`**  
  - Expérimentations de prompts pour LLMs (coref, reformulation, etc.).  
  - Fichiers :  
    - `prompts.md` (documentation des prompts et retours)  
    - `prompts.txt` (collecte de formulations brutes)  
    - `mistral.py` (script d’envoi de prompts)

Chaque branche est conçue pour isoler un aspect du projet : conversion & scoring (coreferee-spacy), evaluation UD (corefud), documentation (docsdev) et tests de prompts (prompts).  


## Auteurs

- Jeanne Costantini

- Jourdan Wilson

- Jocelyn Zaruma

- Lina Sabir

## Remerciements

- Sur la base des données et du projet initial de Vanessa Gaudray Bouju.

- Encadrement : Prof. Iris Taravella.
