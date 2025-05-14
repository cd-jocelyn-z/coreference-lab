import ollama
from pathlib import Path
from textwrap import dedent
from corpus_utils import load_json

#################################################################################################
## On teste ici les LLMs en isolation. Pas besoin que les sorties soient structurées à ce stade.
## L'objectif est d'explorer différents prompts et d'observer les comportements du modèle.
## Dès qu’un comportement satisfaisant est identifié, on note le prompt associé.
## Ensuite, ce prompt pourra être intégré dans le script final : run_llm_annotator.py.
##
## Les tests sont réalisés manuellement, sans pipeline ni validation automatique.
##
## Pour consigner les résultats dans un fichier lors des tests :
## $ python run_llm_lab.py > model_name_output-x.txt
#################################################################################################

def create_prompt(text: str):
    return [
        {
            "role": "system",
            "content": dedent("""
                Vous êtes un expert en linguistique française, spécialisé dans la résolution des coréférences.
                Votre rôle est d’identifier les coréférences dans le texte fourni.
            """)
        },
        {
            "role": "assistant",
            "content": "Je vais analyser l’ensemble de votre texte français et repérer les mentions coréférentielles."
        },
        {
            "role": "user",
            "content": f"Parfait ! Voici le texte français à analyser : {text}"
        }
    ]

def run_llms(text, source):
    models = [
        # "mistral:7b-instruct",
        # "llama3:8b",
        # "deepseek-r1:7b",
        "gemma3:4b",
        # "deepseek-r1:14b"
    ]

    for model_name in models:
        print(f"\n### Source : {source} | Modèle : {model_name}\n")
        response = ollama.chat(
            model=model_name,
            messages=create_prompt(text)
        )
        print(response.message.content)

data_path = Path("data/data.json")
corpus = load_json(data_path)


for doc in corpus.docs[125:150]:
    print(f"\n{'='*80}")
    print(f"### Processing : {doc.source}")
    print(f"{'='*80}\n")
    run_llms(doc.text, doc.source)

#:10
# 10:20
# 20:30
# 30:39 # 38 is missing # 30-40
# 39:49 # to process docs 41-50
# 49:59
# 59:69
# 69:79 # 70-80
# 79:89 # 85 is missing, so 91 is in this range