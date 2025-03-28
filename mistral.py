import ollama

text = """
Ainsi, la discrimination positive, lorsqu’elle est appliquée consiste, à favoriser des mesures visant à promouvoir : l’égalité des chances, l'accès à l'éducation, à l'emploi, à la formation (la politique d’égalité des chances mise en place par les institutions Science Po pour les étudiants issues des minorités) ou encore l'octroi de bourses sur critère sociaux mise en place par le Crous ; en vue de créer des conditions plus équitables, pour réduire les disparités économiques, encourager la diversité culturelle, à travers la création de modèles positifs, pouvant offrir aux groupes défavorisés des opportunités qui leur ont souvent été refusées dans le passé.
En Afrique du Sud ; elle a permis la représentation équitable de chaque groupe racial dans la vie sociale, économique et politique.
"""

prompt = f"""Tu es un expert dans la langue française. Identifie les expressions qui font référence à la même entité dans ce texte. 
Pour chaque groupe de co-références, indique :
1. L'antécédent.
2. Les co-références.

Texte :
{text}

Qui suivent la forme :
[antecedant] : [co-référence 1, co-référence 2, ...]
"""

response = ollama.chat(model="mistral:7b-instruct", messages=[
    {"role": "user", "content": prompt}
])

print(response['message']['content'])