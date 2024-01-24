from pydantic import BaseModel, field_validator
from typing import Any
import pandas as pd

class DataFrameModel(BaseModel):
    df: Any

    @field_validator('df')
    def check_is_dataframe(cls, v):
        if not isinstance(v, pd.DataFrame):
            raise ValueError("df must be a pandas DataFrame")
        return v