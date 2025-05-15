## Branche `prompts`

Cette branche regroupe nos expérimentations autour de la génération et de la gestion de prompts pour les LLMs :

- **Statut**  
  - 5 commits en avance et 27 commits en retard par rapport à `main`.
- **Fichiers clés**  
  - `prompts.md` : documentation des prompts testés, exemples et retours d’expérience.  
  - `prompts.txt` : fichier brut de collecte des prompts initiaux pour différents scénarios (coref, reformulation, etc.).  
  - `mistral.py` : script de génération et d’envoi de prompts à un modèle Mistral (ou tout autre API LLM).  
  - `README.md` : notice d’introduction à l’usage de la branche et aux dépendances requises.  
  - `.gitignore` : fichiers et dossiers à exclure du suivi Git.
- **Objectif**  
  Centraliser toutes les ressources et scripts permettant de tester différentes formulations de prompts, d’évaluer leur impact sur la qualité des réponses pour la tâche de coréférence, et de faciliter l’automatisation des expérimentations.
