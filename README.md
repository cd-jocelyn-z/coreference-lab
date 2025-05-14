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
