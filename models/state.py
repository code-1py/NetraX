from dataclasses import dataclass , field
from .service import Service
class State:
    state:str|None = None
    reason:str|None = None
    reason_ttl:int|None = None
    service:Service|None = None