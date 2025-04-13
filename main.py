import ollama
from pydantic import BaseModel
import json
import argparse
from pathlib import Path
from typing import List, Optional
import pandas as pd
from tqdm import tqdm


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
    parser.add_argument("-ipp", "--input_prompts_path", type=str, required=True,
                        help="Le  chemin de prompts à passer aux LLMs")
    parser.add_argument("-op", "--output_path", type=str,
                        help="Le chemin à sauvegarder les résultats.")
    return parser.parse_args()

def load_json(data_path:Path, prompts_path:Path):
    with open(data_path) as data_file:
        docs = json.load(data_file)
    with open(prompts_path) as prompt_file:
        prompts = json.load(prompt_file)
    
    return docs, prompts

def run_llms(docs,prompts):

    models = [
        #"mistral:7b-instruct", 
        "llama3.2:latest",
        #"gemma3:4b",
    ]
    
    results = []

    for model_name in tqdm(models): 
        print(f"Model name: {model_name}")
        for prompt in prompts:
            prompt_id = prompt["id"]
            prompt_text = prompt["prompt"]

            for idx, doc in enumerate(docs[:1], start=1):
                text = doc['text']
                print(f"Analysis: Prompt {prompt_id}, Text {idx}")

                system_message = (
                    f"You are an expert in French linguistics, specializing in coreferencing."
                    "Identify all coreferencing mentions and add to the chain for each mention."
                    "{coref_id:[[token, position, 0],[token, position, 0], ...], "
                    "coref_id:[[token, position, 0], [token, position, 0], ...], ...}."
                )

                full_prompt = prompt_text + text

                response = ollama.chat(
                    model=model_name,
                    messages=[
                        {"role": "system", "content": system_message},
                        {"role": "user", "content": full_prompt}
                    ],
                    format=Coref.model_json_schema(),
                )
                
                coref = Coref.model_validate_json(response.message.content)

                results.append({
                    "prompt_id": prompt_id,
                    "prompt": prompt_text,
                    "source_id": f"text_{idx:03}",
                    "text": text,
                    "model": model_name,
                    "result": coref
                })

    return results

def save_json(llm_outputs: List[dict], path:Path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(llm_outputs, f, ensure_ascii=False, indent=2)


def main():
    """
    CLI: python main.py -idp data.json -ipp prompts.json -op corref_annotations
    """
    args = get_args()
    data_path = args.input_data_path
    prompts_path = args.input_prompts_path
    output_path = Path(args.output_path)

    docs, prompts = load_json(data_path, prompts_path)
    llm_outputs = run_llms(docs, prompts)
    df_results = pd.DataFrame(llm_outputs).reindex(columns=
        ["prompt_id","prompt","source_id","text", "model", "result"])
    print(df_results)

    if output_path:
        save_json(llm_outputs, Path(output_path))
        csv_path = Path(output_path).with_suffix(".csv")
        df_results.to_csv(csv_path, index=False, header=True)
            

if __name__ == "__main__":
    main()