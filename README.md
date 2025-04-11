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
