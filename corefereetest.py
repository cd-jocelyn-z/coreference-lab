import coreferee
import spacy
import xml.etree.ElementTree as ET
import io
import sys

nlp = spacy.load("fr_core_news_lg")
nlp.add_pipe("coreferee")

xml_path = "/home/jeanne/Desktop/NewFolder/textes_CR.xml"
output_file = "coreference_results.txt"

try:
    tree = ET.parse(xml_path)
    root = tree.getroot()
except Exception as e:
    print(f"Error reading XML file: {e}")
    exit(1)

extracted_text = ""
for doc_elem in root.findall(".//doc"):
       if doc_elem.text:
        extracted_text += doc_elem.text.strip() + " "

doc = nlp(extracted_text)

if len(doc) == 0:
    print("No text extracted from XML. Please check the XML structure.")
    exit(1)

buffer = io.StringIO()
old_stdout = sys.stdout
sys.stdout = buffer

doc._.coref_chains.print()

sys.stdout = old_stdout
formatted_coref_output = buffer.getvalue()

with open(output_file, "w", encoding="utf-8") as f:
    f.write(formatted_coref_output)

print(f"Coreference results have been written to {output_file}.")