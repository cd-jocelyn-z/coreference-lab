from pathlib import Path
from textwrap import dedent
import json
import ollama
from corpus_utils import load_json, save_json
from datastructures import Corpus, Doc, Coref, Mention, CorefSchemaList

def create_prompt(text: str):
    return [
        {
            "role": "system",
            "content": dedent("""
            Vous êtes un expert en linguistique française spécialisé dans la résolution des coréférences.

            Votre tâche est d'identifier toutes les chaînes de coréférences dans un texte donné. Pour chaque entité ou groupe d'entités, vous devez produire une **sortie structurée au format JSON**, suivant précisément le format ci-dessous.

            Chaque chaîne doit être représentée par un objet contenant :
            - `id` : un identifiant unique pour la chaîne (entier)
            - `entity` : l'entité principale ou le groupe d'entités (chaîne ou liste de chaînes)
            - `mentions` : une liste d'objets, chacun contenant :
                - `token` : le mot tel qu'il apparaît dans le texte (chaîne)
                - `position` : la position du token dans le texte, en commençant à 0
                - `annotation` : toujours 0

            Retournez UNIQUEMENT un tableau JSON contenant ces objets, sans aucun commentaire ni explication.
            Votre réponse DOIT commencer par '[' et se terminer par ']'.
            La réponse doit être un JSON valide et parseable.

            Exemple de sortie attendue :
            [
              {
                "id": 0,
                "entity": "Julie",
                "mentions": [
                  {"token": "elle", "position": 2, "annotation": 0},
                  {"token": "son", "position": 7, "annotation": 0},
                  {"token": "Julie", "position": 10, "annotation": 0}
                ]
              },
              {
                "id": 1,
                "entity": ["Julie", "mari"],
                "mentions": [
                  {"token": "elle", "position": 17, "annotation": 0},
                  {"token": "mari", "position": 20, "annotation": 0},
                  {"token": "ils", "position": 23, "annotation": 0}
                ]
              }
            ]

            IMPORTANT : Si une mention fait référence à un groupe, indiquez tous les membres du groupe dans `entity` comme une liste.
            NE FOURNISSEZ AUCUN COMMENTAIRE NI TEXTE EN DEHORS DU TABLEAU JSON.
            VOTRE RÉPONSE DOIT ÊTRE UN JSON VALIDE ET PARSEABLE.
            """)
        },
        {
            "role": "assistant",
            "content": "Compris. Je retournerai uniquement un tableau JSON valide et parseable, sans aucun texte supplémentaire."
        },
        {
            "role": "user",
            "content": f"Voici le texte à analyser :\n\n{text}"
        }
    ]


def llm_annotator(corpus_path: Path, model_name: str, output_path: Path):
    corpus = load_json(corpus_path)
    results = []

    for i, doc in enumerate(corpus.docs):
        print(f"\n\nDocument {i+1}/{len(corpus.docs)} — {doc.source}")
        response = ollama.chat(
            model=model_name,
            messages=create_prompt(doc.text),
            format=CorefSchemaList.model_json_schema(),
        )

        try:
            corefs_raw = json.loads(response.message.content)
            new_corefs = []

            validated_corefs = CorefSchemaList.model_validate(corefs_raw)
            corefs = validated_corefs.corefs
            for coref in corefs:
                mentions = [Mention(**m.model_dump()) for m in coref.mentions]
                entity = coref.entity if isinstance(coref.entity, str) else ", ".join(coref.entity)
                new_corefs.append(Coref(id=coref.id, entity=entity, mentions=mentions))
        except Exception as e:
            print(f"Erreur lors du parsing de la sortie du modèle : {e}")
            new_corefs = []

        annotated_doc = Doc(
            classe=doc.classe,
            niveau=doc.niveau,
            source=doc.source,
            text=doc.text,
            corefs=new_corefs
        )
        results.append(annotated_doc)

    annotated_corpus = Corpus(docs=results)
    save_json(annotated_corpus, output_path)

if __name__ == "__main__":
    corpus = load_json(Path("data/data.json"))
    test_corpus = Corpus(docs=corpus.docs[0:]) # ajouté si on souhaite tester sur qqs fichiers
    test_corpus_path = Path("data/test_data.json")
    save_json(test_corpus, test_corpus_path)
    llm_annotator(
        corpus_path=test_corpus_path,
        # model_name="deepseek-r1:14b",
        model_name="gemma3:4b",
        # output_path=Path("data/data_enriched-deepseek.json,
        output_path=Path("data/data_enriched-gemma.json")
    )
