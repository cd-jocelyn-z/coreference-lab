import ollama
import json

with open("data.json") as data_file:
    docs = json.load(data_file)
with open("prompts.json") as prompt_file:
    prompts = json.load(prompt_file)

models = ["mistral:7b-instruct","llama3.2:latest" ]
results = []

for model_name in models: 

    for prompt_obj in prompts:
        prompt_id = prompt_obj["id"]
        prompt_text = prompt_obj["prompt"]

        for idx, doc in enumerate(docs[:2]):
            text = doc['text']
            full_prompt = prompt_text + "\n\n" + text
            print(f"Analysis: Prompt {prompt_id}, Text {idx}")

            response = ollama.chat(
                model=model_name,
                messages=[{"role": "user", "content": full_prompt}]
            )

            annotated = response['message']['content']

            results.append({
                "prompt_id": prompt_id,
                "prompt": prompt_text,
                "source_id": f"text_{idx:03}",
                "text": text,
                "model": model_name,
                "result": annotated
            })

with open("coref_annotations.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)