from dataclasses import dataclass, field
from typing import List
from pydantic import BaseModel

class Mention(BaseModel):
    token: str
    position: int
    annotation: int

class Coref(BaseModel):
    id: int                  
    entity: str            
    mentions: List[Mention]  

@dataclass
class Doc:
    classe: str
    niveau: str
    source: str
    text: str
    corefs: List[Coref] = field(default_factory=list)

@dataclass
class Corpus:
    docs: List[Doc] = field(default_factory=list)
