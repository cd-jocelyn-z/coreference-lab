import xml.etree.ElementTree as ET
import re
import os

# Input files
XML_FILE = 'textes_CR.xml'
COREF_FILE = 'coreference_results.txt'
OUTPUT_FILE = 'output.conll'

# Load the XML file
with open(XML_FILE, 'r', encoding='utf-8') as xml_file:
    tree = ET.parse(xml_file)
    root = tree.getroot()

# Extract text from the XML file
sentences = []
for doc in root.findall('.//texte'):
    text = doc.text.strip()
    # Split the text into sentences (basic split for now)
    sentences += re.split(r'(\.|\?|\!)\s+', text)

# Load the coreference file
coref_chains = {}
with open(COREF_FILE, 'r', encoding='utf-8') as coref_file:
    for line in coref_file:
        if line.strip():
            # Extract chain ID and mentions
            chain_id, mentions = line.strip().split(':')
            chain_id = chain_id.strip()
            mentions = [m.strip() for m in mentions.split(',')]
            coref_chains[chain_id] = mentions

# Prepare the CoNLL output
with open(OUTPUT_FILE, 'w', encoding='utf-8') as output_file:
    doc_id = 1
    for i, sentence in enumerate(sentences):
        tokens = sentence.split()
        output_file.write(f"#begin document (doc{doc_id});\n")
        for j, token in enumerate(tokens):
            coref_tag = "-"
            # Check if the token is part of a coreference chain
            for chain_id, mentions in coref_chains.items():
                for mention in mentions:
                    if token in mention:
                        coref_tag = f"({chain_id})"
            # Write the token line
            output_file.write(f"{j+1}\t{token}\t-\t-\t{coref_tag}\n")
        output_file.write("#end document\n\n")
        doc_id += 1

print(f"Conversion complete. Output written to {OUTPUT_FILE}.")
import xml.etree.ElementTree as ET
import re
import os

# Input files
XML_FILE = 'textes_CR.xml'
COREF_FILE = 'coreference_results.txt'
OUTPUT_FILE = 'output.conll'

# Load the XML file
with open(XML_FILE, 'r', encoding='utf-8') as xml_file:
    tree = ET.parse(xml_file)
    root = tree.getroot()

# Extract text from the XML file
sentences = []
for doc in root.findall('.//texte'):
    text = doc.text.strip()
    # Split the text into sentences (basic split for now)
    sentences += re.split(r'(\.|\?|\!)\s+', text)

# Load the coreference file
coref_chains = {}
with open(COREF_FILE, 'r', encoding='utf-8') as coref_file:
    for line in coref_file:
        if line.strip():
            # Extract chain ID and mentions
            chain_id, mentions = line.strip().split(':')
            chain_id = chain_id.strip()
            mentions = [m.strip() for m in mentions.split(',')]
            coref_chains[chain_id] = mentions

# Prepare the CoNLL output
with open(OUTPUT_FILE, 'w', encoding='utf-8') as output_file:
    doc_id = 1
    for i, sentence in enumerate(sentences):
        tokens = sentence.split()
        output_file.write(f"#begin document (doc{doc_id});\n")
        for j, token in enumerate(tokens):
            coref_tag = "-"
            # Check if the token is part of a coreference chain
            for chain_id, mentions in coref_chains.items():
                for mention in mentions:
                    if token in mention:
                        coref_tag = f"({chain_id})"
            # Write the token line
            output_file.write(f"{j+1}\t{token}\t-\t-\t{coref_tag}\n")
        output_file.write("#end document\n\n")
        doc_id += 1

print(f"Conversion complete. Output written to {OUTPUT_FILE}.")
