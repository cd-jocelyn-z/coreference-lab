import xml.etree.ElementTree as ET
import json

tree = ET.parse("data.xml")
corpus = tree.getroot()


docs = []
for doc in corpus:
    if doc.text and doc.text.strip():
        docs.append({
            "class": doc.attrib.get("class"),
            "niveau": doc.attrib.get("niveau"),
            "source": doc.attrib.get("source"),
            "text": " ".join(line for line in doc.text.splitlines())
        })


with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(docs, f, ensure_ascii=False, indent=2)
