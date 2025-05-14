from dataclasses import dataclass, field
from typing import List, Union
from pydantic import BaseModel

class Mention(BaseModel):
    token: str
    position: int
    annotation: int

class Coref(BaseModel):
    id: int
    entity: str
    mentions: List[Mention]

class MentionSchema(BaseModel):
    token: str
    position: int
    annotation: int

class CorefSchema(BaseModel):
    id: int
    entity: Union[str, List[str]]
    mentions: List[MentionSchema]

class CorefSchemaList(BaseModel):
    corefs: List[CorefSchema]

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
