from pydantic import BaseModel, Field
from typing import Dict

example = {
    '01/2023': 0.1,
    '02/2023': 0.2
}

class MetricsModel(BaseModel):
    mrr: Dict[str, float] = Field(..., example = example)
    chunrate: Dict[str, float] = Field(..., example = example)