# decofre

## Mise en place de votre environnement virtuel
Il faut disposer d’un environnement virtuel qui nous permet de lancer l’outil.

Selon le fichier `setup.cfg`, ligne 27 :
`python_requires = >=3.8`

Vous pouvez utiliser, par exemple, Python 3.9.

Pour utiliser une version plus ancienne de Python, vous pouvez recourir à pyenv (voir : https://www.agencedebord.com/blog/changer-de-version-de-python-avec-pyenv).

`$ pip install pyenv`

`$ pyenv install 3.9.13`

Ensuite, lors de la création de votre environnement virtuel pour le projet, au lieu d'exécuter :

`$ python3 -m venv .venv`

qui utilise la version globale de Python installée sur votre machine, procédez comme suit pour spécifier la version de Python de votre choix.

```python
$ Users/jocelyn/.pyenv/versions/3.9.13/bin/python -m venv .venv
$ source .venv/bin/activate
$ python -m pip install decofre
$ python -m spacy download fr_core_news_lg
```

## Utiliser decofre-train
Pour lancer une première test de l'outil :

Vous pouvez nommer le dossier de sorite "sanity_output" dans la ligne de commandes :

```python
$ decofre-train --config tests/sanity-check.jsonnet --model-config decofre/models/default.jsonnet --out-dir sanity_output 
```     

Après vous aurez un dossier sanity_ouput.

**Note :** il se peut que auriez une erreur comme la suite:

    >File "/Users/jocelyn/Workspace_B/active/03_nanterre/01_enrichissment_corpus/project_test_3/decofre/.venv/lib/python3.9/site-packages/torch/serialization.py", line 1470, in load
        raise pickle.UnpicklingError(_get_wo_message(str(e))) from None
    _pickle.UnpicklingError: Weights only load failed. In PyTorch 2.6, we changed the default value of the `weights_only` argument in `torch.load` from `False` to `True`. Re-running `torch.load` with `weights_only` set to `False` will likely succeed, but it can result in arbitrary code execution. Do it only if you got the file from a trusted source.
    Please file an issue with the following so that we can make `weights_only=True` compatible with your use case: WeightsUnpickler error: Unsupported operand 149

    Check the documentation of torch.load to learn more about types accepted by default with weights_only https://pytorch.org/docs/stable/generated/torch.load.html.


donc pour se faire: il faut juste downgrade la version de torch : 

`$ python -m pip install --upgrade "torch<2.6"`
   

Vous pouvez ensuite relancer :

    decofre-train --config tests/sanity-check.jsonnet --model-config decofre/models/default.jsonnet --out-dir sanity_output

Maintenant, vous devriez avoir un dossier sanity_output à consulter pour l'étape suivante.

## Utiliser decofre-infer
Pour ce faire, assurez-vous de bien vérifier le dossier sanity_output. Normalement, les fichiers coref.model et detector.model se trouvent au premier niveau. Prenez le chemin relatif de chacun.

Ensuite, dans le sous-dossier tests, vous trouverez un sous-dossier fixtures contenant un fichier raw.txt. Prenez également son chemin relatif.

Dès que vous avez ces informations, remplissez la ligne de commande.

```python
$ decofre-infer path/to/detector.model path/to/coref.model path/to/raw_text.txt
```

 Le ligne de commande que j'ai fait :

 ```python 
$ decofre-infer sanity_output/detector.model sanity_output/coref.model tests/fixtures/raw_text.txt
```