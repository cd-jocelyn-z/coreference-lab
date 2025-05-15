# coreference-lab (branche `coreferee-spacy`)

Ce dépôt regroupe le code et les scripts développés dans le cadre d’un projet de Master dédié à l’évaluation des outils de résolution de coréférence en français. L’objectif est de comparer les méthodes traditionnelles (rule-based, statistiques) comme Coreferee, Cofr, Decofre, CorefUD, et les approches modernes basées sur les LLM.

## Structure du dépôt

- `XML-to-CONLL.py` : Conversion de documents XML et sorties Coreferee vers le format CoNLL-2012.  
- `coreferee_to_conll.py` : Génération de fichiers CoNLL-2012 à partir de texte brut ou de CoNLL, via spaCy + Coreferee.  
- `corefereetest.py` : Script minimal pour tester Coreferee sur un mini-corpus et visualiser les résultats.  
- `evaluate.py` : Scoring pairwise des chaînes (précision, rappel, F1) avec spaCy + Coreferee (compatible Pydantic<2.0).  
- `evaluate_all_metrics.py` : Calcul des métriques MUC, B³, CEAF, BLANC sur prédictions CoNLL-2012.  
- `journal.md` : Journal de bord et notes de développement.

## Prérequis

- Python 3.8+  
- spaCy 3.x  
- coreferee 1.x  
- pydantic < 2.0  

Installer les dépendances :
```bash
pip install spacy coreferee "pydantic<2.0"
python -m spacy download fr_core_news_md
coreferee install fr
```
## Utilisation

### Conversion de XML vers CoNLL-2012
```python
python XML-to-CONLL.py \
  --input_xml textes_CR.xml \
  --coref_file coreference_results.txt \
  --output_conll output.conll
```
### Conversion de texte brut / CoNLL

```python
python coreferee_to_conll.py \
  --input_file input.conll \
  --output_file output.conll \
  --spacy_model fr_core_news_md
```

### Évaluation des prédictions

```python
python evaluate.py \
  --corpus_directory path/to/gold_conll_dir \
  --language fr \
  --spacy_model fr_core_news_md

python evaluate_all_metrics.py gold.conll output.conll

```
