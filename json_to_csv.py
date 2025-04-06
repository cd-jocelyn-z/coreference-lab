import pandas as pd
import json

with open("coref_annotations.json", "r", encoding="utf-8") as f:
    data = json.load(f)

df = pd.DataFrame(data)
df.to_csv("coref_annotations.csv", index=False, encoding="utf-8")
