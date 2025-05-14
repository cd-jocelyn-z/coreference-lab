import xml.etree.ElementTree as ET
from corpus_utils import save_json
from datastructures import Corpus, Doc
from pathlib import Path

def parse_xml(path: Path) -> Corpus:
    tree = ET.parse(path)
    corpus = tree.getroot()

    docs = []
    for doc_elem in corpus:
        if doc_elem.text and doc_elem.text.strip():
            doc = Doc(
                classe=doc_elem.attrib.get("class", ""),
                niveau=doc_elem.attrib.get("niveau", ""),
                source=doc_elem.attrib.get("source", ""),
                text=" ".join(line.strip() for line in doc_elem.text.splitlines()),
                corefs=[]
            )
            docs.append(doc)

    return Corpus(docs=docs)

corpus = parse_xml(Path("data/data.xml"))
save_json(corpus, Path("data/data.json"))
