from typing import List
from pydantic import BaseModel

class User(BaseModel):
    dc_id: int
    tags: List[str]
    tags_with_id: List[int]
    

users = {
    806935115707056130: User(dc_id=806935115707056130, tags=["test"], tags_with_id=[938796651877920859])
}