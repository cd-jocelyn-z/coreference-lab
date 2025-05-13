from datastructures import Corpus, Doc, Coref
from pathlib import Path
import json

def load_json(data_path: Path) -> Corpus:
    docs_list = []

    with open(data_path, encoding="utf-8") as data_file:
        docs = json.load(data_file)

    for doc in docs:
        corefs = [Coref(**c) for c in doc.get("corefs", [])]
        current = Doc(
            classe=doc["class"],
            niveau=doc["niveau"],
            source=doc["source"],
            text=doc["text"],
            corefs=corefs
        )
        docs_list.append(current)

    return Corpus(docs=docs_list)

def save_json(corpus: Corpus, output_file: Path) -> None:
    data = []

    for doc in corpus.docs:
        current = {
            "class": doc.classe,
            "niveau": doc.niveau,
            "source": doc.source,
            "text": doc.text,
            "corefs": [coref.dict() for coref in getattr(doc, "corefs", [])]
        }
        data.append(current)

    with open(output_file, "w", encoding="utf-8") as outfile:
        json.dump(data, outfile, indent=2, ensure_ascii=False)
