import ollama
from pydantic import BaseModel
import json
import argparse
from pathlib import Path
from typing import List
import pandas as pd
from tqdm import tqdm
from textwrap import dedent

class Chain(BaseModel):
    token: str
    position: int
    annotation: int

class Coref(BaseModel):
    id: str
    chains: List[List[Chain]]

def get_args():
    parser = argparse.ArgumentParser(description="Tester les LLMS")
    parser.add_argument("-idp", "--input_data_path", type=str, required=True,
                        help="Le chemin de données à passer aux LLMs")
    parser.add_argument("-op", "--output_path", type=str,
                        help="Le chemin à sauvegarder les résultats.")
    parser.add_argument("-n", "--num_texts", type=int, default=3,
                    help="Number of documents to test.")
    return parser.parse_args()

def create_prompt(text: str):
    
    prompt_messages = [

        {"role": "system",
         "content": dedent("""
        Vous êtes un expert en linguistique française, spécialisé dans la résolution des coréférences.
        Votre rôle est d’identifier les coréférences dans le texte fourni.
        """)

        },

        # {
        #     "role": "system",
        #     "content": dedent("""
        #         Vous êtes un expert en linguistique française, spécialisé dans la résolution des coréférences.
        #         Identifiez toutes les mentions coréférentielles et regroupez-les en chaînes.
        #         Retournez le résultat au format suivant :
        #         {coref_id: [[token, position, 0], [token, position, 0], ...], 
        #          coref_id: [[token, position, 0], [token, position, 0], ...], ...}.
        #     """)
        # },

        {"role": "assistant",
         "content": "Je vais analyser l’ensemble votre texte français et repérer les mentions coréférentielles. "},

        {"role": "user",
         "content": f"""
         For context: return 
         Parfait ! Voici le texte français à analyser{text}, 
        
         """}
        ]

    return prompt_messages

def load_json(data_path:Path):
    with open(data_path) as data_file:
        docs = json.load(data_file)
    
    return docs

def run_llms(texts: List[str]):
    models = [
        # "deepseek-r1:7b", 
        "llama3:8b",
        #"mistral:7b-instruct",
    ]
    
    results = []

    for model_name in tqdm(models): 
        print(f"Model name: {model_name}")
        for text_info in texts:
            text_id = text_info["source"]
            text = text_info["text"]
            response = ollama.chat(
                model=model_name,
                messages=create_prompt(text),
                format=Coref.model_json_schema(),
            )
            
            coref = Coref.model_validate_json(response.message.content)

            print(f"doc id: {text_id}")
            print(f"coref: {coref}")
            print(f"total coref chains: {len(coref.chains)}")
            print()

            results.append({
                "text_id": text_id,
                "text": text,
                "model": model_name,
                "result": coref.model_dump() if coref else None 
            })


    return results

def save_json(llm_outputs: List[dict], path:Path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(llm_outputs, f, ensure_ascii=False, indent=2)


def main():
    """
    CLI: python main_v3.py -idp data.json -op coref_annotations

    Note: By default, the number of documents to run is set to 3.

    You can specify the number of documents you'd like to test using the -n flag:
    CLI: python main_v3.py -idp data.json -op coref_annotations -n 10
    """
    args = get_args()
    data_path = args.input_data_path
    file_name = Path(args.output_path)
    nb_texts = args.num_texts

    texts = load_json(data_path)
    llm_outputs = run_llms(texts[:nb_texts])

    df_results = pd.DataFrame(llm_outputs).reindex(columns=
        ["text_id","text","model","result"])
    print(df_results)

    if args.output_path:
        output_folder = Path("llm_outputs")
        output_folder.mkdir(exist_ok=True)
        output_path = output_folder / file_name

        save_json(llm_outputs, output_path)
        csv_path = output_path.with_suffix(".csv")
        df_results.to_csv(csv_path, index=False, header=True)
            

if __name__ == "__main__":
    main()