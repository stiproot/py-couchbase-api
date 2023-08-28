from pydantic import BaseModel
from typing import List


class QryReq(BaseModel):
    query: str
    params: List[str]
